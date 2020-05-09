#include <iostream>
#include "CMscnProblem.h"

using namespace std;

int main() {
	CMscnProblem c_issue;
	c_issue.bRead("issue.txt");

	double * d_sample_solution = new double[38];
	for (int i = 0; i < 38; i++) {
		d_sample_solution[i] = 1;
	}

	bool isSuccess = true;
	cout << endl<< "dGetQuality: " << c_issue.dGetQuality(d_sample_solution, isSuccess) << endl;
	cout << "bConstraintsSatisfied: " << c_issue.bConstraintsSatisfied(d_sample_solution) << endl;

	c_issue.bSaveObject("object.txt");
	c_issue.bSaveSolution("solution.txt");

	return 0;
}