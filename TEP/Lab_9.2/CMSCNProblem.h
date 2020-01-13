#pragma once
#include "CMatrix.h"
#include "CSolution.h"

class CMSCNProblem
{
public:
	CMSCNProblem();

	void setD(int iNum);
	void setF(int iNum);
	void setM(int iNum);
	void setS(int iNum);

	void setCD(double v, int i, int j) { cd.set(v, i, j); }
	void setCF(double v, int i, int j) { cf.set(v, i, j); }
	void setCM(double v, int i, int j) { cm.set(v, i, j); }
	void setMinXD(double v, int i, int j) { xdMin.set(v, i, j); }
	void setMaxXD(double v, int i, int j) { xdMax.set(v, i, j); }
	void setMinXF(double v, int i, int j) { xfMin.set(v, i, j); }
	void setMaxXF(double v, int i, int j) { xfMin.set(v, i, j); }
	void setMinXM(double v, int i, int j) { xmMin.set(v, i, j); }
	void setMaxXM(double v, int i, int j) { xmMin.set(v, i, j); }

	void setSD(double v, int i) { sd[i] = v; }
	void setSF(double v, int i) { sf[i] = v; }
	void setSM(double v, int i) { sm[i] = v; }
	void setSS(double v, int i) { ss[i] = v; }
	void setUD(double v, int i) { ud[i] = v; }
	void setUF(double v, int i) { uf[i] = v; }
	void setUM(double v, int i) { um[i] = v; }
	void setP(double v, int i)  { p[i]  = v; }

	void vReadFile(const char* fileName);
	void vReadTable(std::fstream & fs, CTable & ctable);
	void vReadMatrix(std::fstream & fs, CMatrix & cmatrix, int iRow, int iCol);
	void vReadMinMax(std::fstream & fs, CMatrix & cmin, CMatrix & cmax, int iRow, int iCol);

	double getQuality(CSolution & csolution, int* err);
	bool constrainedSatisfied(CSolution& csolution, int* err);

	int errorCheck(CSolution& sol) { return (sol.getXD().iGetSize() != d * f || sol.getXF().iGetSize() != f * m || sol.getXM().iGetSize() != m * s) ? 0 : -1; }
	void generateInstances(int iSeed);

private:
	int d;
	int f;
	int m;
	int s;

	CSolution solution;

	double calculateZ() { return calculateP() - calculateKU() - calculateKT(); }
	double calculateKT();
	double calculateKU();
	double calculateP();

	CMatrix cd = CMatrix(0, 0);
	CMatrix cf = CMatrix(0, 0);
	CMatrix cm = CMatrix(0, 0);

	CTable sd = CTable(0);
	CTable sf = CTable(0);
	CTable sm = CTable(0);
	CTable ss = CTable(0);
	CTable ud = CTable(0);
	CTable uf = CTable(0);
	CTable um = CTable(0);
	CTable p = CTable(0);

	CMatrix xdMin = CMatrix(0, 0);
	CMatrix xdMax = CMatrix(0, 0);
	CMatrix xfMin = CMatrix(0, 0);
	CMatrix xfMax = CMatrix(0, 0);
	CMatrix xmMin = CMatrix(0, 0);
	CMatrix xmMax = CMatrix(0, 0);
};