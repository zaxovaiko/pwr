#include "CSolution.h"

using std::fstream;
using std::endl;

CSolution::CSolution(int d, int f, int m, int s)
{
	this->d = d;
	this->f = f;
	this->m = m;
	this->s = s;
	xd = CMatrix(d, f);
	xf = CMatrix(f, m);
	xm = CMatrix(m, s);
}

CSolution::CSolution()
{
	xd = CMatrix();
	xf = CMatrix();
	xm = CMatrix();
	d = 0;
	f = 0;
	m = 0;
	s = 0;
}

void CSolution::setXD(double v, int i, int j) { vSetMatrix(xd, v, i, j); }
void CSolution::setXM(double v, int i, int j) { vSetMatrix(xm, v, i, j); }
void CSolution::setXF(double v, int i, int j) { vSetMatrix(xf, v, i, j); }

void CSolution::vReadFile(const char* filename)
{
	fstream file(filename);
	char temp;

	file >> temp; file >> d;
	file >> temp; file >> f;
	file >> temp; file >> m;
	file >> temp; file >> s;

	xd.vResize(f, d);
	xf.vResize(m, f);
	xm.vResize(s, m);

	double helper = 0;

	file >> temp; file >> temp;
	vReadMatrixFile(file, xd, d, f);

	file >> temp; file >> temp;
	vReadMatrixFile(file, xf, f, m);

	file >> temp; file >> temp;
	vReadMatrixFile(file, xm, m, s);
}

CSolution CSolution::vReadDoubleTable(double * pdSolution, int d, int f, int m, int s)
{
	CSolution help(d, f, s, m);

	for (int i = 0; i < d; ++i)
		for (int j = 0; j < f; ++j)
			help.xd.vSet(pdSolution[i * f + j], i, j);

	int xdSize = help.getXD().iGetSize();

	for (int i = 0; i < f; ++i)
		for (int j = 0; j < m; ++j)
			help.xf.vSet(pdSolution[xdSize + i * m + j], i, j);

	int xfSize = help.getXF().iGetSize();

	for (int i = 0; i < m; ++i)
		for (int j = 0; j < s; ++j)
			help.xm.vSet(pdSolution[xdSize + xfSize + i * s + j], i, j);

	return help;
}
double * CSolution::toDoubleTable()
{
	int i_size = d * f + f * m + s * m, i_counter = 0;
	double * pd_table = new double[i_size];

	for (int i = 0; i < d; i++)
	{
		for (int j = 0; j < f; j++)
		{
			pd_table[i_counter] = xd.dGet(i, j);
			i_counter++;
		}
	}

	for (int i = 0; i < f; i++)
	{
		for (int j = 0; j < m; j++)
		{
			pd_table[i_counter] = xf.dGet(i, j);
			i_counter++;
		}
	}

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < s; j++)
		{
			pd_table[i_counter] = xm.dGet(i, j);
			i_counter++;
		}
	}

	return pd_table;
}
void CSolution::vSaveMatrixFile(fstream & fs, CMatrix & matrix)
{
	for (int ii = 0; ii < matrix.iGetRows(); ii++)
		for (int jj = 0; jj < matrix.iGetCols(); jj++)
			fs << matrix.dGet(ii, jj) << " ";
}

void CSolution::vSetMatrix(CMatrix & mat, double value, int i, int j)
{
	if (value < 0 || !mat.checkRowsAndColumns(i, j))
		return;
	mat.vSet(value, i, j);
}

void CSolution::vReadMatrixFile(fstream & fs, CMatrix & cmatrix, int iRows, int iCols)
{
	vector<double> d_vector;
	string str;

	getline(fs, str);
	getline(fs, str);

	istringstream ss(str);
	double d_num;
	while (ss >> d_num)
		d_vector.push_back(d_num);

	if (iCols * iRows != d_vector.size()) 
		return;

	cmatrix.vResize(iRows, iCols);
	int helpVec = 0;
	for (int i = 0; i < iRows; i++)
	{
		for (int j = 0; j < iCols; j++) 
		{
			cmatrix.vSet(d_vector[helpVec], i, j);
			helpVec++;
		}
	}
}

void CSolution::vSaveFile(const char * filename)
{
	fstream file(filename);
	file.flush();

	file << "D "; file << d << endl;
	file << "F "; file << f << endl;
	file << "M "; file << m << endl;
	file << "S "; file << s << endl;

	file << "xd" << endl; vSaveMatrixFile(file, xd); file << endl;
	file << "xf" << endl; vSaveMatrixFile(file, xf); file << endl;
	file << "xm" << endl; vSaveMatrixFile(file, xm); file << endl;

	file.close();
}