#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include "CSolution.h"

void CSolution::vReadFile(const char * fileName)
{
	std::fstream file(fileName);
	char t;

	file >> t; file >> d; // D 1
	file >> t; file >> f; // F 1
	file >> t; file >> m; // M 1
	file >> t; file >> s; // S 1

	xd.resize(f, d);
	xf.resize(m, f);
	xm.resize(s, m);

	file >> t; file >> t;
	vReadMatrix(file, xd, d, f); // xd

	file >> t; file >> t;
	vReadMatrix(file, xf, f, m); // xf

	file >> t; file >> t;
	vReadMatrix(file, xm, m, s); // xm
}

void CSolution::vReadMatrix(std::fstream& fs, CMatrix & cmatrix, int iRow, int iCol)
{
	std::vector<double> vector;
	std::string str;

	std::getline(fs, str);
	std::getline(fs, str);

	std::istringstream ss(str);

	double num;
	while (ss >> num)
		vector.push_back(num);

	if (iRow * iCol != vector.size()) 
		return;

	cmatrix.resize(iRow, iCol);

	int ind = 0;
	for (int i = 0; i < iRow; i++) 
	{
		for (int j = 0; j < iCol; j++)
		{
			cmatrix.set(i, j, vector[ind]);
			ind++;
		}
	}
}