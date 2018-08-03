#include "pointerlist.h"

PointerList::PointerList()
{

}

int FIRST(PointerList L);

int END(PointerList L);

int RETRIEVE(int n, PointerList L);
int LOCATE(int x, PointerList L);
int NEXT(int p, PointerList L);
int PREVIOUS(int p, PointerList L);

void INSERT(int x, int p, PointerList L)
{
   //Create a new ListNode
   PointerList::ListNode *n = new PointerList::ListNode;
   n->data = x;

   // If putting ListNode in empty List
   if(L->head == NULL)
   {
      L->head = n;
      n->NEXT == NULL;
      return;
   }

   
}

void DELETE(int p, PointerList L);
void MAKENULL(PointerList L);

