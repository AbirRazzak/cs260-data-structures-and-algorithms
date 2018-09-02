#include <iostream>
#include <assert.h>
using namespace std;

struct celltype{
    int element;
    celltype* next;
};

struct Dictionary{
    celltype* arr[10];
};

//hash function - just a simple mod hash
int h(int x){
    return x%10;
}

//sets given hasht able to be an empty table
void MAKENULL(Dictionary* A){
    for(int i = 0; i < 10; i++){
        A->arr[i] = 0;
    }
}

//checks if given number is in hash table
bool MEMBER(int x, Dictionary A){
    int hash = h(x);
    
    if(A.arr[hash]){
      celltype* current = A.arr[hash];
        while(current){
            if(current->element == x){
              return true;
            }
          current = current->next;
        }
      }
    
    return false;
}

//Finds and deletes the given number from the has table
void DELETE(int x, Dictionary* A){
    int bucket = h(x);
    //check that bucket has values
    if(A->arr[bucket]){
        if(A->arr[bucket]->element == x){
           A->arr[bucket] = A->arr[bucket]->next;
        }
        else{
            //loops through nodes in the bucket to find x
            celltype* current = A->arr[bucket];
            while(current->next){
                if(current->next->element == x){
                current->next = current->next->next;
                return;
                }
                else
                current = current->next;
            }
        }
    }
}

//Inserts given number into the hash table in the appropriate bucket
int INSERT(int x, Dictionary* A){
    if(!MEMBER(x,*A)){
       int bucket = h(x);
       celltype* oldheader = A->arr[bucket];
       celltype* newCell = new celltype;
       newCell->element = x;
       newCell->next = oldheader;
       A->arr[bucket]=newCell;
    }
}

int main(){
    Dictionary A;
    MAKENULL(&A);

    INSERT(5, &A);
    //test to see if member works correctly for numbers not in table
    assert(!MEMBER(15,A));
    //test to see if member works after adding a number to hash table
    INSERT(15, &A);
    assert(MEMBER(15,A));

    //test for delete function
    DELETE(15, &A);
    assert(!MEMBER(15,A));

    cout << "All test passed for open hash table!\n";
    return 0;
}