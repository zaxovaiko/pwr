#pragma once
#include <iostream>

bool b_alloc_table_3_dim(char**** psTable, int iSize) {
	if (iSize < 0) {
		return false;
	}

	char*** ps_table = new char**[iSize];

	for (int ii = 0; ii < iSize; ii++)
	{
		ps_table[ii] = new char*[iSize];
		for (int ij = 0; ij < iSize; ij++)
		{
			ps_table[ii][ij] = new char[iSize];
		}
	}

	*psTable = ps_table;
	return true;
}

bool b_dealloc_table_3_dim(char*** psTable, int iSize) {
	if (iSize < 0) {
		return false;
	}

	for (int ii = 0; ii < iSize; ii++)
	{
		for (int ij = 0; ij < iSize; ij++)
		{
			delete[] psTable[ii][ij];
		}
		delete[] psTable[ii];
	}

	delete[] psTable;
	return true;
}

void v_alloc_table_add_5(int iSize) {
	if (iSize < 0) {
		return;
	}

	int* pi_array = new int[iSize];

	for (int offset = 0; offset < iSize; offset++)
	{
		pi_array[offset] = offset + 5;
		std::cout << pi_array[offset] << " ";
	}

	delete[] pi_array;
}

bool b_alloc_table_2_dim(int*** piTable, int iSizeX, int iSizeY) {
	if (iSizeX < 0 || iSizeY < 0) {
		return false;
	}

	int** pi_table = new int*[iSizeX];
	for (int ii = 0; ii < iSizeX; ii++)
	{
		pi_table[ii] = new int[iSizeY];
	}

	*piTable = pi_table;
	return true;
}

// Można usunąć iSizeY
bool b_dealloc_table_2_dim(int** piTable, int iSizeX, int iSizeY) {
	if (iSizeX < 0 || iSizeY < 0) {
		return false;
	}

	for (int ii = 0; ii < iSizeX; ii++)
	{
		delete[] piTable[ii];
	}

	delete[] piTable;
	return true;
}