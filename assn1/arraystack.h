#ifndef ARRAYSTACK_H
#define ARRAYSTACK_H

class ArrayStack
{
   private:
   public:
      int top;
      int data[5000];
      ArrayStack();
};

int TOP(ArrayStack s);
void POP(ArrayStack s);
void PUSH(int x, ArrayStack s);
bool EMPTY(ArrayStack s);
void MAKENULL(ArrayStack s);

#endif