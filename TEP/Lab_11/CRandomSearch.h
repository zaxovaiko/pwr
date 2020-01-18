#pragma once
#include "CMscnProblem.h"
#include "CSolution.h"
#include "CRandom.h"
#include "CProblem.h"

class CRandomSearch {
public:
	CRandomSearch(CProblem* problem) { this->problem = problem; }
	
	void setSeed(int v) { i_seed = v; }
	void startOptimalization(int time) { randomSearch(time); }
	void setProblem(CProblem* problem) { if (this->problem == NULL) this->problem = problem; }
	
	double* nextValid();

	int randomSearch(int time);
	int iGetSeed() { return i_seed; }

private:
	int i_seed;
	CProblem* problem;
};