#!/usr/bin/python3

from loctree import *


def find_min(dict):
    k = next(iter(dict))  # Gets the first key in dict
    min = dict[k]  # Set the min to the first value of dict
    for key in dict:
        if dict[key] < min:
            k = key

    return k


def huffman(data):
    # Find the 2 lowest values in the dict
    min1_key = find_min(data)
    min1 = data[min1_key]
    del(data[min1_key])
    min2_key = find_min(data)
    min2 = data[min2_key]
    del(data[min2_key])

    total = min1 + min2
    r = Node(total)  # Make root equal to running total
    t = Tree(r)
    r.add(Node(min1_key, r))  # Make min1 the LeftMost Child
    r.add(Node(min2_key, r))  # Make min2 the Right Sibling of min1

    while len(data) != 0:
        # Get the lowest value in dict
        m_key = find_min(data)
        m = data[m_key]
        del(data[m_key])

        # Calculate the new total
        total = total + m

        # Replace current tree with a new one with new total as root
        # New min will be leftmost child and old tree is its sibling
        r = t.root()
        t.make_null()
        q = Node(total)
        t.set_root(q)
        q.add(Node(m_key, q))
        q.add(r)
        r.parent = q

    return t


def main():
    data = {
        "a": .07,
        "b": .09,
        "c": .12,
        "d": .22,
        "e": .23,
        "f": .27
    }
    tree = huffman(data)
    i = tree.root()
    print(i.value)
    while i is not None:
        if len(i.children) != 0:
            for child in i.children:
                print(child.value)
            i = i.children[1]


if __name__ == '__main__':
    main()