#include <iostream>
#include <set>
using namespace std;

//Dijsktra function to calculate shorted path to each node
void Dijkstra(int **C,int source,int n){
    //initializes set of unvisited nodes and array of shortest paths
    set<int> unvisited;
    int D[n] = {0};

    //inserts all nodes except start node to unvicisted
    for(int i = 0; i < n; i++){
        if(i != source-1){
            unvisited.insert(i);
            D[i] = C[source-1][i];
        }
    }
    for(int i = 0; i < n-1; i++){
        set<int>::iterator it = unvisited.begin();
        int w = *it;
        //finds the unvisited node that has the shortest path from start
        for(it; it!= unvisited.end(); ++it){
            if(D[w] > D[*it]){
                w = *it;
            }
        }
        unvisited.erase(w);

        //sets the shortest path if the current path to node is not the shortest
        for(it = unvisited.begin(); it != unvisited.end(); ++it){
            int v = *it;
            if(D[w] == -1){
            }
            else if(C[w][v] == -1){
            }
            else if(D[v] == -1){
                D[v] = D[w] + C[w][v];
            }
            else if(D[v] > D[w] + C[w][v]){
                D[v] = D[w] + C[w][v];
            }
        }

    }
    for(int i = 0; i < n; i++){
        cout << "D[" << i+1 << "]: " << D[i] << ", ";
    }
}

int main(){
    //creates 2D array to represent adjacency matrix
    int **A = {0};
    A = new int*[6];
    for(int i = 0; i < 6; i++)
        A[i] = new int[6]; 
    for(int i = 0; i < 6; i++){
        for(int j = 0; j < 6; j++){
            A[i][j] = -1;
        }
    }

    //creates graph from review 2 problem 6.
    A[0][1] = 4; A[0][2] = 1; A[0][3] = 5; A[0][4] = 8;
    A[0][5] = 10; A[2][1] = 2; A[3][4] = 2; A[4][5] = 1;
    A[0][0] = 0; A[1][1] = 0; A[2][2] = 0; A[3][3] = 0; A[4][4] = 0; A[5][5] = 0;

    cout << "Final values for array D: ";
    Dijkstra(A, 1, 6);
    return 0;
}