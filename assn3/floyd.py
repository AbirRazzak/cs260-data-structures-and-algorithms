#!/usr/bin/env python3


def shortest(A, C, P):
    """
    shortest takes an n X n matrix C of arc costs and produces an
    n X n matrix A of lengths of shortest paths and an n X n matrix
    P giving a point in the "middle" of each shortest path
    """
    n = len(A)

    for i in range(n):
        for j in range(n):
            A[i][j] = C[i][j]
            P[i][j] = 0

    for i in range(n):
        A[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (A[i][k] + A[k][j]) < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    P[i][j] = k


def path(i, j, P):
    """
    Prints shortest path between nodes
    :param i: vertex
    :param j: vertex
    :param P: matrix of paths from shortest
    """
    k = P[i][j]
    if k == 0:
        return
    path(i, k, P)
    print(k)
    path(k, j, P)


if __name__ == "__main__":
    """
    Test Code
    """
    C = [[0 for x in range(6)] for x in range(6)]

    C[0][1] = 4
    C[0][2] = 1
    C[0][3] = 5
    C[0][4] = 8
    C[0][5] = 10
    C[2][1] = 2
    C[3][4] = 2
    C[4][5] = 1

    A = [[0 for x in range(6)] for x in range(6)]
    P = [[0 for x in range(6)] for x in range(6)]

    print("\n-------- Floyd Testing --------")
    print("\nMatrix C")
    for x in C:
        print(x)
    print("\nRunning shortest(A, C, P)")
    shortest(A, C, P)

    print("\nMatrix A")
    for x in A:
        print(x)

    print("\nMatrix P")
    for x in P:
        print(x)

    print("\nPaths:")
    print("1->2")
    path(0, 1, P)
    print("1->3")
    path(0, 2, P)
    print("1->4")
    path(0, 3, P)
    print("1->5")
    path(0, 4, P)
    print("1->6")
    path(0, 5, P)

    print("\n-------- Complete --------")
