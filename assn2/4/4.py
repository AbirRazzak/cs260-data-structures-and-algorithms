#!/usr/bin/python3

from pointerlist import *

a = PointerList()
b = PointerList()

# a is sorted 0 to 9
for i in range(10):
    a.INSERT(i, i)

# b is sorted 4 to 11
for i in range(4, 12):
    b.INSERT(i - 4, i)

print("List a:")
a.display()
print("List b:")
b.display()

# I don't get why it matters if 2 lists are ordered or not
# Prompt doesn't mention anything about sorting the lists when merging...
print("Merging list b into list a...")
j = a.END()
i = b.FIRST()
end = b.END() - 1
while i != end:
    x = b.RETRIEVE(i)
    a.INSERT(j, x)
    j = j + 1
    i = i + 1

a.display()
