#include <iostream>
#include "CMatrix.h"

CMatrix::CMatrix(int iRows, int iCols) 
{
	i_rows = iRows;
	i_cols = iCols;
	i_size = iRows * iCols;
	cmatrix.vSetNewSize(i_size);
}

void CMatrix::vPrint()
{
	for (int i = 0; i < i_rows; i++)
	{
		for (int j = 0; j < i_cols; j++)
			std::cout << cmatrix[i_rows * i + j] << " ";
		std::cout << std::endl;
	}
}

double CMatrix::dSumRow(int iRow)
{
	double sum = 0;
	for (int j = 0; j < i_cols; j++)
		sum += get(iRow, j);
	return sum;
}

double CMatrix::dSumCol(int iCol)
{
	double sum = 0;
	for (int j = 0; j < i_rows; j++)
		sum += get(j, iCol);
	return sum;
}

void CMatrix::randomize(CRandom & random, double min, double max)
{
	for (int i = 0; i < i_rows; i++)
		for (int j = 0; j < i_cols; j++)
			set(random.d_rand(min, max), i, j);
}

void CMatrix::resize(int iNewRow, int iNewCol)
{
	i_rows = iNewRow;
	i_cols = iNewCol;
	i_size = i_rows * i_cols;
	cmatrix.vSetNewSize(i_size);
}