#!/usr/bin/env python3


import time
from pointerlist import *
from pointerstack import *

print("Starting time inserting 2000 numbers in a POINTER LIST")
L = PointerList()
start = time.time()
for x in range(2000):
    L.INSERT(x, x)
end = time.time()
print("Process took {0} seconds to run.\n\n".format(end - start))
#L.display()

print("STARTING TIME INSERTING 2000 NUMBERS IN A POINTER STACK")
S = PointerStack()
start2 = time.time()
for x in range(2000):
    S.PUSH(x)
end2 = time.time()
print("Process took {0} seconds to run.\n\n".format(end2 - start2))
#S.display()

print("STARTING TIME POPPING 2000 NUMBERS IN A POINTER STACK")
S = PointerStack()
start3 = time.time()
for x in range(2000):
    S.POP()
end3 = time.time()
print("Process took {0} seconds to run.\n\n".format(end3 - start3))
S.display()

