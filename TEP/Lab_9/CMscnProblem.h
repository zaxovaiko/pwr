#pragma once
#include <string>

using std::string;

class CMscnProblem
{
private:
	int i_D;
	int i_F;
	int i_M;
	int i_S;

	double* pd_sd; 
	double* pd_sf;
	double* pd_sm;
	double* pd_ss;

	double** ppd_cd;
	double** ppd_cf;
	double** ppd_cm;

	double* pd_ud;
	double* pd_uf;
	double* pd_um;
	double* pd_p;

	double** ppd_xdminmax;
	double** ppd_xfminmax;
	double** ppd_xmminmax;

	double** ppd_xd;
	double** ppd_xf;
	double** ppd_xm;

public:
	CMscnProblem();
	~CMscnProblem();

	bool bSetD(int iVal);
	bool bSetF(int iVal);
	bool bSetM(int iVal);
	bool bSetS(int iVal);

	bool bSetValueCD(int iRow, int iColumn, double dVal);
	bool bSetValueCF(int iRow, int iColumn, double dVal);
	bool bSetValueCM(int iRow, int iColumn, double dVal);

	bool bSetValueSD(int iIndex, double dVal);
	bool bSetValueSF(int iIndex, double dVal);
	bool bSetValueSM(int iIndex, double dVal);
	bool bSetValueSS(int iIndex, double dVal);

	bool bSetValueUD(int iIndex, double dVal);
	bool bSetValueUF(int iIndex, double dVal);
	bool bSetValueUM(int iIndex, double dVal);

	bool bSetValueP(int iIndex, double dVal);

	bool bSetValueXDMinMax(int iRow, int iColumn, double dVal);
	bool bSetValueXFMinMax(int iRow, int iColumn, double dVal);
	bool bSetValueXMMinMax(int iRow, int iColumn, double dVal);

	double dGetMin(double* pdSolution, int iId);
	double dGetMax(double* pdSolution, int iId);
	double dCalculateTransportCost();
	double dCalculateContractCost();
	double dCalculateIncome();
	double dCalculateProfit();

	double dGetQuality(double *pdSolution, bool &isSuccess);
	bool bConstraintsSatisfied(double *pdSolution);
	bool bSaveSolution(string sFileName);
	bool bSaveObject(string sFileName);
	bool bRead(string sFileName);
};