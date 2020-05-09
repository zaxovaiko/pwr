#pragma once
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include "CSolution.h"
#include "CMatrix.h"
#include "CRandom.h"
#include "CProblem.h"

using std::fstream;
using std::vector;

class CMscnProblem : public CProblem
{
public:
	CMscnProblem();

	void setD(int n);
	void setF(int n);
	void setM(int n);
	void setS(int n);

	void setCD(double v, int i, int j);
	void setCF(double v, int i, int j);
	void setCM(double v, int i, int j);
	void setMINXD(double v, int i, int j);
	void setMAXXD(double v, int i, int j);
	void setMINXF(double v, int i, int j);
	void setMAXXF(double v, int i, int j);
	void setMINXM(double v, int i, int j);
	void setMAXXM(double v, int i, int j);

	void setSD(double v, int i);
	void setSF(double v, int i);
	void setSM(double v, int i);
	void setSS(double v, int i);
	void setUD(double v, int i);
	void setUF(double v, int i);
	void setUM(double v, int i);
	void setPS(double v, int i);

	bool isMINMAXCorrect(CSolution& csolution);

	void vReadFile(const char * filename);
	void vSaveFile(const char* fielname);
	
	double getQuality(CSolution& csolution, int* err);
	double getQuality(double* pdSolution, int* err);
	double getQualityIfNotGoodImprove(CSolution& csolution);

	bool constrainedSatisfied(CSolution& csolution, int* err);
	bool constrainedSatisfied(double* pdSolution, int* err);

	void debuggingPrint();

	int errorCheck(CSolution& csolution);

	void generateInstances(int iSeed);
	double* randomizeSolution(CRandom& rand);

	int iSolutionSize() { return d * f + f * m + s * m; }
	void fixSolutionTable(double* pdSolution, int length);

private:
	int d;
	int f;
	int m;
	int s;

	CMatrix cd;
	CMatrix cf;
	CMatrix cm;

	CTable sd;
	CTable sf;
	CTable sm;
	CTable ss;
	CTable ud;
	CTable uf;
	CTable um;
	CTable ps;

	CMatrix xdMin;
	CMatrix xdMax;
	CMatrix xfMin;
	CMatrix xfMax;
	CMatrix xmMin;
	CMatrix xmMax;

	void vSaveTableFile(fstream& fs, CTable& table);
	void vSaveMatrixFile(fstream& fs, CMatrix& matrix);
	void vSaveMatrixMINMAXFile(fstream& fs, CMatrix& min, CMatrix& max);

	void vReadTable(fstream& fs, CTable& table);
	void vReadMatrix(fstream& fs, CMatrix& matrix, int rows, int columns);
	void vReadMINMAX(fstream& fs, CMatrix& min, CMatrix& max, int rows, int columns);

	double calculateZ(CSolution& solution);
	double calculateKT(CSolution& solution);
	double calculateKU(CSolution& solution);
	double calculateP(CSolution& solution);

	void vSetMatrix(CMatrix& mat, double v, int i, int j);
	void vSetTable(CTable &vec, double v, int i);
	void vSetVector(vector<double> &vec, double v, int i) { vec[i] = v; }

	void fixRow(CMatrix& cmatrix, int iRow);
};