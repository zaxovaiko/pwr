#pragma once
#include "CMatrix.h"

class CSolution
{
public:
	CSolution() {};

	int iGetD() { return d; }
	int iGetF() { return f; }
	int iGetM() { return m; }
	int iGetS() { return s; }

	CMatrix & getXD() { return xd; }
	CMatrix & getXF() { return xf; }
	CMatrix & getXM() { return xm; }

	void vReadFile(const char* fileName);
	void vReadMatrix(std::fstream & fs, CMatrix & cmatrix, int iRow, int iCol);
	void vPrint() { xd.vPrint(); xm.vPrint(); xf.vPrint(); }

private:
	int d = 0;
	int f = 0;
	int m = 0;
	int s = 0;

	CMatrix xd = CMatrix(0, 0);
	CMatrix xf = CMatrix(0, 0);
	CMatrix xm = CMatrix(0, 0);
};