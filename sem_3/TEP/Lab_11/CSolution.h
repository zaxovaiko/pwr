#pragma once

#include <fstream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include "CMatrix.h"
#include "CTable.h"

using std::vector;
using std::string;
using std::istringstream;
using std::fstream;

class CSolution {
public:
	CSolution();
	CSolution(int d, int f, int m, int s);
	
	CMatrix& getXD() { return xd; }
	CMatrix& getXF() { return xf; }
	CMatrix& getXM() { return xm; }

	void setXD(double v, int i, int j);
	void setXF(double v, int i, int j);
	void setXM(double v, int i, int j);

	void vPrint() { xd.vPrint(); xm.vPrint(); xf.vPrint(); }
	void vReadFile(const char* filename);
	void vSaveFile(const char* filename);

	CSolution vReadDoubleTable(double* pdSolution, int d, int f, int s, int m);
	double* toDoubleTable();
	
private:
	void vSaveMatrixFile(fstream & fs, CMatrix & matrix);
	void vReadMatrixFile(fstream & fs, CMatrix & matrix, int rows, int columns);
	void vSetMatrix(CMatrix & mat, double value, int i, int j);

	int d;
	int f;
	int m;
	int s;

	CMatrix xd;
	CMatrix xf;
	CMatrix xm;
};