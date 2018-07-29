//#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <array>

//using namespace std;

struct ArrayList
{
	int size;
	int data[100];
};

int FIRST(ArrayList L)
{
	int current = 0;
	//int size = sizeof(L.data);

	while(current < L.size)
	{
		if(L.data[current])
		{
			// Return the position of the first assigned value in data[]
			return current;
		}
		current = current + 1;
	}

	// If no values are assigned in data, return -1
	return -1;
}

void END(ArrayList L)
{
	int current = L.size - 1;

	while(current <= 0)
	{
		if(L.data[current])
		{
			// Return the position of the last assigned value in data[]
			return current;
		}
		current = current - 1;
	}

	// If no values are assigned in data, return -1
	return -1;
}

void RETRIEVE(int n, ArrayList L)
{
	if(L.data[n])
	{
		// Return the value of the data at position n
		return L.data[n];
	}
	else
	{
		// Return -1 if there is no data at position n
		return -1;
	}
}

void LOCATE()
{

}

void NEXT()
{

}

void PREVIOUS()
{

}

void INSERT()
{

}

void DELETE()
{

}

void MAKENULL()
{

}

int main(int argc, char const *argv[])
{
	ArrayList x;
	x.size = 100;
	
	x.data[5] = 3;
	int first = FIRST(x);
	printf("%d\n", first);

	return 1;
}
