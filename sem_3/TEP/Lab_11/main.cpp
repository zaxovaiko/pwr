#pragma once
#include <iostream>
#include "CMscnProblem.h"
#include "CDiffEvol.h"
#include "CSolution.h"
#include "CRandomSearch.h" 
#include "CProblem.h"

using namespace std;

int main()
{
	int* err = new int;
	CMscnProblem* problem = new CMscnProblem();
	CSolution csolution;
	csolution.vReadFile("solution.txt");
	(*problem).vReadFile("problem.txt");

	cout << "Quality: " << (*problem).getQuality(csolution, err) << endl;
	cout << "Constrained satisfied: " << (*problem).constrainedSatisfied(csolution, err) << endl;

	cout << "Quality: " << (*problem).getQualityIfNotGoodImprove(csolution) << endl;
	cout << "Constrained satisfied: " << (*problem).constrainedSatisfied(csolution, err) << endl;

	/// RandomSearch
	int times = 1000;
	CRandomSearch randomSearch(problem);
	randomSearch.randomSearch(times);

	/// DifferentialEvolution
	int times_diff = 100;
	int population = 100;
	double probability = 0.2;
	double weight = 0.01;

	CDiffEvol diff(problem, weight, probability, population);
	cout << "BEST SOLUTION IS: " << diff.startDifferentialEvolution(times_diff) << endl;
}