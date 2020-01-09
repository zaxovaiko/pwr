#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include "CMscnProblem.h"
#include "CRandom.h"

using namespace std;

CMscnProblem::CMscnProblem() {
	i_D = 1;
	i_F = 1;
	i_M = 1;
	i_S = 1;

	pd_sd = new double[i_D];
	pd_sf = new double[i_F];
	pd_sm = new double[i_M];
	pd_ss = new double[i_S];

	ppd_cd = new double*[i_D];
	ppd_cf = new double*[i_F];
	ppd_cm = new double*[i_M];

	for (int i = 0; i < i_D; i++) ppd_cd[i] = new double[i_F];
	for (int i = 0; i < i_F; i++) ppd_cf[i] = new double[i_M];
	for (int i = 0; i < i_M; i++) ppd_cm[i] = new double[i_S];

	pd_ud = new double[i_D];
	pd_uf = new double[i_F];
	pd_um = new double[i_M];

	pd_p = new double[i_S]; // Income

	ppd_xdminmax = new double*[2 * i_D];
	ppd_xfminmax = new double*[2 * i_F];
	ppd_xmminmax = new double*[2 * i_M];

	for (int i = 0; i < 2 * i_D; i++) ppd_xdminmax[i] = new double[i_F];
	for (int i = 0; i < 2 * i_F; i++) ppd_xfminmax[i] = new double[i_M];
	for (int i = 0; i < 2 * i_M; i++) ppd_xmminmax[i] = new double[i_S];

	ppd_xd = new double*[i_D];
	ppd_xf = new double*[i_F];
	ppd_xm = new double*[i_M];

	for (int i = 0; i < i_D; i++) ppd_xd[i] = new double[i_F];
	for (int i = 0; i < i_F; i++) ppd_xf[i] = new double[i_M];
	for (int i = 0; i < i_M; i++) ppd_xm[i] = new double[i_S];
}

CMscnProblem::~CMscnProblem() {
	delete[] pd_sd;
	delete[] pd_sf;
	delete[] pd_sm;
	delete[] pd_ss;

	for (int i = 0; i < i_D; i++) delete[] ppd_cd[i];
	for (int i = 0; i < i_F; i++) delete[] ppd_cf[i];
	for (int i = 0; i < i_M; i++) delete[] ppd_cm[i];

	delete[] ppd_cd;
	delete[] ppd_cf;
	delete[] ppd_cm;

	delete[] pd_ud;
	delete[] pd_uf;
	delete[] pd_um;

	delete[] pd_p;

	for (int i = 0; i < 2 * i_D; i++) delete[] ppd_xdminmax[i];
	for (int i = 0; i < 2 * i_F; i++) delete[] ppd_xfminmax[i];
	for (int i = 0; i < 2 * i_M; i++) delete[] ppd_xmminmax[i];

	delete[] ppd_xdminmax;
	delete[] ppd_xfminmax;
	delete[] ppd_xmminmax;

	for (int i = 0; i < i_D; i++) delete[] ppd_xd[i];
	for (int i = 0; i < i_F; i++) delete[] ppd_xf[i];
	for (int i = 0; i < i_M; i++) delete[] ppd_xm[i];

	delete[] ppd_xd;
	delete[] ppd_xf;
	delete[] ppd_xm;
}

bool CMscnProblem::bSetD(int iVal) {
	if (iVal < 0 || iVal == i_D) {
		return false;
	}

	double* pd_new_sd = new double[iVal];
	double* pd_new_ud = new double[iVal];
	double** ppd_new_cd = new double*[iVal];
	double** ppd_new_xd = new double*[iVal];
	double** ppd_new_xdminmax = new double*[2 * iVal];

	for (int i = 0; i < iVal; i++) {
		pd_new_sd[i] = pd_sd[i];
		pd_new_ud[i] = pd_ud[i];
		ppd_new_cd[i] = ppd_cd[i];
		ppd_new_xd[i] = ppd_xd[i];
		ppd_new_xdminmax[i] = ppd_xdminmax[i];
	}

	for (int i = iVal; i < 2 * iVal; i++) {
		ppd_new_xdminmax[i] = ppd_xdminmax[i];
	}

	if (i_D < iVal) {
		for (int i = i_D; i < iVal; i++) {
			ppd_new_cd[i] = new double[i_F];
			ppd_new_xd[i] = new double[i_F];
		}
		for (int i = 2 * i_D; i < 2 * iVal; i++) {
			ppd_new_xdminmax[i] = new double[i_F];
		}
	}

	for (int i = iVal; i < i_D; i++) {
		delete[] ppd_cd[i];
		delete[] ppd_xd[i];
	}

	delete[] pd_sd;
	delete[] pd_ud;
	delete[] ppd_cd;
	delete[] ppd_xd;

	pd_sd = pd_new_sd;
	pd_ud = pd_new_ud;
	ppd_cd = ppd_new_cd;
	ppd_xd = ppd_new_xd;

	for (int i = 2 * iVal; i < 2 * i_D; i++)
		delete[] ppd_xdminmax[i];
	delete[] ppd_xdminmax;

	ppd_xdminmax = ppd_new_xdminmax;

	i_D = iVal;
	return true;
}

bool CMscnProblem::bSetF(int iVal) {
	if (iVal < 0 || iVal == i_F) {
		return false;
	}

	double* pd_new_sf = new double[iVal];
	double* pd_new_uf = new double[iVal];
	double** ppd_new_cf = new double*[iVal];
	double** ppd_new_cd = new double*[i_D];
	double** ppd_new_xf = new double*[iVal];
	double** ppd_new_xd = new double*[i_D];
	double** ppd_new_xdminmax = new double*[2 * i_D];
	double** ppd_new_xfminmax = new double*[2 * iVal];

	for (int i = 0; i < i_D; i++) {
		ppd_new_cd[i] = new double[iVal];
		ppd_new_xd[i] = new double[iVal];
	}
	for (int i = 0; i < 2 * i_D; i++) {
		ppd_new_xdminmax[i] = new double[iVal];
	}

	for (int i = 0; i < i_D; i++) {
		for (int j = 0; j < iVal; j++) {
			ppd_new_cd[i][j] = ppd_cd[i][j];
			ppd_new_xd[i][j] = ppd_xd[i][j];
			ppd_new_xdminmax[i][j] = ppd_xdminmax[i][j];
		}
	}

	for (int i = i_D; i < 2 * i_D; i++) {
		for (int j = 0; j < iVal; j++) {
			ppd_new_xdminmax[i][j] = ppd_xdminmax[i][j];
		}
	}

	for (int i = 0; i < iVal; i++) {
		pd_new_sf[i] = pd_sf[i];
		pd_new_uf[i] = pd_uf[i];
		ppd_new_cf[i] = ppd_cf[i];
		ppd_new_xf[i] = ppd_xf[i];
		ppd_new_xfminmax[i] = ppd_xfminmax[i];
	}

	for (int i = iVal; i < 2 * iVal; i++) {
		ppd_new_xfminmax[i] = ppd_xfminmax[i];
	}

	if (i_F < iVal) {
		for (int i = i_F; i < iVal; i++) {
			ppd_new_cf[i] = new double[i_M];
			ppd_new_xf[i] = new double[i_M];
		}
		for (int i = 2 * i_F; i < 2 * iVal; i++) {
			ppd_new_xfminmax[i] = new double[i_M];
		}
	}

	for (int i = 0; i < i_D; i++) {
		for (int j = iVal; j < i_F; j++) {
			delete ppd_cd[i];
			delete ppd_xd[i];
		}
	}

	for (int i = iVal; i < i_F; i++) {
		delete[] ppd_cf[i];
		delete[] ppd_xf[i];
	}

	delete[] pd_sf;
	delete[] pd_uf;
	delete[] ppd_cf;
	delete[] ppd_xf;
	delete[] ppd_cd;
	delete[] ppd_xd;

	pd_sf = pd_new_sf;
	pd_uf = pd_new_uf;
	ppd_cd = ppd_new_cd;
	ppd_xd = ppd_new_xd;
	ppd_cf = ppd_new_cf;
	ppd_xf = ppd_new_xf;

	for (int i = 0; i < 2 * i_D; i++)
		for (int j = iVal; j < i_F; j++)
			delete[] ppd_xdminmax[i];

	for (int i = 2 * iVal; i < 2 * i_F; i++)
		delete[] ppd_xfminmax[i];

	delete[] ppd_xfminmax;
	delete[] ppd_xdminmax;

	ppd_xfminmax = ppd_new_xfminmax;
	ppd_xdminmax = ppd_new_xdminmax;

	i_F = iVal;
	return true;
}

bool CMscnProblem::bSetM(int iVal) {
	if (iVal < 0 || iVal == i_M) {
		return false;
	}

	double* pd_new_sm = new double[iVal];
	double* pd_new_um = new double[iVal];
	double** ppd_new_cm = new double*[iVal];
	double** ppd_new_cf = new double*[i_F];
	double** ppd_new_xm = new double*[iVal];
	double** ppd_new_xf = new double*[i_F];
	double** ppd_new_xfminmax = new double*[2 * i_F];
	double** ppd_new_xmminmax = new double*[2 * iVal];

	for (int i = 0; i < i_F; i++) {
		ppd_new_cf[i] = new double[iVal];
		ppd_new_xf[i] = new double[iVal];
	}
	for (int i = 0; i < 2 * i_F; i++) {
		ppd_new_xfminmax[i] = new double[iVal];
	}


	for (int i = 0; i < i_F; i++) {
		for (int j = 0; j < iVal; j++) {
			ppd_new_cf[i][j] = ppd_cf[i][j];
			ppd_new_xf[i][j] = ppd_xf[i][j];
			ppd_new_xfminmax[i][j] = ppd_xfminmax[i][j];
		}
	}

	for (int i = i_F; i < 2 * i_F; i++) {
		for (int j = 0; j < iVal; j++) {
			ppd_new_xfminmax[i][j] = ppd_xfminmax[i][j];
		}
	}

	for (int i = 0; i < iVal; i++) {
		pd_new_sm[i] = pd_sm[i];
		pd_new_um[i] = pd_um[i];
		ppd_new_cm[i] = ppd_cm[i];
		ppd_new_xm[i] = ppd_xm[i];
		ppd_new_xmminmax[i] = ppd_xmminmax[i];
	}

	for (int i = iVal; i < 2 * iVal; i++) {
		ppd_new_xmminmax[i] = ppd_xmminmax[i];
	}

	if (i_M < iVal) {
		for (int i = i_M; i < iVal; i++) {
			ppd_new_cm[i] = new double[i_S];
			ppd_new_xm[i] = new double[i_S];
		}
		for (int i = 2 * i_M; i < 2 * iVal; i++) {
			ppd_new_xmminmax[i] = new double[i_S];
		}
	}

	for (int i = 0; i < i_F; i++) {
		for (int j = iVal; j < i_M; j++) {
			delete ppd_cf[i];
			delete ppd_xf[i];
		}
	}

	for (int i = iVal; i < i_M; i++) {
		delete[] ppd_cm[i];
		delete[] ppd_xm[i];
	}

	delete[] pd_sm;
	delete[] pd_um;
	delete[] ppd_cm;
	delete[] ppd_xm;
	delete[] ppd_cf;
	delete[] ppd_xf;

	pd_sm = pd_new_sm;
	pd_um = pd_new_um;
	ppd_cf = ppd_new_cf;
	ppd_xf = ppd_new_xf;
	ppd_cm = ppd_new_cm;
	ppd_xm = ppd_new_xm;

	for (int i = 0; i < 2 * i_F; i++)
		for (int j = iVal; j < i_M; j++)
			delete[] ppd_xfminmax[i];

	for (int i = 2 * iVal; i < 2 * i_M; i++)
		delete[] ppd_xmminmax[i];

	delete[] ppd_xmminmax;
	delete[] ppd_xfminmax;

	ppd_xmminmax = ppd_new_xmminmax;
	ppd_xfminmax = ppd_new_xfminmax;

	i_M = iVal;
	return true;
}

bool CMscnProblem::bSetS(int iVal) {
	if (iVal < 0 || iVal == i_S) {
		return false;
	}

	double* pd_new_ss = new double[iVal];
	double* pd_new_p = new double[iVal];
	double** ppd_new_cm = new double*[i_M];
	double** ppd_new_xm = new double*[i_M];
	double** ppd_new_xmminmax = new double*[2 * i_M];

	for (int i = 0; i < i_M; i++) {
		ppd_new_cm[i] = new double[iVal];
		ppd_new_xm[i] = new double[iVal];
	}

	for (int i = 0; i < 2 * i_M; i++) {
		ppd_new_xmminmax[i] = new double[iVal];
	}

	for (int i = 0; i < i_M; i++) {
		for (int j = 0; j < iVal; j++) {
			ppd_new_cm[i][j] = ppd_cm[i][j];
			ppd_new_xm[i][j] = ppd_xm[i][j];
			ppd_new_xmminmax[i][j] = ppd_xmminmax[i][j];
		}
	}

	for (int i = i_M; i < 2 * i_M; i++)
		for (int j = 0; j < iVal; j++)
			ppd_new_xmminmax[i][j] = ppd_xmminmax[i][j];

	for (int i = 0; i < iVal; i++) {
		pd_new_ss[i] = pd_ss[i];
		pd_new_p[i] = pd_p[i];
	}

	for (int i = 0; i < i_M; i++) {
		for (int j = iVal; j < i_S; j++) {
			delete ppd_cm[i];
			delete ppd_xm[i];
		}
	}

	delete[] pd_ss;
	delete[] pd_p;
	delete[] ppd_cm;
	delete[] ppd_xm;

	pd_ss = pd_new_ss;
	pd_p = pd_new_p;
	ppd_cm = ppd_new_cm;
	ppd_xm = ppd_new_xm;

	for (int i = 0; i < 2 * i_M; i++)
		for (int j = iVal; j < i_S; j++)
			delete[] ppd_xmminmax[i];

	delete[] ppd_xmminmax;
	ppd_xmminmax = ppd_new_xmminmax;

	i_S = iVal;
	return true;
}

bool CMscnProblem::bSetCD(int iRow, int iColumn, double dVal) {
	if (iRow < 0 || iRow >= i_D || iColumn < 0 || iColumn >= i_F) {
		return false;
	}
	ppd_cd[iRow][iColumn] = dVal;
	return true;
}

bool CMscnProblem::bSetCF(int iRow, int iColumn, double dVal) {
	if (iRow < 0 || iRow >= i_F || iColumn < 0 || iColumn >= i_M) {
		return false;
	}
	ppd_cf[iRow][iColumn] = dVal;
	return true;
}

bool CMscnProblem::bSetCM(int iRow, int iColumn, double dVal) {
	if (iRow < 0 || iRow >= i_M || iColumn < 0 || iColumn >= i_S) {
		return false;
	}
	ppd_cm[iRow][iColumn] = dVal;
	return true;
}

bool CMscnProblem::bSetSD(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_D) {
		return false;
	}
	pd_sd[iIndex] = dVal;
}

bool CMscnProblem::bSetSF(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_F) {
		return false;
	}
	pd_sf[iIndex] = dVal;
}

bool CMscnProblem::bSetSM(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_M) {
		return false;
	}
	pd_sm[iIndex] = dVal;
}

bool CMscnProblem::bSetSS(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_S) {
		return false;
	}
	pd_ss[iIndex] = dVal;
}

bool CMscnProblem::bSetUD(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_D) {
		return false;
	}
	pd_ud[iIndex] = dVal;
}

bool CMscnProblem::bSetUF(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_F) {
		return false;
	}
	pd_uf[iIndex] = dVal;
}

bool CMscnProblem::bSetUM(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_M) {
		return false;
	}
	pd_um[iIndex] = dVal;
}

bool CMscnProblem::bSetP(int iIndex, double dVal) {
	if (iIndex < 0 || iIndex >= i_S) {
		return false;
	}
	pd_p[iIndex] = dVal;
}

bool CMscnProblem::bSetXDMinMax(int iRow, int iColumn, double dVal) {
	if (iRow < 0 || iRow >= 2 * i_D || iColumn < 0 || iColumn >= i_F) {
		return false;
	}
	ppd_xdminmax[iRow][iColumn] = dVal;
	return true;
}

bool CMscnProblem::bSetXFMinMax(int iRow, int iColumn, double dVal) {
	if (iRow < 0 || iRow >= 2 * i_F || iColumn < 0 || iColumn >= i_M) {
		return false;
	}
	ppd_xfminmax[iRow][iColumn] = dVal;
	return true;
}

bool CMscnProblem::bSetXMMinMax(int iRow, int iColumn, double dVal) {
	if (iRow < 0 || iRow >= 2 * i_M || iColumn < 0 || iColumn >= i_S) {
		return false;
	}
	ppd_xmminmax[iRow][iColumn] = dVal;
	return true;
}

double CMscnProblem::dGetMin(double * pdSolution, int iId) {
	if (iId >= i_D * i_F) {
		iId -= i_D * i_F;
	}
	else {
		return ppd_xdminmax[2 * (iId / i_F)][iId%i_F];
	}

	if (iId >= i_F * i_M) {
		iId -= i_F * i_M;
	}
	else {

		return ppd_xfminmax[2 * (iId / i_M)][iId%i_M];
	}

	if (iId >= i_M * i_S) {
		iId -= i_M * i_S;
	}
	else {
		return ppd_xmminmax[2 * (iId / i_S)][iId%i_S];
	}

	return -1;
}

double CMscnProblem::dGetMax(double * pdSolution, int iId) {

	if (iId >= i_D * i_F) {
		iId -= i_D * i_F;
	}
	else {
		return ppd_xdminmax[1 + 2 * (iId / i_F)][iId%i_F];
	}

	if (iId >= i_F * i_M) {
		iId -= i_F * i_M;
	}
	else {
		return ppd_xfminmax[1 + 2 * (iId / i_M)][iId%i_M];
	}

	if (iId >= i_M * i_S) {
		iId -= i_M * i_S;
	}
	else {
		return ppd_xmminmax[1 + 2 * (iId / i_S)][iId%i_S];
	}

	return -1;
}

double CMscnProblem::dCalculateTransportCost() {
	double d_sum = 0;

	for (int i = 0; i < i_D; i++) {
		for (int j = 0; j < i_F; j++) {
			d_sum += ppd_cd[i][j] * ppd_xd[i][j];
		}
	}

	for (int i = 0; i < i_F; i++) {
		for (int j = 0; j < i_M; j++) {
			d_sum += ppd_cf[i][j] * ppd_xf[i][j];
		}
	}

	for (int i = 0; i < i_M; i++) {
		for (int j = 0; j < i_S; j++) {
			d_sum += ppd_cm[i][j] * ppd_xm[i][j];
		}
	}

	return d_sum;
}

double CMscnProblem::dCalculateContractCost() {
	double d_sum = 0;

	for (int i = 0; i < i_D; i++) {
		double d_count_of_element = 0;
		for (int j = 0; j < i_F; j++) {
			d_count_of_element += ppd_xd[i][j];
		}
		d_sum += pd_ud[i] * d_count_of_element;
	}

	for (int i = 0; i < i_F; i++) {
		double d_count_of_element = 0;
		for (int j = 0; j < i_M; j++) {
			d_count_of_element += ppd_xf[i][j];
		}
		d_sum += pd_uf[i] * d_count_of_element;
	}

	for (int i = 0; i < i_M; i++) {
		double d_count_of_element = 0;
		for (int j = 0; j < i_S; j++) {
			d_count_of_element += ppd_xm[i][j];
		}
		d_sum += pd_um[i] * d_count_of_element;
	}

	return d_sum;
}

double CMscnProblem::dCalculateIncome() {
	double d_sum = 0;
	for (int i = 0; i < i_M; i++) {
		for (int j = 0; j < i_S; j++) {
			d_sum += pd_p[i] * ppd_xd[i][j];
		}
	}
	return d_sum;
}

double CMscnProblem::dCalculateProfit() {
	return dCalculateIncome() - dCalculateTransportCost() - dCalculateContractCost();
}

double CMscnProblem::dGetQuality(double * pdSolution, bool &bIsSuccess) {
	bIsSuccess = true;

	if (pdSolution == NULL) {
		bIsSuccess = false;
	}

	int count = 0;
	i_D = pdSolution[count++];
	i_F = pdSolution[count++];
	i_M = pdSolution[count++];
	i_S = pdSolution[count++];

	for (int i = 0; i < i_D; i++) {
		for (int j = 0; j < i_F; j++) {
			if (pdSolution[count] >= 0) {
				ppd_xd[i][j] = pdSolution[count];
				count++;
			}
			else {
				bIsSuccess = false;
				i = i_D; 
				j = i_F;
			}
		}
	}

	for (int i = 0; i < i_F; i++) {
		for (int j = 0; j < i_M; j++) {
			if (pdSolution[count] >= 0) {
				ppd_xf[i][j] = pdSolution[count];
				count++;
			}
			else {
				bIsSuccess = false;
				i = i_F; 
				j = i_M;
			}
		}
	}

	for (int i = 0; i < i_M; i++) {
		for (int j = 0; j < i_S; j++) {
			if (pdSolution[count] >= 0) {
				ppd_xm[i][j] = pdSolution[count];
				count++;
			}
			else {
				bIsSuccess = false;
				i = i_M; 
				j = i_S;
			}
		}
	}

	return dCalculateProfit();
}

bool CMscnProblem::bConstraintsSatisfied(double * pdSolution, string & sErrorCode) {
	sErrorCode = "";

	if (pdSolution == NULL) {
		sErrorCode = NULL_ERROR;
		return false;
	}

	int i_counter = 0;
	if (i_D != pdSolution[i_counter++] ||
		i_F != pdSolution[i_counter++] ||
		i_M != pdSolution[i_counter++] ||
		i_S != pdSolution[i_counter++]) {
		sErrorCode = LENGTH_ERROR;
		return false;
	}

	double d_current_sum_xd = 0;
	double d_current_sum_xf = 0;
	double d_current_sum_xm = 0;
	double d_total_sum_xd = 0;
	double d_total_sum_xf = 0;
	double d_total_sum_xm = 0;

	for (int i = 0; i < i_D; i++) {
		for (int j = 0; j < i_F; j++) {
			if (pdSolution[i_counter] >= 0) {
				d_current_sum_xd += pdSolution[i_counter];
				i_counter++;
			}
			else {
				sErrorCode = NEGATIVE_VAL_ERROR;
				return false;
			}
		}

		if (d_current_sum_xd > pd_sd[i]) {
			sErrorCode = BIGGER_THAN_PRODUCED_ERROR;
			return false;
		}
		d_total_sum_xd += d_current_sum_xd;
		d_current_sum_xd = 0;
	}

	for (int i = 0; i < i_F; i++) {
		for (int j = 0; j < i_M; j++) {
			if (pdSolution[i_counter] >= 0) {
				d_current_sum_xf += pdSolution[i_counter];
				i_counter++;
			}
			else {
				sErrorCode = NEGATIVE_VAL_ERROR;
				return false;
			}
		}

		if (d_current_sum_xf > pd_sf[i]) {
			sErrorCode = BIGGER_THAN_PRODUCED_ERROR;
			return false;
		}
		d_total_sum_xf += d_current_sum_xf;
		d_current_sum_xf = 0;
	}

	for (int i = 0; i < i_M; i++) {
		for (int j = 0; j < i_S; j++) {
			if (pdSolution[i_counter] >= 0) {
				d_current_sum_xm += pdSolution[i_counter];
				i_counter++;
			}
			else {
				sErrorCode = NEGATIVE_VAL_ERROR;
				return false;
			}
		}

		if (d_current_sum_xm > pd_sm[i]) {
			sErrorCode = BIGGER_THAN_PRODUCED_ERROR;
			return false;
		}
		d_total_sum_xm += d_current_sum_xm;
		d_current_sum_xm = 0;
	}

	d_current_sum_xm = 0;
	i_counter = INDEX_OF_FIRST_DATA_IN_SOLUTION + i_D * i_F + i_F * i_M;

	for (int i = 0; i < i_S; i++) {
		for (int j = 0; j < i_M; j++) {
			d_current_sum_xm += pdSolution[i_counter + i_M * j]; 
		}

		if (d_current_sum_xm > pd_ss[i]) {
			sErrorCode = BIGGER_THAN_PRODUCED_ERROR;
			return false;
		}

		d_current_sum_xm = 0;
		i_counter++;
	}

	if (d_total_sum_xd < d_total_sum_xf || d_total_sum_xf < d_total_sum_xm) {
		sErrorCode = SUM_ERROR;
		return false;
	}


	i_counter = 0;
	for (int i = 0; i < 2 * i_D; i += 2) {
		for (int j = 0; j < i_F; j++) {
			if (pdSolution[i_counter] < ppd_xdminmax[i][j] || pdSolution[i_counter] > ppd_xdminmax[i + 1][j]) {
				sErrorCode = MIN_MAX_ERROR;
				return false;
			}
			i_counter++;
		}
	}

	for (int i = 0; i < 2 * i_F; i += 2) {
		for (int j = 0; j < i_M; j++) {
			if (pdSolution[i_counter] < ppd_xfminmax[i][j] || pdSolution[i_counter] > ppd_xfminmax[i + 1][j]) {
				sErrorCode = MIN_MAX_ERROR;
				return false;
			}
			i_counter++;
		}
	}

	for (int i = 0; i < 2 * i_M; i += 2) {
		for (int j = 0; j < i_S; j++) {
			if (pdSolution[i_counter] < ppd_xmminmax[i][j] || pdSolution[i_counter] > ppd_xmminmax[i + 1][j]) {
				sErrorCode = MIN_MAX_ERROR;
				return false;
			}
			i_counter++;
		}
	}

	return true;
}

bool CMscnProblem::bSaveSolution(string sFileName)
{
	if (sFileName == "") return false;

	FILE *pfFile;
	pfFile = fopen(sFileName.c_str(), "w+");

	if (pfFile != NULL) {
		fprintf(pfFile, "%s %d\n", "D", i_D);
		fprintf(pfFile, "%s %d\n", "F", i_F);
		fprintf(pfFile, "%s %d\n", "M", i_M);
		fprintf(pfFile, "%s %d\n", "S", i_S);

		fprintf(pfFile, "\nxd\n");
		for (int ii = 0; ii < i_D; ii++)
			for (int ij = 0; ij < i_F; ij++)
				fprintf(pfFile, "%g ", ppd_xd[ii][ij]);

		fprintf(pfFile, "\nxf\n");
		for (int ii = 0; ii < i_F; ii++)
			for (int ij = 0; ij < i_M; ij++)
				fprintf(pfFile, "%g ", ppd_xf[ii][ij]);

		fprintf(pfFile, "\nxm\n");
		for (int ii = 0; ii < i_M; ii++)
			for (int ij = 0; ij < i_S; ij++)
				fprintf(pfFile, "%g ", ppd_xm[ii][ij]);

		fclose(pfFile);
		return true;
	}

	return false;
}

bool CMscnProblem::bRead(string sFileName) {
	fstream file(sFileName);

	string ch;
	string q;
	int i_num;
	double d_num;

	file >> ch;
	file >> i_num;
	bSetD(i_num);

	file >> ch;
	file >> i_num;
	bSetF(i_num);

	file >> ch;
	file >> i_num;
	bSetM(i_num);

	file >> ch;
	file >> i_num;
	bSetS(i_num);

	cout << "D " << i_D << endl;
	cout << "F " << i_F << endl;
	cout << "M " << i_M << endl;
	cout << "S " << i_S << endl;

	file >> ch;
	for (int i = 0; i < i_D; i++) {
		file >> d_num >> q;
		bSetSD(i, d_num);
		cout << "sd[" << i << +"]: " << pd_sd[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < i_F; i++) {
		file >> d_num >> q;
		bSetSF(i, d_num);
		cout << "sf[" << i << +"]: " << pd_sf[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < i_M; i++) {
		file >> d_num >> q;
		bSetSM(i, d_num);
		cout << "sm[" << i << +"]: " << pd_sm[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < i_S; i++) {
		file >> d_num >> q;
		bSetSS(i, d_num);
		cout << "ss[" << i << +"]: " << pd_ss[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < i_D; i++) {
		for (int j = 0; j < i_F; j++) {
			file >> d_num >> q;
			bSetCD(i, j, d_num);
			cout << "cd[" << i << "][" << j << "]: " << ppd_cd[i][j] << "\n";
		}
	}

	file >> ch;
	for (int i = 0; i < i_F; i++) {
		for (int j = 0; j < i_M; j++) {
			file >> d_num >> q;
			bSetCF(i, j, d_num);
			cout << "cf[" << i << "][" << j << "]: " << ppd_cf[i][j] << "\n";
		}
	}

	file >> ch;
	for (int i = 0; i < i_M; i++) {
		for (int j = 0; j < i_S; j++) {
			file >> d_num >> q;
			bSetCM(i, j, d_num);
			cout << "cm[" << i << "][" << j << "]: " << ppd_cm[i][j] << "\n";
		}
	}

	file >> ch;
	for (int i = 0; i < i_D; i++) {
		file >> d_num >> q;
		bSetUD(i, d_num);
		cout << "ud[" << i << "]: " << pd_ud[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < i_D; i++) {
		file >> d_num >> q;
		bSetUF(i, d_num);
		cout << "uf[" << i << "]: " << pd_uf[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < i_D; i++) {
		file >> d_num >> q;
		bSetUM(i, d_num);
		cout << "um[" << i << "]: " << pd_um[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < i_S; i++) {
		file >> d_num >> q;
		bSetP(i, d_num);
		cout << "p[" << i << "]: " << pd_p[i] << "\n";
	}

	file >> ch;
	for (int i = 0; i < 2 * i_D; i += 2) {
		for (int j = 0; j < i_F; j++) {
			file >> d_num >> q;
			bSetXDMinMax(i, j, d_num);
			cout << "xdminmax[" << i << ", " << j << "]: " << ppd_xdminmax[i][j] << "\n";
			file >> d_num >> q;
			bSetXDMinMax(i + 1, j, d_num);
			cout << "xdminmax[" << i + 1 << ", " << j << "]: " << ppd_xdminmax[i + 1][j] << "\n";
		}
	}

	file >> ch;
	for (int i = 0; i < 2 * i_F; i += 2) {
		for (int j = 0; j < i_M; j++) {
			file >> d_num >> q;
			bSetXFMinMax(i, j, d_num);
			cout << "xfminmax[" << i << ", " << j << "]: " << ppd_xfminmax[i][j] << "\n";
			file >> d_num >> q;
			bSetXFMinMax(i + 1, j, d_num);
			cout << "xfminmax[" << i + 1 << ", " << j << "]: " << ppd_xfminmax[i + 1][j] << "\n";
		}
	}

	file >> ch;
	for (int i = 0; i < 2 * i_M; i += 2) {
		for (int j = 0; j < i_S; j++) {
			file >> d_num >> q;
			bSetXMMinMax(i, j, d_num);
			cout << "xmminmax[" << i << ", " << j << "]: " << ppd_xmminmax[i][j] << "\n";
			file >> d_num >> q;
			bSetXMMinMax(i + 1, j, d_num);
			cout << "xmminmax[" << i + 1 << ", " << j << "]: " << ppd_xmminmax[i + 1][j] << "\n";
		}
	}

	return true;
}

bool CMscnProblem::bSaveObject(string sFileName) {
	if (sFileName == "") {
		return false;
	}

	FILE *pfFile;
	pfFile = fopen(sFileName.c_str(), "w+");

	if (pfFile != NULL) {
		fprintf(pfFile, "%s %d\n", "D", i_D);
		fprintf(pfFile, "%s %d\n", "F", i_F);
		fprintf(pfFile, "%s %d\n", "M", i_M);
		fprintf(pfFile, "%s %d\n", "S", i_S);

		fprintf(pfFile, "sd\n");
		for (int i = 0; i < i_D; i++)
			fprintf(pfFile, "%g ", pd_sd[i]);

		fprintf(pfFile, "\nsf\n");
		for (int i = 0; i < i_F; i++)
			fprintf(pfFile, "%g ", pd_sf[i]);

		fprintf(pfFile, "\nsm\n");
		for (int i = 0; i < i_M; i++)
			fprintf(pfFile, "%g ", pd_sm[i]);

		fprintf(pfFile, "\nss\n");
		for (int i = 0; i < i_S; i++)
			fprintf(pfFile, "%g ", pd_ss[i]);

		fprintf(pfFile, "\ncd\n");
		for (int i = 0; i < i_D; i++) {
			for (int j = 0; j < i_F; j++)
				fprintf(pfFile, "%g ", ppd_cd[i][j]);
			fprintf(pfFile, "\n");
		}

		fprintf(pfFile, "cf\n");
		for (int i = 0; i < i_F; i++) {
			for (int j = 0; j < i_M; j++)
				fprintf(pfFile, "%g ", ppd_cf[i][j]);
			fprintf(pfFile, "\n");
		}

		fprintf(pfFile, "cm\n");
		for (int ii = 0; ii < i_M; ii++) {
			for (int ij = 0; ij < i_S; ij++)
				fprintf(pfFile, "%g ", ppd_cm[ii][ij]);
			fprintf(pfFile, "\n");
		}

		fprintf(pfFile, "ud\n");
		for (int ii = 0; ii < i_D; ii++)
			fprintf(pfFile, "%g ", pd_ud[ii]);

		fprintf(pfFile, "\nuf\n");
		for (int ii = 0; ii < i_F; ii++)
			fprintf(pfFile, "%g ", pd_uf[ii]);

		fprintf(pfFile, "\num\n");
		for (int ii = 0; ii < i_M; ii++)
			fprintf(pfFile, "%g ", pd_um[ii]);

		fprintf(pfFile, "\np\n");
		for (int ii = 0; ii < i_S; ii++)
			fprintf(pfFile, "%g ", pd_p[ii]);

		fprintf(pfFile, "\nxdminmax\n");
		for (int ii = 0; ii < 2 * i_D; ii++)
			for (int ij = 0; ij < i_F; ij++)
				fprintf(pfFile, "%g ", ppd_xdminmax[ii][ij]);

		fprintf(pfFile, "\nxfminmax\n");
		for (int ii = 0; ii < 2 * i_F; ii++)
			for (int ij = 0; ij < i_M; ij++)
				fprintf(pfFile, "%g ", ppd_xfminmax[ii][ij]);

		fprintf(pfFile, "\nxmminmax\n");
		for (int ii = 0; ii < 2 * i_M; ii++)
			for (int ij = 0; ij < i_S; ij++)
				fprintf(pfFile, "%g ", ppd_xmminmax[ii][ij]);

		fclose(pfFile);
		return true;
	}

	return false;
}

void CMscnProblem::vGenerateInstance(int iInstanceSeed) {
	CRandom random(iInstanceSeed);
	for (int i = 0; i < i_D; i++) {
		bSetSD(i, random.d_rand(MIN_SD, MAX_SD));
	}

	for (int i = 0; i < i_F; i++) {
		bSetSF(i, random.d_rand(MIN_SF, MAX_SF));
	}

	for (int i = 0; i < i_M; i++) {
		bSetSM(i, random.d_rand(MIN_SM, MAX_SM));
	}

	for (int i = 0; i < i_S; i++) {
		bSetSS(i, random.d_rand(MIN_SS, MAX_SS));
	}

	for (int i = 0; i < i_D; i++) {
		for (int j = 0; j < i_F; j++) {
			bSetCD(i, j, random.d_rand(MIN_CD, MAX_CD));
		}
	}

	for (int i = 0; i < i_F; i++) {
		for (int j = 0; j < i_M; j++) {
			bSetCF(i, j, random.d_rand(MIN_CF, MAX_CF));
		}
	}

	for (int i = 0; i < i_M; i++) {
		for (int j = 0; j < i_S; j++) {
			bSetCM(i, j, random.d_rand(MIN_CM, MAX_CM));
		}
	}

	for (int i = 0; i < i_D; i++) {
		bSetUD(i, random.d_rand(MIN_CD, MAX_CD));
	}

	for (int i = 0; i < i_F; i++) {
		bSetUF(i, random.d_rand(MIN_UF, MAX_UF));
	}

	for (int i = 0; i < i_M; i++) {
		bSetUM(i, random.d_rand(MIN_UM, MAX_UM));
	}

	for (int i = 0; i < i_S; i++) {
		bSetP(i, random.d_rand(MIN_P, MAX_P));
	}

	for (int i = 0; i < 2 * i_D; i += 2) {
		for (int j = 0; j < i_F; j++) {
			bSetXDMinMax(i, j, 0);
			bSetXDMinMax(i + 1, j, min(pd_sd[i / 2], pd_sf[j]));
		}
	}

	for (int i = 0; i < 2 * i_F; i += 2) {
		for (int j = 0; j < i_M; j++) {
			double d_d_to_f_max = 0;
			for (int k = 1; k < 2 * i_D; k += 2) {
				d_d_to_f_max += ppd_xdminmax[k][i / 2];
			}

			bSetXFMinMax(i, j, 0);
			double d_max_correct_val = min(pd_sf[i / 2], pd_sm[j]);
			bSetXFMinMax(i + 1, j, min(d_max_correct_val, d_d_to_f_max));
		}
	}

	for (int i = 0; i < 2 * i_M; i += 2) {
		for (int j = 0; j < i_S; j++) {
			double d_f_to_m_max = 0;
			for (int k = 1; k < 2 * i_F; k += 2) {
				d_f_to_m_max += ppd_xfminmax[k][i / 2];
			}

			bSetXMMinMax(i, j, 0);
			double d_max_correct_val = min(pd_sm[i / 2], pd_ss[j]);
			bSetXMMinMax(i + 1, j, min(d_max_correct_val, d_f_to_m_max));
		}
	}
}