#pragma once

#define ITERATIONS 10000

#include "CMscnProblem.h"
#include "CRandom.h"

class CRandomSearch
{
private:
	CMscnProblem * pc_problem;
	double* pd_random(CRandom &cGenerator);
public:
	CRandomSearch(CMscnProblem * cProblem) { pc_problem = cProblem; }
	double * pd_find_best(int iSeed);
};