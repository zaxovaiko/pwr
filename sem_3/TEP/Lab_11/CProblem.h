#pragma once
#include "CRandom.h"
class CProblem {
public: 
	virtual double getQuality(double* pdSolution, int* err) = 0;
	virtual bool constrainedSatisfied(double* pdSolution, int* err) = 0;

	virtual void fixSolutionTable(double* pdSolution, int length)=0;
	virtual double* randomizeSolution(CRandom& rand) = 0;

	virtual int iSolutionSize() = 0;
};