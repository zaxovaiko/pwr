#pragma once
#include <random>

class CRandom
{
public:
	CRandom(unsigned int iSeed) { gen.seed(iSeed); }
	double d_rand(double min, double max) { return std::uniform_real_distribution<double>{min, max}(gen); }
	int i_rand(int min, int max) { return std::uniform_int_distribution<int>{min, max}(gen); }

private:
	std::mt19937 gen = std::mt19937(0);
};