# ~ import scaff.cantorpairs as cp
# ~ from prefscript import PReFScript
from prefscript import PReFScript, cp
my_fs = PReFScript()
# ~ my_fs = PReFScript("Store Gödel numbers")
my_fs.load("script_sign.prfs")
my_fs.list(w_code = 1)
my_fs.load("script_proj.prfs")
my_fs.load("script_bool.prfs")
my_fs.load("script_compar.prfs")
my_fs.load("script_division.prfs")
my_fs.list()
d = my_fs.to_python("div")
print(d(cp.dp(14, 5)))
print(d(cp.dp(15, 5)))
my_fs.list("swap", w_code = 1)
my_fs.list("sign", w_code = 2)
