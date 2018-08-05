#!/usr/bin/env python3

from pointerlist import *
from pointerstack import *

# Testing Lists
print("STARTING TESTS FOR STACK...\n")
L = PointerList()

L.INSERT(0, 4)
print("INSERT::Expected output: '4' ")
L.display()
print()

l = L.FIRST()
print("\nFIRST::Expected output: '0' ")
print("{0}".format(l))

l = L.NEXT(l)
L.INSERT(1, 2)
print("\nNEXT::Expected output: '1' ")
print("{0}".format(l))

l = L.END()
print("\nEND::Expected output: '2' ")
print("{0}".format(l))

L.INSERT(l, 6)
l = L.LOCATE(6)
print("\nLOCATE::Expected output: '2' ")
print("{0}".format(l))

r = L.RETRIEVE(l)
print("\nRETRIEVE::Expected output: '6' ")
print("{0}".format(r))

l = L.PREVIOUS(l)
print("\nPREVIOUS::Expected output: '1' ")
print("{0}".format(l))

L.INSERT(3, 5)
L.INSERT(4, 8)
#L.DELETE(1)
#print("\nDELETE::Expected output: '4 6' ")
#L.display()

L.MAKENULL()
print("\nMAKENULL::Expected output: 'None' ")
L.display()
print()

# Testing Stacks
print("\nSTARTING TESTS FOR STACK...\n")
S = PointerStack()

S.PUSH(4)
S.PUSH(7)
S.PUSH(8)
print("PUSH::Expected output: '8 7 4' ")
S.display()
print()

top = S.TOP()
print("\nTOP::Expected output: '8' ")
print("{0}".format(top))

S.POP()
print("\nPOP::Expected output: '7 4' ")
S.display()
print()

print("\nEMPTY::Expected output: 'FALSE' ")
if S.EMPTY() is False:
    print("FALSE")

S.MAKENULL()
print("\nMAKENULL::Expected output: 'TRUE' ")
if S.EMPTY() is True:
    print("TRUE")
