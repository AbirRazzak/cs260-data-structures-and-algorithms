#ifndef ARRAYLIST_H
#define ARRAYLIST_H

class ArrayList
{
	private:
	public:
		int size;
		int data[5000];
		ArrayList();
};

int FIRST(ArrayList L);
int END(ArrayList L);
int RETRIEVE(int n, ArrayList L);
int LOCATE(int x, ArrayList L);
int NEXT(int p, ArrayList L);
int PREVIOUS(int p, ArrayList L);
void INSERT(int x, int p, ArrayList L);
void DELETE(int p, ArrayList L);
void MAKENULL(ArrayList L);

#endif