#pragma once
#include "CRandom.h"

class CTable
{
public:
	CTable(int iSize);
	//~CTable() { delete[] pd_table; }

	void vSetNewSize(int iSize);
	void vPrint();

	int iGetSize() { return i_size; }
	double &operator[] (int index) { return pd_table[index]; }
	void randomize(CRandom & random, double min, double max);

private:
	double * pd_table;
	int i_size;
};