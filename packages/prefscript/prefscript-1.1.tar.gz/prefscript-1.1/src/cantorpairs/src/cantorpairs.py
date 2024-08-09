'''
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528, april 2023 onwards 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Ancillary functions for PReFScript, the Partial Recursive Functions lab.

Implements a slight variant of Cantor's pair / unpair functions;
adapted from `https://en.wikipedia.org/wiki/Pairing_function`
The dotted pair is a bijection between `NxN` and `N-{0}`:
the natural number zero is used as "nil".

Project started: mid Germinal 2003.
Current version: 0.2, early Thermidor 2024.
Not pip-installable as of today. See README at `https://github.com/balqui/cantorpairs`

After each push, the following extra incantation is most likely 
necessary in the local copy of the git repo for `prefscript`:
`git submodule update --remote`
'''

from functools import cache
from math import isqrt

__version__ = "0.3"

@cache
def _isqrt(n):
	return isqrt(n)

# ~ def _isqrt(n):
    # ~ '''
    # ~ int square root via binary search, own program
    # ~ because math.sqrt fails with big numbers, e.g. the
    # ~ decoding of dp(10, 10^17) comes out wrong.
    # ~ '''
    # ~ def rr(n, k):
        # ~ """
        # ~ Pre: k <= sqrt(n)
        # ~ Post: a <= sqrt(n) < b and b - a = k
        # ~ """
        # ~ if 4*k*k > n:
            # ~ return k, 2*k
        # ~ a, b = rr(n, 2*k)
        # ~ m = (a + b)//2 # m = a + k
        # ~ if m*m <= n:
            # ~ return m, b
        # ~ else:
            # ~ return a, m
    # ~ assert n >= 0
    # ~ if n == 0:
        # ~ return 0
    # ~ return rr(n, 1)[0]

@cache
def _unpair(z):
    "local sq root instead of math.sqrt"
    assert z > 0
    w = (_isqrt(8*(z - 1) + 1) - 1)//2
    t = (w*w + w)//2
    x = z - 1 - t
    return x, w - x

@cache
def dp(x, y):
    return ((x + y)*(x + y + 1))//2 + x + 1

def pr_L(z):
    if z == 0:
        return 0
    return _unpair(z)[0]

def pr_R(z):
    if z == 0:
        return 0
    return _unpair(z)[1]

def tup_e(*nums):
    '''
    nums: arbitrary quantity of numbers to encode the sequence;
    fall back into the iterable version, the tuple cast will do nothing
    '''
    return tup_i(nums)

def tup_i(nums):
    '''
    nums expected to be an iterable here;
    the reversed nature of the encoding needs to 
    expand it into a sequence;
    end of sequence (= empty sequence) encoded 
    by 0 in its role of # nil, out of dotted pair range
    '''
    t = 0 
    for i in reversed(tuple(nums)):
        t = dp(i, t)
    return t

@cache
def s_tup(t, k):
    '''
    suffix tuple: t assumed a tuple of at least k components,
    return the suffix tuple from k-th on;
    t itself for k == 0, empty tuple 0 if k larger than len of t
    '''
    if t == 0:
        "empty tuple or original k too large"
        return 0
    if k == 0:
        "full suffix"
        return t
    return s_tup(pr_R(t), k-1)

def pr(t, k):
    '''
    projection function: get the k-th component;
    returns zero (meaning end of tuple) if k is too large
    '''
    return pr_L(s_tup(t, k))
