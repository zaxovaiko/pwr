#pragma once
#include "CRandomSearch.h"
#include "CMscnProblem.h"
#include "CSolution.h"
#include "CRandom.h"
#include "CProblem.h"

using std::cout;
using std::endl;

int CRandomSearch::randomSearch(int time)
{
	int bestQuality = 0;
	int counter = 0;
	int current = 0;
	double * solution = new double[problem->iSolutionSize()];

	CRandom rand;
	while (counter < time)
	{
		solution = problem->randomizeSolution(rand);
		current = problem->getQuality(solution, NULL);

		if (problem->constrainedSatisfied(solution, NULL))
			if (bestQuality < current) {
				bestQuality = current;
				cout << endl << counter << ". Now profit is: " << current << ", best SOL: " << bestQuality << endl << endl;
			}
			else cout << endl << counter << ". Now profit is: " << current << ", best SOL: " << bestQuality << endl << endl;
		else cout << counter << ". Now profit is: " << current << ", but SOL IS NOT correct, best SOL: " << bestQuality << endl;
		counter++;
	}

	cout << "THE BEST SOLUTION: " << bestQuality << endl;
	return bestQuality;
}

double* CRandomSearch::nextValid()
{
	CRandom rand(i_seed);
	double* pd_solution = new double[problem->iSolutionSize()];

	while (true)
	{
		pd_solution = problem->randomizeSolution(rand);
		if (problem->constrainedSatisfied(pd_solution, NULL))
			return pd_solution;
	}
}