#include <iostream>
#include <string>
#include "CTable.h"

using namespace std;

CTable::CTable() {
	vSetName(DEFAULT_NAME);
	vSetSize(DEFAULT_SIZE);
	pi_table = new int[DEFAULT_SIZE];

	cout << "bezp: '" << s_name << "'" << endl;
}

CTable::CTable(string sName, int iTableLen) {
	vSetName(sName);
	vSetSize(iTableLen);
	pi_table = new int[iTableLen];

	cout << "parametr: '" << s_name << "'" << endl;
}

CTable::CTable(const CTable &pcOther) : s_name(pcOther.s_name + "_copy"), i_table_len(pcOther.i_table_len) {
	pi_table = new int[pcOther.i_table_len];
	for (int i = 0; i < pcOther.i_table_len; i++)
	{
		pi_table[i] = pcOther.pi_table[i];
	}

	cout << "kopiuj: '" << s_name << "'" << endl;
}

//CTable::~CTable() {
//	cout << "usuwam: '" << s_name << "'" << endl;
//	cout << pi_table[0] << " ";
//	delete[] pi_table;
//}

bool CTable::bSetNewSize(int iTableLen) {
	if (iTableLen < 0) {
		return false;
	}

	i_table_len = iTableLen;
	int* pi_table_copy = pi_table;
	pi_table = new int[i_table_len];

	for (int i = 0; i < i_table_len; i++)
	{
		pi_table[i] = pi_table_copy[i];
	}

	delete[] pi_table_copy;
	return true;
}

void CTable::vSetValueAt(int iOffset, int iNewVal) {
	pi_table[iOffset] = iNewVal;
}

void CTable::vPrint() {
	for (int i = 0; i < i_table_len; i++)
	{
		cout << pi_table[i] << " ";
	}
	cout << endl;
}

CTable CTable::operator*(const CTable& cOther) {
	CTable c_res;

	// find size
	int i_count_same = 0;
	for (int i = 0; i < cOther.i_table_len; i++)
	{
		int j = 0;
		while (cOther.pi_table[i] != pi_table[j] || j < i_table_len) {
			j++;
		}

		i_count_same++;
	}

	// set new size for c_res
	c_res.bSetNewSize(i_count_same);

	// find exact values
	int i_counter = 0;
	for (int i = 0; i < cOther.i_table_len; i++)
	{
		int j = 0;
		while (cOther.pi_table[i] != pi_table[j] || j < i_table_len) {
			j++;
		}

		c_res.pi_table[i_counter] = pi_table[j];
		i_counter++;
		j = i_table_len;
	}

	// get unique
	int i_unique = 0;
	for (int i = 0; i < c_res.i_table_len; i++)
	{
		int j;
		for (j = 0; j < i; j++)
		{
			if (c_res.pi_table[i] == c_res.pi_table[j]) {
				j = i;
				// break;
			}
		}

		if (i == j) {
			i_unique++;
		}
	}

	// create copy array
	// get old values to new array
	int* p_arr = new int[i_unique];
	for (int i = 0, k = 0; i < c_res.i_table_len; i++)
	{
		int j;
		for (j = 0; j < i; j++)
		{
			if (c_res.pi_table[i] == c_res.pi_table[j]) {
				j = i;
				// break;
			}
		}

		if (i == j) {
			p_arr[k++] = c_res.pi_table[i];
		}
	}

	// rewrite to c_res
	c_res.bSetNewSize(i_unique);
	for (int i = 0; i < i_unique; i++)
	{
		c_res.pi_table[i] = p_arr[i];
	}

	return c_res;
}

CTable CTable::operator+(const CTable& cOther) {
	CTable c_tab_res;
	c_tab_res.bSetNewSize(cOther.i_table_len + i_table_len);

	for (int i = 0; i < i_table_len; i++)
	{
		c_tab_res.pi_table[i] = pi_table[i];
	}

	for (int i = i_table_len; i < cOther.i_table_len + i_table_len; i++)
	{
		c_tab_res.pi_table[i] = cOther.pi_table[i - i_table_len];
	}

	return c_tab_res;
}