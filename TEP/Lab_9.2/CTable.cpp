#include <iostream>
#include <algorithm>
#include "CTable.h"

CTable::CTable(int iSize)
{
	i_size = iSize;
	pd_table = new double[i_size];
}

void CTable::vSetNewSize(int iSize)
{
	double * pd_table_copy = new double[iSize];
	for (int i = 0; i < std::min(i_size, iSize); i++)
		pd_table_copy[i] = pd_table[i];

	delete[] pd_table;

	pd_table = pd_table_copy;
	i_size = iSize;
}

void CTable::vPrint()
{
	for (int i = 0; i < i_size; i++)
		std::cout << pd_table[i] << " ";
	std::cout << std::endl;
}

void CTable::randomize(CRandom & random, double min, double max)
{
	for (int i = 0; i < i_size; i++)
		this[i] = random.d_rand(min, max);
}
