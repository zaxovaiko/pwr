#include "CMatrix.h"

using std::cout;
using std::endl;

void CMatrix::vResize(int iRows, int iCols)
{
	i_rows = iRows;
	i_cols = iCols;
	i_size = iRows * iCols;
	cmatrix.vSetSize(i_size);
}

void CMatrix::vFill(double dValue)
{
	for (int i = 0; i < i_size; i++) 
		cmatrix[i] = dValue;
}

void CMatrix::vSet(double dValue, int iRow, int iCol)
{
	if (iRow * iCol > i_size || iRow > i_rows || iCol > i_cols) 
		return;
	cmatrix[iRow * i_cols + iCol] = dValue;
}

void CMatrix::vPrint()
{
	for (int i = 0; i < i_rows; i++)
		for (int j = 0; j < i_cols; j++) 
			cout << dGet(i, j) << " ";
		cout << endl;
}

double CMatrix::rowSum(int iRow)
{
	double sum = 0;
	for (int j = 0; j < i_cols; ++j) 
		sum += dGet(iRow, j);
	return sum;
}

double CMatrix::colSum(int iCol)
{
	double sum = 0;
	for (int i = 0; i < i_cols; ++i) 
		sum += dGet(i, iCol);
	return sum;
}

void CMatrix::randomizeInMatrix(CRandom & crandom, double dMin, double dMax)
{
	for (int i = 0; i < i_rows; i++)
		for (int j = 0; j < i_cols; j++)
			vSet(crandom.dRand(dMin, dMax), i, j);
}