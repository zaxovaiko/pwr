#pragma once

#define DEFAULT_SIZE 5

#include <iostream>
#include "CRandom.h"

using std::string;

class CTable
{
public:
	CTable();
	CTable(int iSize);
	CTable(const CTable & cOther);
	CTable(CTable && cOther);
	~CTable() { delete[] pd_table; };

	void vSetSize(int iSize);
	void vPrint();
	void vCopy(const CTable & cOther);

	CTable& operator=(const CTable & cOther);
	double &operator[] (int i);
	
	int iGetSize() { return i_size; }
	void randomizeInTable(CRandom& crandom, double dMin, double dMax);

private:
	int i_size;
	double* pd_table;
};