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

	bool bSetCD(int iRow, int iColumn, double dVal);
	bool bSetCF(int iRow, int iColumn, double dVal);
	bool bSetCM(int iRow, int iColumn, double dVal);

	bool bSetSD(int iIndex, double dVal);
	bool bSetSF(int iIndex, double dVal);
	bool bSetSM(int iIndex, double dVal);
	bool bSetSS(int iIndex, double dVal);

	bool bSetUD(int iIndex, double dVal);
	bool bSetUF(int iIndex, double dVal);
	bool bSetUM(int iIndex, double dVal);

	bool bSetP(int iIndex, double dVal);

	bool bSetXDMinMax(int iRow, int iColumn, double dVal);
	bool bSetXFMinMax(int iRow, int iColumn, double dVal);
	bool bSetXMMinMax(int iRow, int iColumn, double dVal);

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