#include <iostream>
#include <stdio.h>

#include "arraystack.h"

ArrayStack::ArrayStack()
{
   top = 0;
   *data = 0;   
}

// TOP - Gets the top value of the Stack
// param s - Stack of which to return top value of
// return int - Returns the integer value of the top of Stack
int TOP(ArrayStack s)
{
   return s.top;
}

// POP - Deletes the Top value of the stack
// param s - Stack in which we are popping
void POP(ArrayStack s)
{
   int size = 5000;
   for(int i = size - 1; i > -1; i--)
   {
      if(s.data[i])
      {
         s.data[i] = 0; // Delete top of stack
         s.top = s.data[i-1]; // Reassign Top value
         return;
      }
   }
}

// PUSH - Adds a number to the top of the Stack
// param x - Integer of which we are inserting
// param s - Stack in which is being inserted into
void PUSH(int x, ArrayStack s)
{
   int size = 5000;
   for(int i = 0; i < size; i++)
   {
      if(!s.data[i])
      {
         s.data[i] = x;
         s.top = x;
         return;
      }
   }

   // If you ever run out of room to push...
   std::cout << "Whoops, no more room left in the stack... :(\n";
}

// EMPTY - Determines if the Stack is empty
// param s - Stack in which we are evaluating
// return bool - True if Stack is empty, False if Stack is populated
bool EMPTY(ArrayStack s)
{
   return (s.data[0]);
}

// MAKENULL - Clears out the Stack
// param s - Stack to be cleared out
void MAKENULL(ArrayStack s)
{
   std::fill_n(s.data, 5000, 0);
}
