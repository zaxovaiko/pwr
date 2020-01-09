#include <iostream>
#include <random>
#include <string>
#include "CMscnProblem.h"
#include "CRandomSearch.h"

using namespace std;

int main() {
	CMscnProblem c_issue;
	CRandomSearch c_search(&c_issue);

	c_issue.bSetD(1);
	c_issue.bSetF(2);
	c_issue.bSetM(1);
	c_issue.bSetS(4);

	double * d_sample_solution = new double[38];
	for (int i = 0; i < 38; i++) {
		d_sample_solution[i] = 1;
	}
/*
	cout << c_issue.iGetD() << endl;
	cout << c_issue.iGetF() << endl;
	cout << c_issue.iGetM() << endl;
	cout << c_issue.iGetS() << endl;*/

	c_issue.vGenerateInstance(3);

	string error = "";
	bool isSuccess = true;
	
	c_issue.dGetQuality(d_sample_solution, isSuccess);
	/*cout << "P = " << c_issue.dCalculateIncome() << endl;
	cout << "KT = " << c_issue.dCalculateTransportCost() << endl;
	cout << "KU = " << c_issue.dCalculateContractCost() << endl;*/

	cout << endl;
	for (int i = 0; i < 10; i++) {
		cout << "test #" << i << ": ";
		c_search.pd_find_best(i);
		cout << endl;
	}

	// cout << "dGetQuality: " << c_issue.dGetQuality(d_sample_solution, isSuccess) << endl;	

	c_issue.bSaveObject("object.txt");
	c_issue.bSaveSolution("solution.txt");

	return 0;
}