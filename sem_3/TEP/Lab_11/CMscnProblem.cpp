#include "CMscnProblem.h"
#include "CProblem.h"
#include "CSolution.h"
#include "CTable.h"
#include "CMatrix.h"
#include "CRandom.h"
#include "CProblem.h"

#define NUM_OF_D 2
#define NUM_OF_F 1
#define NUM_OF_M 3
#define NUM_OF_S 4

#define C_MIN 2
#define C_MAX 7
#define S_MIN 10
#define S_MAX 20
#define U_MIN 50
#define U_MAX 100
#define P_MIN 60
#define P_MAX 500

#define CORRECTION 0.5

using std::fstream;
using std::string;
using std::getline;
using std::cout;
using std::endl;
using std::vector;

CMscnProblem::CMscnProblem()
{
	d = NUM_OF_D;
	f = NUM_OF_F;
	m = NUM_OF_M;
	s = NUM_OF_S;

	cd = CMatrix(f, d);
	cf = CMatrix(m, f);
	cm = CMatrix(s, m);

	sd.vSetSize(d);
	ud.vSetSize(d);
	sf.vSetSize(f);
	uf.vSetSize(f);
	sm.vSetSize(m);
	um.vSetSize(m);
	ss.vSetSize(s);
	ps.vSetSize(s);
}

void CMscnProblem::setD(int n)
{
	d = n;
	cd.vResize(f, n);
	sd.vSetSize(n);
	ud.vSetSize(n);
}
void CMscnProblem::setF(int n)
{
	f = n;
	cd.vResize(f, d);
	cf.vResize(m, f);
	sf.vSetSize(f);
	uf.vSetSize(f);
}
void CMscnProblem::setM(int n)
{
	m = n;
	cf.vResize(m, f);
	cm.vResize(s, m);
	sm.vSetSize(m);
	um.vSetSize(m);
}
void CMscnProblem::setS(int n)
{
	s = n;
	cm.vResize(s, m);
	ss.vSetSize(s);
	ps.vSetSize(s);
}

void CMscnProblem::setCD(double v, int i, int j) { vSetMatrix(cd, v, i, j); }
void CMscnProblem::setCF(double v, int i, int j) { vSetMatrix(cf, v, i, j); }
void CMscnProblem::setCM(double v, int i, int j) { vSetMatrix(cm, v, i, j); }

void CMscnProblem::setMINXD(double v, int i, int j) { vSetMatrix(xdMin, v, i, j); }
void CMscnProblem::setMAXXD(double v, int i, int j) { vSetMatrix(xdMax, v, i, j); }
void CMscnProblem::setMINXF(double v, int i, int j) { vSetMatrix(xfMin, v, i, j); }
void CMscnProblem::setMAXXF(double v, int i, int j) { vSetMatrix(xfMax, v, i, j); }
void CMscnProblem::setMINXM(double v, int i, int j) { vSetMatrix(xmMin, v, i, j); }
void CMscnProblem::setMAXXM(double v, int i, int j) { vSetMatrix(xmMax, v, i, j); }

void CMscnProblem::setSD(double v, int i) { vSetTable(sd, v, i); }
void CMscnProblem::setSF(double v, int i) { vSetTable(sf, v, i); }
void CMscnProblem::setSM(double v, int i) { vSetTable(sm, v, i); }
void CMscnProblem::setSS(double v, int i) { vSetTable(ss, v, i); }
void CMscnProblem::setUD(double v, int i) { vSetTable(ud, v, i); }
void CMscnProblem::setUF(double v, int i) { vSetTable(uf, v, i); }
void CMscnProblem::setUM(double v, int i) { vSetTable(um, v, i); }
void CMscnProblem::setPS(double v, int i) { vSetTable(ps, v, i); }

void CMscnProblem::vReadFile(const char * filename)
{
	fstream file(filename);
	string tr;
	char temp;

	file >> temp; file >> d;
	file >> temp; file >> f;
	file >> temp; file >> m;
	file >> temp; file >> s;

	getline(file, tr);
	getline(file, tr); vReadTable(file, sd);
	getline(file, tr); vReadTable(file, sf);
	getline(file, tr); vReadTable(file, sm);
	getline(file, tr); vReadTable(file, ss);

	getline(file, tr); vReadMatrix(file, cd, d, f);
	getline(file, tr); vReadMatrix(file, cf, f, m);
	getline(file, tr); vReadMatrix(file, cm, m, s);

	getline(file, tr); vReadTable(file, ud);
	getline(file, tr); vReadTable(file, uf);
	getline(file, tr); vReadTable(file, um);
	getline(file, tr); vReadTable(file, ps);

	getline(file, tr); vReadMINMAX(file, xdMin, xdMax, d, f);
	getline(file, tr); vReadMINMAX(file, xfMin, xfMax, f, m);
	getline(file, tr); vReadMINMAX(file, xmMin, xmMax, m, s);
}

void CMscnProblem::vSaveFile(const char * filename)
{
	fstream file(filename);
	file.flush();

	file << "D "; file << d << endl;
	file << "F "; file << f << endl;
	file << "M "; file << m << endl;
	file << "S "; file << s << endl;

	file << "sd" << endl; vSaveTableFile(file, sd); file << endl;
	file << "sf" << endl; vSaveTableFile(file, sf); file << endl;
	file << "sm" << endl; vSaveTableFile(file, sm); file << endl;
	file << "ss" << endl; vSaveTableFile(file, ss); file << endl;

	file << "cd" << endl; vSaveMatrixFile(file, cd); file << endl;
	file << "cf" << endl; vSaveMatrixFile(file, cf); file << endl;
	file << "cm" << endl; vSaveMatrixFile(file, cm); file << endl;

	file << "ud" << endl; vSaveTableFile(file, ud); file << endl;
	file << "uf" << endl; vSaveTableFile(file, uf); file << endl;
	file << "um" << endl; vSaveTableFile(file, um); file << endl;

	file << "p" << endl; vSaveTableFile(file, ps); file << endl;

	file << "xdminmax" << endl; vSaveMatrixMINMAXFile(file, xdMin, xdMax); file << endl;
	file << "xfminmax" << endl; vSaveMatrixMINMAXFile(file, xfMin, xfMax); file << endl;
	file << "xmminmax" << endl; vSaveMatrixMINMAXFile(file, xmMin, xmMax); file << endl;

	file.close();
}

double CMscnProblem::getQuality(CSolution& solution, int * err)
{
	if (err != NULL)
	{
		*err = errorCheck(solution);
		if (*err != 0) return false;
	}
	return calculateZ(solution);
}

double CMscnProblem::getQuality(double * pdSolution, int * err)
{
	CSolution solution;
	solution = solution.vReadDoubleTable(pdSolution, d, f,s, m);
	return getQuality(solution, err);
}

double CMscnProblem::getQualityIfNotGoodImprove(CSolution & input_solution)
{
	for (int i = 0; i < d; i++)
		if (input_solution.getXD().rowSum(i) > sd[i])
			fixRow(input_solution.getXD(), i--);

	for (int i = 0; i < f; ++i)
		if (input_solution.getXF().rowSum(i) > sf[i])
			fixRow(input_solution.getXF(), i--);

	for (int i = 0; i < m; ++i)
		if (input_solution.getXM().rowSum(i) > sm[i])
			fixRow(input_solution.getXM(), i--);

	for (int i = 0; i < s; ++i)
		if (input_solution.getXM().colSum(i) > ss[i])
			fixRow(input_solution.getXM(), i--);

	for (int i = 0; i < f; ++i)
		if (input_solution.getXD().colSum(i) > input_solution.getXF().rowSum(i))
			fixRow(input_solution.getXF(), i--);

	for (int i = 0; i < m; ++i)
		if (input_solution.getXD().colSum(i) > input_solution.getXM().rowSum(i))
			fixRow(input_solution.getXF(), i--);

	if (!constrainedSatisfied(input_solution, NULL)) getQualityIfNotGoodImprove(input_solution);	
	return getQuality(input_solution, NULL);
}

void CMscnProblem::fixRow(CMatrix& mat, int row)
{
	for (int i = 0; i < mat.iGetCols(); i++)
	{
		mat.vSet(mat.dGet(row, i) - CORRECTION, row, i);
		if (mat.dGet(row, i) < 0)
			mat.vSet(0.1, row, i);
	}
}

bool CMscnProblem::constrainedSatisfied(CSolution& solution, int * err)
{
	if (err != NULL) {
		*err = errorCheck(solution);
		if (*err != 0)  return false;
	}

	for (int i = 0; i < d; i++) if (solution.getXD().rowSum(i) > sd[i]) return false;
	for (int i = 0; i < f; ++i) if (solution.getXF().rowSum(i) > sf[i] || solution.getXD().colSum(i) > solution.getXF().rowSum(i)) return false;
	for (int i = 0; i < m; ++i) if (solution.getXM().rowSum(i) > sm[i] || solution.getXD().colSum(i) > solution.getXM().rowSum(i)) return false;
	for (int i = 0; i < s; ++i) if (solution.getXM().colSum(i) > ss[i]) return false;
	return true;
}

bool CMscnProblem::constrainedSatisfied(double * pdSolution, int * err)
{
	CSolution solution;
	solution = solution.vReadDoubleTable(pdSolution, d, f, s, m);
	return constrainedSatisfied(solution, err);
}

double CMscnProblem::calculateZ(CSolution& solution)
{
	return calculateP(solution) - calculateKU(solution) - calculateKT(solution);
}

void CMscnProblem::debuggingPrint()
{
	cout << "D "; cout << d << endl;
	cout << "F "; cout << f << endl;
	cout << "M "; cout << m << endl;
	cout << "S "; cout << s << endl;

	cout << "cd" << endl; cd.vPrint();
	cout << "cf" << endl; cf.vPrint();
	cout << "cm" << endl; cm.vPrint();

	cout << "cd" << endl; sd.vPrint();
	cout << "sf" << endl; sf.vPrint();
	cout << "sm" << endl; sm.vPrint();
	cout << "ss" << endl; ss.vPrint();

	cout << "ud" << endl; ud.vPrint();
	cout << "uf" << endl; uf.vPrint();
	cout << "um" << endl; um.vPrint();
	cout << "ps" << endl; ps.vPrint();
}

int CMscnProblem::errorCheck(CSolution& csolution)
{
	return (csolution.getXD().iGetSize() != d * f || csolution.getXF().iGetSize() != f * m || csolution.getXM().iGetSize() != m * s) ? -1 : 0;
}

void CMscnProblem::generateInstances(int iInstanceSeed)
{
	CRandom random(iInstanceSeed);
	
	ud.randomizeInTable(random, U_MIN, U_MAX);
	uf.randomizeInTable(random, U_MIN, U_MAX);
	um.randomizeInTable(random, U_MIN, U_MAX);
	sd.randomizeInTable(random, S_MIN, S_MIN);
	sf.randomizeInTable(random, S_MIN, S_MIN);
	sm.randomizeInTable(random, S_MIN, S_MIN);
	ss.randomizeInTable(random, S_MIN, S_MIN);
	cd.randomizeInMatrix(random, C_MIN, C_MAX);
	cf.randomizeInMatrix(random, C_MIN, C_MAX);
	cm.randomizeInMatrix(random, C_MIN, C_MAX);
}

void CMscnProblem::fixSolutionTable(double * pdSolution, int iSize)
{
	int k = 0;
	for (int i = 0; i < d; i++)
		for (int j = 0; j < f; j++)
			if (pdSolution[k] > xdMax.dGet(i, j))
				pdSolution[k] = xdMax.dGet(i, j);

	for (int i = 0; i < f; i++)
		for (int j = 0; j < m; j++)
			if (pdSolution[k] > xfMax.dGet(i, j)) 
				pdSolution[k] = xfMax.dGet(i, j);

	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
			if (pdSolution[k] > xmMax.dGet(i, j)) 
				pdSolution[k] = xmMax.dGet(i, j);
}

void CMscnProblem::vSaveTableFile(fstream & fs, CTable & ctable)
{
	for (int i = 0; i < ctable.iGetSize(); i++) fs << ctable[i] << " ";
}

void CMscnProblem::vSaveMatrixFile(fstream & fs, CMatrix & cmatrix)
{
	for (int i = 0; i < cmatrix.iGetRows(); i++)
		for (int j = 0; j < cmatrix.iGetCols(); j++)
			fs << cmatrix.dGet(i, j) << " ";
}

void CMscnProblem::vSaveMatrixMINMAXFile(fstream & fs, CMatrix & cmin, CMatrix & cmax)
{
	for (int i = 0; i < cmin.iGetRows(); i++)
		for (int j = 0; j < cmin.iGetCols(); j++)
			fs << cmin.dGet(i, j) << " " << cmax.dGet(i, j);
}

void CMscnProblem::vReadTable(fstream & fs, CTable & ctable)
{
	vector<double> d_vector;
	string str;

	getline(fs, str);

	istringstream ss(str);
	double num;
	while (ss >> num)
		d_vector.push_back(num);

	ctable.vSetSize(d_vector.size());
	for (int i = 0; i < ctable.iGetSize(); i++)
		ctable[i] =  d_vector[i];
}

void CMscnProblem::vReadMatrix(fstream & fs, CMatrix & cmatrix, int iRows, int iCols)
{
	vector<double> d_vector;
	string str;

	getline(fs, str);

	istringstream ss(str);
	double num;
	while (ss >> num)
		d_vector.push_back(num);

	if (iCols * iRows != d_vector.size()) 
		return;

	cmatrix.vResize(iRows, iCols);
	int i_counter = 0;
	for (int i = 0; i < iRows; i++)
	{
		for (int j = 0; j < iCols; j++)
		{
			cmatrix.vSet(d_vector[i_counter], i, j);
			i_counter++;
		}
	}
}

void CMscnProblem::vReadMINMAX(fstream & fs, CMatrix & cmin, CMatrix & cmax, int iRows, int iCols)
{
	vector<double> vector;
	string str;

	getline(fs, str);

	istringstream ss(str);
	double num;
	while (ss >> num)
		vector.push_back(num);

	if (iCols * iRows * 2 != vector.size()) 
		return;

	cmin.vResize(iRows, iCols);
	cmax.vResize(iRows, iCols);

	int i_counter = 0;
	for (int i = 0; i < iRows; i++)
	{
		for (int j = 0; j < iCols; j++)
		{
			cmin.vSet(vector[i_counter], i, j);
			i_counter++;
			cmax.vSet(vector[i_counter], i, j);
		}
	}
}

double CMscnProblem::calculateKT(CSolution& solution)
{
	double sumD = 0;
	for (int i = 0; i < d; i++)
		for (int j = 0; j < f; j++)
			sumD += cd.dGet(i, j) * solution.getXD().dGet(j, i);

	double sumM = 0;
	for (int i = 0; i < f; i++)
		for (int j = 0; j < m; j++)
			sumM += cf.dGet(i, j) * solution.getXF().dGet(j, i);

	double sumS = 0;
	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
			sumS += cm.dGet(i, j) * solution.getXM().dGet(j, i);

	return sumD + sumM + sumS;
}

double CMscnProblem::calculateKU(CSolution& solution)
{
	double sumD = 0;
	for (int i = 0; i < d; i++)
		for (int j = 0; j < f; j++)
			if (solution.getXD().rowSum(j) > 0) sumD += ud[i];

	double sumM = 0;
	for (int i = 0; i < f; i++)
		for (int j = 0; j < m; j++)
			if (solution.getXF().rowSum(j) > 0) sumM += uf[i];

	double sumS = 0;
	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
			if (solution.getXM().rowSum(j) > 0) sumM += um[i];

	return sumD + sumM + sumS;
}

double CMscnProblem::calculateP(CSolution& solution)
{
	double sum = 0;
	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
			sum += ps[j] * solution.getXM().dGet(i, j);
	return sum;
}

void CMscnProblem::vSetMatrix(CMatrix &mat, double v, int i, int j)
{
	if (v < 0 || !mat.checkRowsAndColumns(i,j)) return;
	mat.vSet(v, i, j);
}

void CMscnProblem::vSetTable(CTable &table, double v, int i)
{
	if (v < 0 || table.iGetSize() < i) return;
	table[i] = v;
}

double* CMscnProblem::randomizeSolution(CRandom& rand)
{
	CSolution solution(d, f, m, s);

	for (int i = 0; i < solution.getXD().iGetRows(); i++)
		for (int j = 0; j < solution.getXD().iGetCols(); j++)
			solution.setXD(rand.dRand(xdMin.dGet(i,j), xdMax.dGet(i,j)), i, j);

	for (int i = 0; i < solution.getXF().iGetRows(); i++)
		for (int j = 0; j < solution.getXF().iGetCols(); j++)
			solution.setXF(rand.dRand(xfMin.dGet(i, j), xfMax.dGet(i, j)), i, j);

	for (int i = 0; i < solution.getXM().iGetRows(); i++)
		for (int j = 0; j < solution.getXM().iGetCols(); j++)
			solution.setXM(rand.dRand(xmMin.dGet(i, j), xmMax.dGet(i, j)), i, j);

	return solution.toDoubleTable();
}

bool CMscnProblem::isMINMAXCorrect(CSolution& solution)
{
	for(int i=0; i < d; i++)
		for (int j = 0; j < f; j++)
			if (!(xdMin.dGet(i, j) < solution.getXD().dGet(i, j) < xdMax.dGet(i, j)))
				return false;

	for (int i = 0; i < f; i++)
		for (int j = 0; j < m; j++)
			if (!(xfMin.dGet(i, j) < solution.getXF().dGet(i, j) < xfMax.dGet(i, j)))
				return false;

	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
			if (!(xmMin.dGet(i, j) < solution.getXM().dGet(i, j) < xmMax.dGet(i, j)))
				return false;

	return true;
}