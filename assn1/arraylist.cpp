#include <iostream>
#include <stdio.h>

#include "arraylist.h"

//using namespace std;

ArrayList::ArrayList()
{
	size = 5000;
	*data = 0;
}

int FIRST(ArrayList L)
{
	int current = 0;

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

int END(ArrayList L)
{
	int current = L.size - 1;

	while(current >= 0)
	{
		if(L.data[current])
		{
			// Return the position of the last assigned value in data[] + 1
			return current + 1;
		}
		current = current - 1;
	}

	// If no values are assigned in data, return -1
	return -1;
}

int RETRIEVE(int n, ArrayList L)
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

int LOCATE(int x, ArrayList L)
{
	int current = FIRST(L);
	int end = END(L);

	while(current < end)
	{
		if(L.data[current] == x)
		{
			return current;
		}

		current = current + 1;
	}

	// If no values are x in data, return -1
	return -1;
}

int NEXT(int p, ArrayList L)
{
	int end = END(L);
	if(p == end - 1) return end; // If p is end - 1 then return end
	if(p == end) return -1; // If p is end the return undefined
	for(int i = p + 1; i < end; i++)
	{
		if(L.data[i])
		{
			return i;
		}
	}

	return -1; // If somehow it gets here
}

int PREVIOUS(int p, ArrayList L)
{
	int first = FIRST(L);
	if(p == first) return -1;
	for(int i = p - 1; i >= first; i--)
	{
		if(L.data[i])
		{
			return i;
		}
	}

	return -1; // If somehow it gets here
}

void INSERT(int x, int p, ArrayList L)
{
	if(p > 0 && p < L.size)
	{
		/* If a number is already at position p, 
		move everything after p forward by 1 */
		if(L.data[p])
		{
			int end = END(L);
			for(int i = p + 1; i <= end; i++)
			{
				//Moves everything after p over by 1
				INSERT(RETRIEVE(i, L), i + 1, L);
			}
		}
		
		L.data[p] = x;
	}
}

void DELETE(int p, ArrayList L)
{
	if(L.data[p])
	{
		L.data[p] = 0;
	}
}

void MAKENULL(ArrayList L)
{
	int first = FIRST(L);
	int end = END(L);
	int counter = first;

	while(counter != end)
	{
		L.data[counter] = 0;
		counter = NEXT(counter, L);
	}
}
