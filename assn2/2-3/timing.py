from lcrstree import *
import time


def preorder(n):
    # print(n.value)

    # Traverse subtree 1
    c = n.LeftMostChild
    if c is None:
        return

    preorder(c)

    # Traverse subtree 2
    c = c.RightSibling
    preorder(c)

    # Traverse subtree 3
    c = c.RightSibling
    preorder(c)

def postorder(n):
    c1 = n.LeftMostChild
    if c1 is None:
        #print(n.value)  # Nothing underneath, return root value
        return

    c2 = c1.RightSibling
    c3 = c2.RightSibling

    # Traverse subtree 3
    postorder(c3)
    # Traverse subtree 2
    postorder(c2)
    # Traverse subtree 1
    postorder(c1)

    # Access root value
    #print(n.value)


def create_degree_3(r):
    i = r.value
    n = Node(i+1)
    r.LeftMostChild = n
    s1 = Node(i+2)
    n.RightSibling = s1
    s2 = Node(i+3)
    s1.RightSibling = s2
    n.parent = r
    s1.parent = r
    s2.parent = r


def main():
    # Create tree with height 3
    root = Node(1)
    t1 = Tree(root)
    create_degree_3(root)
    root = root.LeftMostChild
    create_degree_3(root)
    root = root.RightSibling
    create_degree_3(root)
    root = root.RightSibling
    create_degree_3(root)

    # Run timing tests
    root = t1.root()
    start = time.time()
    preorder(root)
    end = time.time()
    print("LCRSTREE Pre-Order Traversal Height 3: Took {0} seconds to complete.".format(end - start))

    root = t1.root()
    start = time.time()
    postorder(root)
    end = time.time()
    print("LCRSTREE Post-Order Traversal Height 3: Took {0} seconds to complete.".format(end - start))


if __name__ == '__main__':
    main()
