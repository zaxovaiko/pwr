#include "CMSCNProblem.h"
#include "CSolution.h"
#include "CRandom.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

#define NUMBER_OF_D 1
#define NUMBER_OF_F 2
#define NUMBER_OF_M 3
#define NUMBER_OF_S 5

#define U_MIN 0
#define U_MAX 100

#define S_MIN 100
#define S_MAX 100

#define C_MIN 100
#define C_MAX 100

CMSCNProblem::CMSCNProblem()
{
	d = NUMBER_OF_D;
	f = NUMBER_OF_F;
	m = NUMBER_OF_M;
	s = NUMBER_OF_S;

	cd.resize(f, d);
	cf.resize(m, f);
	cm.resize(s, m);

	sd.vSetNewSize(d);
	ud.vSetNewSize(d);
	sf.vSetNewSize(f);
	uf.vSetNewSize(f);
	sm.vSetNewSize(m);
	um.vSetNewSize(m);
	ss.vSetNewSize(s);
	p.vSetNewSize(s);
}

void CMSCNProblem::setD(int iNum)
{
	d = iNum;
	cd.resize(f, d);
	sd.vSetNewSize(d);
	ud.vSetNewSize(d);
}

void CMSCNProblem::setF(int iNum)
{
	f = iNum;
	cd.resize(f, d);
	cf.resize(m, f);
	sf.vSetNewSize(f);
	uf.vSetNewSize(f);
}

void CMSCNProblem::setM(int iNum)
{
	m = iNum;
	cf.resize(m, f);
	cm.resize(s, m);
	sm.vSetNewSize(m);
	um.vSetNewSize(m);
}

void CMSCNProblem::setS(int iNum)
{
	s = iNum;
	cm.resize(s, m);
	ss.vSetNewSize(s);
	p.vSetNewSize(s);
}

void CMSCNProblem::vReadTable(std::fstream & fs, CTable & ctable)
{
	std::vector<double> vector;
	std::string str;

	std::getline(fs, str);

	std::istringstream ss(str);
	double num;
	while (ss >> num)
		vector.push_back(num);

	ctable.vSetNewSize(vector.size());
	for (int i = 0; i < ctable.iGetSize(); i++)
		ctable[i] = vector[i];
}

void CMSCNProblem::vReadMatrix(std::fstream & fs, CMatrix & cmatrix, int iRow, int iCol)
{
	std::vector<double> vector;

	std::string str;

	std::getline(fs, str);

	std::istringstream ss(str);
	double num;
	while (ss >> num)
	{
		vector.push_back(num);
	}
	if (iRow * iCol != vector.size()) 
		return;

	cmatrix.resize(iRow, iCol);
	int helpVec = 0;


	for (int i = 0; i < iRow; i++)
		for (int j = 0; j < iCol; j++)
		{
			cmatrix.set(vector[helpVec], i, j);
			helpVec++;
		}
}

void CMSCNProblem::vReadMinMax(std::fstream & fs, CMatrix & cmin, CMatrix & cmax, int iRow, int iCol)
{
	std::vector<double> vector;
	std::string str;

	std::getline(fs, str);
	std::istringstream ss(str);

	double num;
	while (ss >> num)
		vector.push_back(num);

	if (iRow * iCol * 2 != vector.size()) 
		return;

	cmin.resize(iRow, iCol);
	cmax.resize(iRow, iCol);

	int helpVec = 0;

	for (int i = 0; i < iRow; i++)
	{
		for (int j = 0; j < iCol; j++)
		{
			cmin.set(vector[helpVec], i, j);
			helpVec++;
			cmax.set(vector[helpVec], i, j);
		}
	}
}

void CMSCNProblem::vReadFile(const char * fileName)
{
	std::fstream file(fileName);

	std::string trash;
	char t;

	file >> t; file >> d; // d
	file >> t; file >> f; // f
	file >> t; file >> m; // m
	file >> t; file >> s; // s

	std::getline(file, trash);
	std::getline(file, trash);

	vReadTable(file, sd);

	std::getline(file, trash);
	vReadTable(file, sf);

	std::getline(file, trash);
	vReadTable(file, sm);

	std::getline(file, trash);
	vReadTable(file, ss);

	std::getline(file, trash);
	vReadMatrix(file, cd, d, f);

	std::getline(file, trash);
	vReadMatrix(file, cf, f, m);

	std::getline(file, trash);
	vReadMatrix(file, cm, m, s);

	std::getline(file, trash);
	vReadTable(file, ud);

	std::getline(file, trash);
	vReadTable(file, uf);

	std::getline(file, trash);
	vReadTable(file, um);

	std::getline(file, trash);
	vReadTable(file, p);

	std::getline(file, trash);
	vReadMinMax(file, xdMin, xdMax, d, f);

	std::getline(file, trash);
	vReadMinMax(file, xfMin, xfMax, f, m);

	std::getline(file, trash);
	vReadMinMax(file, xmMin, xmMax, m, s);
}

double CMSCNProblem::getQuality(CSolution & csolution, int * err)
{
	if (err != NULL) {
		*err = errorCheck(csolution);
		if (*err != 0) 
			return false;
	}

	solution = csolution;
	return calculateZ();
}

bool CMSCNProblem::constrainedSatisfied(CSolution & csolution, int * err)
{
	if (err != NULL) {
		*err = errorCheck(csolution);
		if (*err != 0) return false;
	}

	solution = csolution;

	for (int i = 0; i < d; i++)
		if (solution.getXD().dSumRow(i) > sd[i]) 
			return false;

	for (int i = 0; i < f; ++i)
		if (solution.getXF().dSumRow(i) > sf[i] || solution.getXD().dSumCol(i) > solution.getXF().dSumRow(i))
			return false;

	for (int i = 0; i < m; ++i)
		if (solution.getXM().dSumRow(i) > sm[i] || solution.getXD().dSumCol(i) > solution.getXM().dSumRow(i))
			return false;

	for (int i = 0; i < s; ++i)
		if (solution.getXM().dSumCol(i) > ss[i]) 
			return false;

	return true;
}

void CMSCNProblem::generateInstances(int iSeed)
{
	CRandom random(iSeed);

	ud.randomize(random, U_MIN, U_MAX);
	uf.randomize(random, U_MIN, U_MAX);
	um.randomize(random, U_MIN, U_MAX);
	
	sd.randomize(random, S_MIN, S_MAX);
	sf.randomize(random, S_MIN, S_MAX);
	sm.randomize(random, S_MIN, S_MAX);
	ss.randomize(random, S_MIN, S_MAX);
	
	cd.randomize(random, C_MIN, C_MAX);
	cf.randomize(random, C_MIN, C_MAX);
	cm.randomize(random, C_MIN, C_MAX);
}

double CMSCNProblem::calculateKT()
{
	double de = 0, fa = 0, ma = 0;

	for (int i = 0; i < d; i++)
		for (int j = 0; j < f; j++)
			de += cd.get(i, j) * solution.getXD().get(j, i);

	for (int i = 0; i < f; i++)
		for (int j = 0; j < m; j++)
			fa += cf.get(i, j) * solution.getXF().get(j, i);

	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
			ma += cm.get(i, j) * solution.getXM().get(j, i);

	std::cout << "KT: " << std::endl;
	std::cout << de << " " << fa << " " << ma << std::endl;
	return de + fa + ma;
}

double CMSCNProblem::calculateKU()
{
	double de = 0, fa = 0, ma = 0;

	for (int i = 0; i < d; i++)
		for (int j = 0; j < f; j++)
			if (solution.getXD().dSumRow(j) > 0) de += ud[i];

	for (int i = 0; i < f; i++)
		for (int j = 0; j < m; j++)
			if (solution.getXF().dSumRow(j) > 0) fa += uf[i];

	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
			if (solution.getXM().dSumRow(j) > 0) ma += um[i];

	std::cout << de << " " << fa << " " << ma << std::endl;
	return de + fa + ma;
}

double CMSCNProblem::calculateP()
{
	double sum = 0;
	for (int i = 0; i < m; i++)
		for (int j = 0; j < s; j++)
		{
			std::cout << p[j] << " ";
			sum += p[j] * solution.getXM().get(i, j);
		}
		
	return sum;
}