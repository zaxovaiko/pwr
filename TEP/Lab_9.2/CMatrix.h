#pragma once
#include "CTable.h"
#include "CRandom.h"

class CMatrix
{
public:
	CMatrix(int iRows, int iCols);

	void vPrint();
	void resize(int iNewRow, int iNewCol);
	void set(int iRow, int iCol, double dValue) { cmatrix[iRow * i_rows + iCol] = dValue; }
	
	double get(int iRow, int iCol) { return cmatrix[iRow * i_rows + iCol]; }
	double dSumRow(int iRow);
	double dSumCol(int iCol);

	int iGetSize() { return i_size; }
	int iGetRows() { return i_rows; }
	int iGetCols() { return i_cols; }
	void randomize(CRandom & random, double min, double max);

private:
	int i_rows;
	int i_cols;
	int i_size;

	CTable cmatrix = CTable(0);
};