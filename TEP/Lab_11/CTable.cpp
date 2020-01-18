#include "CTable.h"

using std::cout;
using std::endl;

CTable & CTable::operator=(const CTable & cOther)
{
	delete[] pd_table;
	pd_table = new double;
	vCopy(cOther);
	i_size = cOther.i_size;
	return *this;
}

double & CTable::operator[](int i)
{
	return pd_table[i];
}

void CTable::randomizeInTable(CRandom & crandom, double dMin, double dMax)
{
	for (int i = 0; i < i_size; i++)
		pd_table[i] = crandom.dRand(dMin, dMax);
}

void CTable::vPrint()
{
	if (pd_table == NULL) 
		return;
	for (int i = 0; i < i_size; i++)
		cout << pd_table[i] << endl;
}

void CTable::vCopy(const CTable & cOther)
{
	if (pd_table != NULL) 
		delete[] pd_table;
	pd_table = new double[cOther.i_size];
	i_size = cOther.i_size;
	for (int i = 0; i < cOther.i_size; i++) 
		pd_table[i] = cOther.pd_table[i];
}

CTable::CTable(const CTable & cOther)
{
	vCopy(cOther); 
	i_size = cOther.i_size;
}

CTable::CTable()
{
	pd_table = new double[DEFAULT_SIZE]; 
	i_size = DEFAULT_SIZE;
}

CTable::CTable(int iSize)
{
	pd_table = new double[iSize]; 
	i_size = iSize;
}

CTable::CTable(CTable && cOther)
{
	pd_table = cOther.pd_table;
	i_size = cOther.i_size;
	cOther.pd_table = NULL;
}

void CTable::vSetSize(int iSize)
{
	if (i_size == iSize || iSize < 0) 
		return;
	if (pd_table == NULL)
		pd_table = new double[iSize];

	double* temp = new double[iSize];
	for (int i = 0; i < iSize; i++) 
		if (i < i_size) 
			temp[i] = pd_table[i];
	delete[] pd_table;

	pd_table = temp;
	i_size = iSize;
}