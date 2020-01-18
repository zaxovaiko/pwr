#include "CDiffEvol.h"
#include "CMscnProblem.h"
#include "CSolution.h"
#include "CRandomSearch.h"

using std::cout;
using std::endl;

double CDiffEvol::startDifferentialEvolution(int times)
{
	int* err = 0;
	CRandom rand;
	populationQuality = new double[populationNumber];

	initPopulation();

	for (int i = 0; i < populationNumber; i++) populationQuality[i] = 0;

	int i_counter = 0;
	while (i_counter < times)
	{
		for (int i = 0; i < populationNumber; i++)
		{
			/// Modification	
			// BEST INDEXES
			int baseInd = turney(rand.iRand(0, populationNumber));
			int addInd0 = turney(rand.iRand(0, populationNumber));
			int addInd1 = turney(rand.iRand(0, populationNumber));

			// NO NEED TO BE UNIQUE
			if (individualsAreDifferent(i, baseInd, addInd0, addInd1)) {
				int genotypeSize = problem->iSolutionSize();
				double *indNew = new double[genotypeSize];

				for (int geneOffSet = 0; geneOffSet < genotypeSize; geneOffSet++)
					if (rand.dRand(0, 1) < crossProbability)
						indNew[geneOffSet] = population[baseInd][geneOffSet] + differenceWeight * (population[addInd0][geneOffSet] - population[addInd1][geneOffSet]);			
					else 
						indNew[geneOffSet] = population[i][geneOffSet];

				fixGenotype(indNew);

				if (problem->constrainedSatisfied(indNew, err)) {
					double quality = problem->getQuality(indNew, err);
					cout.precision(10);
					cout << "Constrained satisfied! Quality: " << quality << endl;
					if (quality > populationQuality[i]) {
						delete[] population[i];
						population[i] = indNew;
						populationQuality[i] = quality;
					} else
						delete[] indNew;
				} else {
					cout << "Constrained not satisfied!" << endl;
					delete[] indNew;
				}
			}
		}
		i_counter++;
	}

	double best = 0;
	for (int i = 0; i < populationNumber; i++)
	{
		cout << i << ". Quality: " << populationQuality[i] << endl;
		if (best < populationQuality[i]) best = populationQuality[i];
	}
	return best;
}

void CDiffEvol::initPopulation()
{
	if (populationNumber < 0) return;
	
	CRandomSearch randomSearch(problem);

	population = new double * [populationNumber];
	for (int i = 0; i < populationNumber; i++)
	{
		population[i] = new double[problem->iSolutionSize()];
		randomSearch.setSeed(rand());

		double* pd_temp_table = randomSearch.nextValid();
		for (int j = 0; j < problem->iSolutionSize(); j++)
			population[i][j] = pd_temp_table[j];
		delete[] pd_temp_table;
	}
}

bool CDiffEvol::individualsAreDifferent(int first, int second, int third, int fourth)
{
	bool answer = true;
	if ((first == second || first == third || first == fourth) || (third == fourth) || (second == third || second == fourth)) answer = false;
	return answer;
}