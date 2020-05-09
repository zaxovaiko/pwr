#include "CMscnProblem.h"
#include "CRandomSearch.h"
#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

double * CRandomSearch::pd_find_best(int iSeed)
{
	CRandom c_gen(iSeed);
	bool b_is_success;
	string s_error_code;

	double* pd_best_solution = pd_random(c_gen);
	double d_best_quality = INT_MIN;

	if (pc_problem->bConstraintsSatisfied(pd_best_solution, s_error_code)) {
		d_best_quality = pc_problem->dGetQuality(pd_best_solution, b_is_success);
	}

	double d_current_quality;
	double* pd_current_solution = pd_random(c_gen);

	double * pd_find_max = new double;
	for (int i = 0; i < ITERATIONS; i++) {
		pd_current_solution = pd_random(c_gen);
		d_current_quality = pc_problem->dGetQuality(pd_current_solution, b_is_success);

		if (d_best_quality < d_current_quality && pc_problem->bConstraintsSatisfied(pd_current_solution, s_error_code)) {
			d_best_quality = d_current_quality;
			pd_best_solution = pd_current_solution;
			pd_find_max = &d_best_quality;
		}
	}

	cout << *pd_find_max;
	return pd_best_solution;
}

double * CRandomSearch::pd_random(CRandom & cGenerator)
{
	int i_solution_data_len = pc_problem->iGetD() * pc_problem->iGetF() + pc_problem->iGetF() * pc_problem->iGetM() + pc_problem->iGetM() * pc_problem->iGetS();
	double * pd_solution = new double[i_solution_data_len + INDEX_OF_FIRST_DATA_IN_SOLUTION];
	bool b_is_success = NULL;
	int i_counter = 0;

	pd_solution[i_counter++] = pc_problem->iGetD();
	pd_solution[i_counter++] = pc_problem->iGetF();
	pd_solution[i_counter++] = pc_problem->iGetM();
	pd_solution[i_counter++] = pc_problem->iGetS();

	for (double i = 0; i < i_solution_data_len; i++) {
		double d_min_val = pc_problem->dGetMin(&i, b_is_success);
		double d_max_val = pc_problem->dGetMax(&i, b_is_success);

		pd_solution[i_counter] = cGenerator.d_rand(d_min_val, d_max_val);
		i_counter++;
	}

	return pd_solution;
}