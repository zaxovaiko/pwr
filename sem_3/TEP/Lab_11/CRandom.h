#pragma once
#include <random>

using std::mt19937;
using std::uniform_int_distribution;
using std::uniform_real_distribution;

class CRandom
{
public:
	CRandom() { gen.seed(0); };
	CRandom(unsigned int iSeed) { gen.seed(iSeed); }
	double dRand(double dMin, double dMax) { return uniform_real_distribution<double>{dMin, dMax}(gen); }
	int iRand(int iMin, int iMax) { return uniform_int_distribution<int>{iMin, iMax}(gen); }

private:
	mt19937 gen = mt19937(0);
};