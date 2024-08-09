'''
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528, april 2023 onwards 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Ancillary functions for the Partial Recursive Functions lab.

Examples of usage of pairing and tupling.
'''

import cantorpairs as cp

for i in range(4):
  for j in range(4):
    print(i, j, cp.dp(i, j))

for i in range(90, 100):
  print(cp.pr_L(i), cp.pr_R(i), cp.dp(cp.pr_L(i), cp.pr_R(i)), i) 

t = cp.tup_e(4, 7, 56, 101)
for i in range(5):
    'last call is actually out of range'
    print(cp.pr(t, i))

st = cp.s_tup(t, 2)
print(st)
for i in range(3):
    print(cp.pr(st, i))

while t:
    print(t, cp.pr_L(t))
    t = cp.pr_R(t)

t = cp.tup_i(range(8, 16))
while t:
    print(t, cp.pr_L(t))
    t = cp.pr_R(t)


