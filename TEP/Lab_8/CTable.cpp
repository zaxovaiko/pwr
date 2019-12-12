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

CTable::~CTable() {
	cout << "usuwam: '" << s_name << "'" << endl;
	delete[] pi_table;
}

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

CTable CTable::operator+(CTable& cOther) {
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

	return move(c_tab_res);
}

CTable::CTable(CTable && cOther) {
	pi_table = cOther.pi_table;
	i_table_len = cOther.i_table_len;

	cOther.pi_table = NULL;
	cOther.i_table_len = 0; // wt
	cout << "move" << endl;
}

CTable& CTable::operator=(CTable && cOther) {
	if (this != &cOther) {
		delete[] pi_table;

		pi_table = cOther.pi_table;
		i_table_len = cOther.i_table_len;

		cOther.pi_table = NULL;
		cOther.i_table_len = 0;
	}
	return *this;
}