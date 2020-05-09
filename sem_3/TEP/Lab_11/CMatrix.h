#pragma once

#include <vector>
#include "CTable.h"
#include "CRandom.h"

class CMatrix
{
public:
	CMatrix() { i_rows = 0; i_cols = 0; }
	CMatrix(int iRows, int iCols) { vResize(iRows, iCols); }
	
	void vResize(int iRows, int iCols);	
	void vFill(double dValue);
	void vPrint();
	
	double dGet(int iRow, int iCol) { return cmatrix[iRow * i_cols + iCol]; }
	void vSet(double dValue, int iRow, int iCol);
	bool checkRowsAndColumns(int i, int j) { return !(i > i_rows || j > i_cols); }

	double rowSum(int iRow);
	double colSum(int iCol);

	int iGetCols() { return i_cols; }
	int iGetRows() { return i_rows; }
	int iGetSize() { return i_size; }

	void randomizeInMatrix(CRandom& crandom, double dMin, double dMax);

private:
	int i_rows;
	int i_cols;
	int i_size;
	CTable cmatrix;
};