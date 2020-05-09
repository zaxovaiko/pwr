#pragma once
#include <string>

#define INDEX_OF_FIRST_DATA_IN_SOLUTION 4
#define NULL_ERROR "pd_solution jest NULL"
#define LENGTH_ERROR "length of solution is incorrect"
#define NEGATIVE_VAL_ERROR "negative value in solution"
#define BIGGER_THAN_PRODUCED_ERROR "sum of ordered is bigger than sum of produced"
#define SUM_ERROR "sum of xd < sum of xf OR sum of xf < sum of xm"
#define MIN_MAX_ERROR "value in solution isn't in minmax range"

#define MIN_CD 10
#define MAX_CD 100

#define MIN_CF 10
#define MAX_CF 200

#define MIN_CM 10
#define MAX_CM 300

#define MIN_UD 10
#define MAX_UD 400

#define MIN_UF 10
#define MAX_UF 400

#define MIN_UM 10
#define MAX_UM 400

#define MIN_P 10
#define MAX_P 500

#define MIN_SD 1
#define MAX_SD 1024

#define MIN_SF 2
#define MAX_SF 512

#define MIN_SM 4
#define MAX_SM 256

#define MIN_SS 8
#define MAX_SS 128

using std::string;

class CMscnProblem
{
private:
	int i_D; // dostawcy
	int i_F; // fabryki
	int i_M; // magazyny
	int i_S; // sklepy

	double* pd_sd; // moc produkcyjna dostawcy
	double* pd_sf; // moc produkcyjna fabryki
	double* pd_sm; // moc produkcyjna magazynu
	double* pd_ss; // moc produkcyjna sklepu

	double** ppd_cd; // koszt od dostawcy do fabryki
	double** ppd_cf; // koszt od fabryki do magazynu
	double** ppd_cm; // koszt od magazynu do sklepu

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

	int iGetD() { return i_D; }
	int iGetF() { return i_F; }
	int iGetM() { return i_M; }
	int iGetS() { return i_S; }

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
	bool bConstraintsSatisfied(double *pdSolution, string & sErrorCode);
	bool bSaveSolution(string sFileName);
	bool bSaveObject(string sFileName);
	bool bRead(string sFileName);

	void vGenerateInstance(int iInstanceSeed);
};