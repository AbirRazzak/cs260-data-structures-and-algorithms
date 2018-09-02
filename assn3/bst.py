#!/usr/bin/python3


from bst_adt import *


class Dictionary:

    def __init__(self):
        """
        defines a dictionary with no parameters
        has an attribute data that points to a BST
        """
        self.data = BinarySearchTree()

    def makenull(self):
        """
        makes the dictionary empty
        """
        self.data.root = None

    def insert(self, x):
        """
        inserts x into the dictionary
        :type x: int
        """
        if self.data.root is None:
            self.data.root = BSTNode(x)
        else:
            bst_insert(x, self.data.root)

    def delete(self, x):
        """
        deletes x from the dictionary
        :type x: int
        """
        bst_delete(x, self.data.root)

    def member(self, x):
        """
        determines if x is a member of the dictionary
        :type x: int
        """
        return bst_member(x, self.data.root)

    def printd(self):
        print_dict(self, self.data.root)


def print_dict(dictbst, curr):
    """
    helper function that prints out a BST Dictionary
    :param dictbst: Dictionary BST that needs to be printed out
    :type dictbst: Dictionary
    :param curr: Current BSTNode being looked at
    :type curr: BSTNode
    :return: String of contents
    """
    if curr is None or curr.element is None:
        return

    else:
        print(curr.element)

        if curr.left_child is not None:
            print_dict(dictbst, curr.left_child)

        if curr.right_child is not None:
            print_dict(dictbst, curr.right_child)


if __name__ == '__main__':
    print("-----Dictionary w/ Binary Search Tree Tests-----")

    d = Dictionary()

    print("Testing insert...")
    print("Inserting 2")
    print("Expecting: [2]")
    d.insert(2)
    d.printd()
    print("Inserting 5")
    print("Expecting: [2, 5]")
    d.insert(5)
    d.printd()
    print("Inserting 1")
    print("Expecting: [2, 1, 5]")
    d.insert(1)
    d.printd()
    print("Inserting 7")
    print("Expecting: [2, 1, 5, 7]")
    d.insert(7)
    d.printd()
    print("Inserting 1 (Should not change anything)")
    print("Expecting: [2, 1, 5, 7]")
    d.insert(1)
    d.printd()

    print("")
    print("")

    print("Testing member...")
    for i in range(9):
        if d.member(i):
            print(str(i) + " is in the Dictionary!")
        else:
            print(str(i) + " is NOT in the Dictionary.")

    print("")
    print("")

    print("Testing delete...")
    print("Deleting 5")
    print("Expecting: [2, 1, 7]")
    d.delete(5)
    d.printd()
    print("Deleting 3 (Deleting non-existent value)")
    print("Expecting: [2, 1, 7]")
    d.delete(3)
    d.printd()
    print("Deleting 2 (Deleting root)")
    print("Expecting: [7, 1]")
    d.delete(2)
    d.printd()

    print("")
    print("")

    print("Testing makenull...")
    print("Expecting: []")
    d.makenull()
    d.printd()
    print("(If nothing appears above this line, then makenull worked!)")

    print("-----Complete-----")
