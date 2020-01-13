#include <iostream>
#include "CMSCNProblem.h"
#include "CSolution.h"

using namespace std;

int main() {
	int* err = new int;
	CMSCNProblem problem;

	CSolution csolution;
	csolution.vReadFile("solution.txt");

	problem.vReadFile("problem.txt");

	cout << problem.getQuality(csolution, err) << "\n";

	return 0;
}