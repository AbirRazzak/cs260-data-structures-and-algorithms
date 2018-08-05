#include <iostream>

#include "pointerlist.h"

PointerList::PointerList()
{
   *head;
}

int FIRST(PointerList *L)
{
   if(L->head) return 0; // List starts at 0 always
   else return -1; // List is empty
}

int END(PointerList *L)
{
   if(!L->head) return -1; // List is empty
   
   int counter = 0;
   PointerList::ListNode *current = L->head;
   //while(current != NULL)
   while(!current)
   {
      current = current->next;
      counter++;
   }

   return counter;
}

int RETRIEVE(int p, PointerList *L)
{
   int counter = 0;
   PointerList::ListNode *current = L->head;
   //while(current != NULL)
   while(!current)
   {
      current = current->next;
      counter++;
      if(counter == p)
      {
         break;
      }
   }

   return current->value;
}

int LOCATE(int x, PointerList *L)
{
   int counter = 0;
   PointerList::ListNode *current = L->head;
   while(!current)
   {
      if(current->value == x) return counter;
      current = current->next;
      counter++;
   }
}

int NEXT(int p, PointerList *L)
{
   int counter = 0;
   PointerList::ListNode *current = L->head;
   // Trace through List and determine the node in the position p
   //while(current != NULL)
   while(!current)
   {
      current = current->next;
      counter++;
      if(counter == p)
      {
         break;
      }
   }

   return (counter + 1);
}

int PREVIOUS(int p, PointerList *L)
{
   int counter = 0;
   PointerList::ListNode *current = L->head;
   // Trace through List and determine the node in the position p
   //while(current != NULL)
   while(!current)
   {
      current = current->next;
      counter++;
      if(counter == p)
      {
         break;
      }
   }

   return (counter - 1);
}

void INSERT(int x, int p, PointerList *L)
{
   //Create a new ListNode
   PointerList::ListNode *n = new PointerList::ListNode;
   n->value = x;

   // If inserting ListNode in empty List
   if(!L->head)
   {
      L->head = n;
      //n->next == NULL;
      return;
   }
   else
   {
      int counter = 0;
      PointerList::ListNode *current = L->head;

      // Trace through List and determine the node in the position p
      //while(current != NULL)
      while(!current)
      {
         if(counter == p)
         {
            break;
         }
         else
         {
            current = current->next;
            counter++;
         }
      }

      // if given p is greater than size of list
      if(p > counter)
      {
         current->next = n; // then just put it in the end
         //n->next = NULL;
         return;
      }
      else // Inserting at a position where current node belongs
      {
         // Push down nodes and insert new node in between
         PointerList::ListNode *nxt = current->next;
         current->next = n;
         n->next = nxt;
      }
   }
}

void DELETE(int p, PointerList *L)
{
   int counter = 0;
   PointerList::ListNode *current = L->head;
   // Trace through List and determine the node in the position p
   //while(current != NULL)
   while(!current)
   {
      if(counter == p - 1) // stop at the node before p
      {
         PointerList::ListNode *after = current->next->next; // Determine what's after p (p+1)
         current->next = after; // Set next node of p-1 to p+1 (esentially deleting p) 
         return;
      }
      else
      {
         current = current->next;
         counter++;
      }
   }

   // Error occured, p was invalid
   std::cout << "Invalid p used.";
}

void MAKENULL(PointerList L);
