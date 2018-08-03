#ifndef POINTERLIST_H
#define POINTERLIST_H

class PointerList
{
   private:
   public:
      PointerList();
      struct ListNode
      {
         int value;
         ListNode* next;
      };
      ListNode *head;
};

int FIRST(PointerList L);
int END(PointerList L);
int RETRIEVE(int n, PointerList L);
int LOCATE(int x, PointerList L);
int NEXT(int p, PointerList L);
int PREVIOUS(int p, PointerList L);
void INSERT(int x, int p, PointerList L);
void DELETE(int p, PointerList L);
void MAKENULL(PointerList L);

#endif
