#!/usr/bin/python3


# Enums
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5


def dfs(graph, vertex, path):
    """
    performs Depth First Search on a given graph (2D array matrix)
    :param graph: 2D Array Matrix representing a directed graph
    :param vertex: Current vertex being computed for traversal
    :param path: Running path of search, required output for this problem
    :return: DFS seeking path
    """
    path += [vertex]

    for nxt in graph[vertex]:
        if nxt not in path:
            path = dfs(graph, nxt, path)

    return path


if __name__ == '__main__':
    # Setting up a matrix representative of the undirected graph, fig 6.38 from textbook
    Matrix = [[0 for x in range(6)] for x in range(6)]
    Matrix[A][B] = 3
    Matrix[A][D] = 4
    Matrix[A][F] = 5
    Matrix[B][C] = 1
    Matrix[B][F] = 1
    Matrix[C][D] = 2
    Matrix[D][B] = 3
    Matrix[E][D] = 3
    Matrix[E][F] = 2
    Matrix[F][D] = 2

    h = dfs(Matrix, 0, [])
    print("Depth First Search Result: ")
    print(h)





