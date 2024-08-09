'''
PReFScript: A Partial Recursive Functions Lab

Rather: Towards a Partial Recursive Functions lab.

Author: Jose L Balcazar, ORCID 0000-0003-4248-4528, april 2023 onwards 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Project started: mid Germinal 2003.
Current version: 0.5, mid Thermidor 2024.

A Python-based environment to explore and experiment with partial 
recursive functions; naturally doubles as a (purely functional) 
programming language, but it is not intended to be used as such.

Each function in a script has: associated Gödel number, nickname, 
comments, and code (string); also, the last operation used to 
construct it. Then, in a separate dict (used as namespace for 
eval calls), a runnable version of the code.

Nicknames are alphanum strings not starting with a number (no surprise).
'''

from collections import defaultdict as ddict
from re import compile as re_compile, finditer as re_finditer
from ascii7io import int2str, str2int, int2raw_str # users are not expected to need int2raw_str
import cantorpairs
cp = cantorpairs

__version__ = "1.1"

# ~ In order to omit Gödel numbers too high, around 300 decimal digits,
# ~ LIMIT_GNUM set to 2**1000 but computed much faster via bit shift

LIMIT_GNUM = 2 << 999

class FunData(dict):
    'Simple class for PReFScript functions data'

    def __init__(self, nick = None, comment = None, how_def = None, def_on = None):
        dict.__init__(self)
        self["nick"] = nick # function name
        self["comment"] = comment
        self["how_def"] = how_def
        self["def_on"] = def_on

    def __str__(self):
        return self["nick"] + "\n " + self["comment"] 

    def how_def(self):
        if self["how_def"] == "basic":
            return "basic"
        return self["how_def"] + ": " + ' '.join(on_what for on_what in self["def_on"])


def mu(x, test):
    "ancillary linear search function for implementing mu-minimization"
    z = 0
    while not test(cp.dp(x, z)):
        z += 1
    return z


def prim_rec(is_base, base, recurse):
	"ancillary course-of-values primitive recursion more efficient than by minimization"

	def c_of_v(x):
		"create the full course of values"
		sq = 0
		for y in range(x + 1):
			new = base(y) if is_base(y) else recurse(cp.dp(y, sq))
			sq = cp.dp(new, sq)
		return sq

	return lambda x: cp.pr_L(c_of_v(x))


class Parser:
    '''Prepare an re-based parser to be used upon reading scripts
    The single Parser with single parse generator is likely to mess up
    the recursive imports, I bet it does not work yet.
    '''

    def __init__(self):
        "group names require Python >= 3.11"
        from re import compile as re_compile, finditer as re_finditer
        about = r"\s*\.about(?P<about>.*)\n"                           # arbitrary documentation
        pragma = r"\s*\.pragma\s+(?P<which>\w+):?\s+(?P<what>\w+)\s*"  # compilation directives
        importing = r"\s*\.import\s+(?P<to_import>[\w._-]+)\s*"        # additional external script
        a7str = r'''(?P<quote>['"])(?P<a7str>.*)(?P=quote)'''
        startdef = r"\d+\s+define\:\s*"
        group1_nick = r"(?P<nick>\w+)\s+"
        group2_comment = r"\[\s*(?P<comment>(\w|\s|[.,:;<>=)(?!/+*-])+)\]\s+" 
        group4_how = r"(?P<how>pair|comp|mu|compair|primrec|ascii_const)\s+" 
        group5_on_what = r"((?P<on_what>([a-zA-Z_]\w*\s+)+)|" + a7str + ")"  # nick args required not to start with a number
        define = (startdef +  
              group1_nick + 
              group2_comment + 
              group4_how +
              group5_on_what)
        self.the_parser = re_compile(define + '|' + about + '|' + pragma + '|' + importing)

    def parse(self, source):
        for thing in re_finditer(self.the_parser, source):
            "can one find out non-matched portions to message the user about?"
            things = thing.groupdict(default = '')
            if about := things['about']:
                yield 'about', about
            if which := things['which']:
                yield 'pragma', (which, things['what'])
            if to_import := things['to_import']:
                yield 'import', to_import
            if nick := things['nick']:
                if things['how'] == "ascii_const":
                    on_what = [things['a7str']]
                else:
                    on_what = things['on_what'].split()
                yield "define", FunData(nick, things['comment'], things['how'], on_what)


class SyntErr:
    "handle syntactic errors in the script - VERY PRIMITIVE for the time being"

    def __init__(self):
        from sys import stderr
        self.e = stderr

    def report(self, nonfatal = False, info = ''):
        "return value to be given to the valid field / alt: fatal here and nonvalid at script"
        p = 'Nonf' if nonfatal else 'F'
        print(p + 'atal error in PReFScript:', info, sep = '\n  ', file = self.e)
        return nonfatal



class PReFScript:

    def __init__(self, store_goedel_numbers = ""):
        '''
        Dicts for storing the functions:
          main for the function data,
          gnums for Gödel numbers,
          pycode for Python runnable code, 
          key is always nick for all of them;
        include here the basic functions;
        their implementation assumes 'import cantorpairs as cp'
        '''
        self.valid = True   # program is correct until proven wrong
        self.main = dict()  # RENAME some day, as I am using also 'main' for the main function to be called
        self.strcode = dict()
        self.pycode = dict()
        self.gnums = dict()
        self.abouts = list()
        self.pragmas = ddict(str)
        self.store_gnums = store_goedel_numbers 
        self.add_basic("k_1", "The constant 1 function", "lambda x: 1", 0)
        self.add_basic("id", "The identity function", "lambda x: x", 1)
        self.add_basic("s_tup", "Single-argument version of suffix tuple", 
                       "lambda x: cp.s_tup(cp.pr_L(x), cp.pr_R(x))", 2)
        self.add_basic("proj", "Single-argument version of projection", 
                       "lambda x: cp.pr(cp.pr_L(x), cp.pr_R(x))", 3)
        self.add_basic("add", "Addition x+y of the two components of input <x.y>", 
                       "lambda x: cp.pr_L(x) + cp.pr_R(x)", 4)
        self.add_basic("mul", "Multiplication x*y of the two components of input <x.y>", 
                       "lambda x: cp.pr_L(x) * cp.pr_R(x)", 5)
        self.add_basic("diff", "Modified difference max(0, x-y) of the two components of input <x.y>", 
                       "lambda x: max(0, cp.pr_L(x) - cp.pr_R(x))", 6)
        self.parser = Parser()
        self.synt_err_handler = SyntErr()


    def add_basic(self, nick, comment, code, num):
        data = FunData()
        data["nick"] = nick
        data["comment"] = comment
        data["how_def"] = "basic"
        data["def_on"] = tuple()
        if self.store_gnums:
            self.gnums[nick] = cp.dp(0, num)
        self.main[nick] = data
        self.strcode[nick] = code
        self.pycode[nick] = eval(code, globals() | self.pycode)


    def list(self, what = None, w_code = 0):
        '''
        if what is None: list everything
        else: search for that what on the dicts
        w_code 0: no code, 1: how and on what, 2: strcode also
        Gödel number printed depending on self.store_gnums and how big it is
        '''
        def list_one(nick, w_code):
            print("\n" + str(self.main[nick]))
            if w_code:
                'print how it is defined'
                print(" " + self.main[nick].how_def())
            if w_code == 2:
                'print also the Python code in this case only'
                print(" " + self.strcode[nick])
            if self.store_gnums:
                if nick in self.gnums:
                    gnum = self.gnums[nick]
                    print(" Gödel number:", gnum,
                          "= <" + str(cp.pr_L(gnum)) + "." + str(cp.pr_R(gnum)) + ">")
                else:
                    self.valid &= self.synt_err_handler(fatal = False, info = "Gödel number too large, omitted.")

        if what is not None:
            list_one(what, w_code)
        else:
            for nick in self.main:
                list_one(nick, w_code)


    def define(self, new_funct):
        'here comes a new function to add to the collection'

        if (nick := new_funct['nick']) in self.main:
            'repeated nick, check for consistency'
            if (self.main[nick]["how_def"] != new_funct['how_def'] or
                self.main[nick]["def_on"] != new_funct['def_on']):
                    self.valid &= self.synt_err_handler.report(nonfatal = False, 
                        info = f"Repeated, inconsistent definitions for function '{nick}' found.")
        else:
            self.main[nick] = new_funct
            on_what = new_funct['def_on']

            if new_funct['how_def'] == "comp":
                self.strcode[nick] = "lambda x: " + on_what[0] + "(" + on_what[1] + "(x))"
                if self.store_gnums and on_what[0] in self.gnums and on_what[1] in self.gnums:
                    gnum = cp.dp(1, cp.dp(self.gnums[on_what[0]], self.gnums[on_what[1]]))
                    if gnum < LIMIT_GNUM:
                        self.gnums[nick] = gnum
                    else:
                        self.valid &= self.synt_err_handler.report(nonfatal = False, 
                            info = f"Gödel number for '{nick}' too large, omitted.")

            elif new_funct['how_def'] == "pair":
                self.strcode[nick] = "lambda x: cp.dp(" + on_what[0] + "(x), " + on_what[1] + "(x))"
                if self.store_gnums and on_what[0] in self.gnums and on_what[1] in self.gnums:
                    gnum = cp.dp(2, cp.dp(self.gnums[on_what[0]], self.gnums[on_what[1]]))
                    if gnum < LIMIT_GNUM:
                        self.gnums[nick] = gnum
                    else:
                        self.valid &= self.synt_err_handler.report(nonfatal = False, 
                            info = f"Gödel number for '{nick}' too large, omitted.")
    
            elif new_funct['how_def'] == "mu":
                self.strcode[nick] = "lambda x: mu(x, " + on_what[0] + ")"
                if self.store_gnums and on_what[0] in self.gnums:
                    gnum = cp.dp(3, self.gnums[on_what[0]])
                    if gnum < LIMIT_GNUM:
                        self.gnums[nick] = gnum
                    else:
                        self.valid &= self.synt_err_handler.report(nonfatal = False, 
                            info = f"Gödel number for '{nick}' too large, omitted.")

            elif new_funct['how_def'] == "compair":
                if not self.pragmas['extended']:
                    self.valid &= self.synt_err_handler.report(nonfatal = True, 
                                  info = "Use of compair requires '.pragma extended: True', changed.")
                self.pragmas['extended'] = 'True'
                self.strcode[nick] = "lambda x: " + on_what[0] + "( cp.dp(" + on_what[1] + "(x), " + on_what[2] + "(x)))"
                if (self.store_gnums and on_what[0] in self.gnums and 
                    on_what[1] in self.gnums and on_what[2] in self.gnums):
                    gnum = cp.dp(1, cp.dp(self.gnums[on_what[0]],
                           cp.dp(2, cp.dp(self.gnums[on_what[1]], self.gnums[on_what[2]]))))
                    if gnum < LIMIT_GNUM:
                        self.gnums[nick] = gnum
                    else:
                        self.valid &= self.synt_err_handler.report(nonfatal = False, 
                            info = f"Gödel number for '{nick}' too large, omitted.")

            elif new_funct['how_def'] == "primrec":
                if not self.pragmas['extended']:
                    self.valid &= self.synt_err_handler.report(nonfatal = True, 
                                  info = "Use of primrec requires '.pragma extended: True', changed.")
                self.pragmas['extended'] = 'True'
                self.strcode[nick] = "prim_rec(" + on_what[0] + ", " + on_what[1] + ", " + on_what[2] + ")"
                if (self.store_gnums and on_what[1] in self.gnums and on_what[2] in self.gnums):
                    gnum = cp.dp(4, cp.dp(int(on_what[0]),
                               cp.dp(self.gnums[on_what[1]], self.gnums[on_what[2]])))
                    if gnum < LIMIT_GNUM:
                        self.gnums[nick] = gnum
                    else:
                        self.valid &= self.synt_err_handler.report(nonfatal = False, 
                            info = f"Gödel number for '{nick}' too large, omitted.")

            else:
                "ascii_const, as no other 'how' captured by parser - kept out of the Goedel numbering for the time being"
                if not self.pragmas['extended']:
                    self.valid &= self.synt_err_handler.report(nonfatal = True, 
                                  info = "Use of ascii constants requires '.pragma extended: True', changed.")
                self.pragmas['extended'] = 'True'
                self.strcode[nick] = "lambda x: str2int( '" + on_what[0] + "' )"

            self.pycode[nick] = eval(self.strcode[nick], globals() | self.pycode)


    def to_python(self, what):
        'returns the Python-runnable version of the function'
        if what not in self.pycode:
            self.valid &= self.synt_err_handler.report(nonfatal = False, 
                info = f"No Python code for function '{what}' found.")
            return None
        return self.pycode[what]


    def find_script_in_file(self, filename, main):
        try:
            with open(filename) as infile:
                 return infile.read()
        except IOError:
            if main:
                self.valid &= self.synt_err_handler.report(nonfatal = False, 
                              info = f"Script {filename} not found.")
            else:
                self.valid &= self.synt_err_handler.report(nonfatal = True, 
                              info = f"Imported script {filename} not found.")


    def load(self, filename, main = True):
        'load in definitions from .prfs file(s) - use .import to recurse into further loading'
        if filename.endswith('.prfs'):
            self.valid &= self.synt_err_handler.report(nonfatal = True, 
                          info = f"File name {filename} NOT expected to include the '.prfs' extension.")
        else:
            filename += '.prfs'
        script = self.find_script_in_file(filename, main)
        if not script:
            return None
        lastread = None
        for label, what in self.parser.parse(script):
            'make the FunData or store the about or the pragma or the import'
            if label == 'pragma':
                if main:
                    "pragmas in main file are stored"
                    self.pragmas[what[0]] = what[1]
                elif what[0] == 'extended' and what[1] == 'True':
                    "pragmas in imported files are ignored except extended when set to True"
                    if self.pragmas['extended'] != 'True':
                        self.valid &= self.synt_err_handler.report(nonfatal = True, 
                            info = f"Warning: the .pragma extended declaration found in {filename} affects globally.")
                    self.pragmas[what[0]] = what[1]
            if label == 'about':
                self.abouts.append('about ' + filename + ': ' + what) 
            if label == 'define':
                self.define(what)
                lastread = what['nick'] # nickname of the last function defined, used for default main
            if label == "import":
                "non-main recursive call"
                self.load(what, main = False)
        if main and not self.pragmas['main']:
            self.valid &= self.synt_err_handler.report(nonfatal = True, 
                 info = f"No main .pragma found in '{filename}'.")
            if self.valid and lastread:
                "warn that main assumed is lastread"
                self.valid &= self.synt_err_handler.report(nonfatal = True, 
                     info = f"Function '{lastread}' guessed to be the main function, cross fingers.")
                self.pragmas['main'] = lastread
            elif self.valid:
                self.valid &= self.synt_err_handler.report(nonfatal = False, 
                     info = f"No guess available for the main function.")


    def dialog(self):
        nick = input("Function name? ")
        comment = input("What is it? ")
        how = input("How is it made? [pair or comp or mu] ")
        on_what = input("Applied to what? [1 or 2 space-sep names] ")
        self.define(FunData(nick.strip(), comment.strip(), how.strip(), tuple(on_what.split())))


    def check_names(self):
        "checks that all function names needed to run main have been defined"

        def check_name(self, name, need = 'pragma main'):
            if name not in checked:
                checked.add(name)
                if name in self.main:
                    if self.main[name]['how_def'] != "ascii_const":
                        for nname in self.main[name]['def_on']:
                            check_name(self, nname, f"'{name}'")
                else:
                    "newly found undefined name"
                    self.valid &= self.synt_err_handler.report(nonfatal = False, 
                        info = f"Function '{name}' not found but needed by {need}.")

        checked = set()
        check_name(self, self.pragmas['main'])


def run():
    'Stand-alone CLI command to be handled as entry point - no Goedel numbers stored; handle the filename as argument'
    from argparse import ArgumentParser
    from pytokr import pytokr
    read, loop = pytokr(iter = True)
    aparser = ArgumentParser(prog = 'prefscript',
              description = 'Partial Recursive Functions Scripting interpreter')
    aparser.add_argument('filename', help = 'script filename to be run, extension .prfs assumed')
    aparser.add_argument('-a', '--about', 
            help = "show contents of .about directives in file and .import'd files before running",
            action = "store_true")
    aparser.add_argument('-v', '--version', 
            action = "version", version = f'{__version__}')
    args = aparser.parse_args()
    f = PReFScript()
    f.load(args.filename)
    if f.valid:
        f.check_names()
    if f.valid:
        'run it on data from stdin according to input/output/main pragmas'
        if args.about:
            print('\n'.join(f.abouts))

        r = f.to_python(f.pragmas["main"])

        if f.pragmas["output"] in ('', "int"):
            post = lambda x: x
        elif f.pragmas["output"] == "ascii":
            post = int2str
        elif f.pragmas["output"] == "bool":
            post = bool

        if f.pragmas["input"] in ('', "int"):
            arg = int(input()) 
        elif f.pragmas["input"] == "none":
            arg = 666 # for one
        elif f.pragmas["input"] == "intseq":
            arg = cp.tup_i(map(int, loop()))

    if f.valid:
        print(post(r(arg)))


if __name__ == "__main__":
    run()
