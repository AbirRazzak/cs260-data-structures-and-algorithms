from lcrstree import *
import time
import loctree


def preorder(n):
    # print(n.value)  # Access root value
    c = n.LeftMostChild
    if c is None:
        return

    # Traverse subtree 1
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


def test_lcrs():
    # Create tree with height 3
    r = Node(1)
    t1 = Tree(r)
    create_degree_3(r)
    root = r.LeftMostChild
    create_degree_3(root)
    root = root.RightSibling
    create_degree_3(root)
    root = root.RightSibling
    create_degree_3(root)

    # Run timing tests
    start = time.time()
    preorder(r)
    end = time.time()
    print("LCRSTREE Pre-Order Traversal Height 3:   Took {0} seconds to complete.".format(end - start))

    start = time.time()
    postorder(r)
    end = time.time()
    print("LCRSTREE Post-Order Traversal Height 3:  Took {0} seconds to complete.".format(end - start))

    # Making tree height of 4
    root = root.parent
    root = root.LeftMostChild
    root = root.LeftMostChild
    while root is not None:
        create_degree_3(root)
        root = root.RightSibling

    # Run timing tests
    start = time.time()
    preorder(r)
    end = time.time()
    print("LCRSTREE Pre-Order Traversal Height 4:   Took {0} seconds to complete.".format(end - start))

    start = time.time()
    postorder(r)
    end = time.time()
    print("LCRSTREE Post-Order Traversal Height 4:  Took {0} seconds to complete.".format(end - start))


def preorder_loc(n):
    #print(n.value)

    if len(n.children) == 0:
        return

    # Traverse subtree 1
    preorder_loc(n.children[0])

    # Traverse subtree 2
    preorder_loc(n.children[1])

    # Traverse subtree 3
    preorder_loc(n.children[2])


def postorder_loc(n):
    if len(n.children) == 0:
        #print(n.value)  # Nothing underneath, return root value
        return

    # Traverse subtree 3
    postorder_loc(n.children[2])

    # Traverse subtree 2
    postorder_loc(n.children[1])

    # Traverse subtree 1
    postorder_loc(n.children[0])

    # Access root value
    #print(n.value)

def test_loc():
    # Create a tree of height 3
    r = loctree.Node(1)
    t2 = loctree.Tree(r)
    for i in range(0, 3):
        r.add(loctree.Node(i, r))

    for i in range(0, 3):
        s = r.children[i]
        for j in range(0, 3):
            s.add(loctree.Node(j, s))

    # Run timing tests
    start = time.time()
    preorder_loc(r)
    end = time.time()
    print("LOCTREE Pre-Order Traversal Height 3:    Took {0} seconds to complete.".format(end - start))

    start = time.time()
    postorder_loc(r)
    end = time.time()
    print("LOCTREE Post-Order Traversal Height 3:   Took {0} seconds to complete.".format(end - start))

    # Make tree height 4
    for z in range(0, 3):
        p = r.children[z]
        for i in range(0, 3):
            s = p.children[i]
            for j in range(0, 3):
                s.add(loctree.Node(j, s))

    # Run timing tests
    # Run timing tests
    start = time.time()
    preorder_loc(r)
    end = time.time()
    print("LOCTREE Pre-Order Traversal Height 4:    Took {0} seconds to complete.".format(end - start))

    start = time.time()
    postorder_loc(r)
    end = time.time()
    print("LOCTREE Post-Order Traversal Height 4:   Took {0} seconds to complete.".format(end - start))


if __name__ == '__main__':
    test_lcrs()
    test_loc()
