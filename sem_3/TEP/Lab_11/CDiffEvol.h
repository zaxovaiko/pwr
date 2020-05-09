#pragma once

#include "CMscnProblem.h"
#include "CSolution.h"
#include "CRandom.h"
#include "CRandomSearch.h"
#include "CProblem.h"

class CDiffEvol
{
public:
	CDiffEvol(CProblem* cproblem, double differenceWeight, double crossProbability, int populationNumber) {
		this->problem = cproblem;
		this->populationNumber = populationNumber;
		this->differenceWeight = differenceWeight; this->crossProbability = crossProbability;
	};
	double startDifferentialEvolution(int seconds);
	double* getPopulationQuality() { return populationQuality; }

	void startOptimalization(int times) { startDifferentialEvolution(times); }

	/// Modification
	int turney(int iSize) {
		double* INDIV_BEST = new double [problem->iSolutionSize()];
		int INDEX_BEST = 0;

		// FIND BEST
		int index = 0;
		for (int i = 0; i < iSize; i++)
		{
			if (INDEX_BEST < problem->getQuality(population[i], NULL) && problem->constrainedSatisfied(population[i], NULL)) {
				INDEX_BEST = problem->getQuality(population[i], NULL);
				index = i;
			}
		}
		return index;
	};

private:
	int populationNumber;

	double** population;
	double* populationQuality;
	double tablesSize;
	double crossProbability;
	double differenceWeight;

	void initPopulation();
	bool individualsAreDifferent(int first, int second, int third, int fourth);
	void fixGenotype(double* genotype) { problem->fixSolutionTable(genotype, NULL); }
	CProblem* problem;
};