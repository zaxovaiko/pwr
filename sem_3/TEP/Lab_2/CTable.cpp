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

	// debug
	for (int i = 0; i < iTableLen; i++)
	{
		pi_table[i] = rand();
	}

	cout << endl;
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
	int* pi_temp_table = pi_table;
	pi_table = new int[i_table_len];

	for (int i = 0; i < i_table_len; i++)
	{
		pi_table[i] = pi_temp_table[i];
	}

	delete[] pi_temp_table;
	return true;
}

bool bAcc(CTable *pTabs) {
	int i_size = pTabs[0].iGetSize() + pTabs[1].iGetSize();
	int* pi_array = new int[i_size];

	int* p_farr = pTabs[0].piGetTable();
	for (int i = 0; i < pTabs[0].iGetSize(); i++)
	{
		cout << p_farr[i] << " ";
		pi_array[i] = p_farr[i];
	}

	int* p_sarr = pTabs[1].piGetTable();
	for (int i = pTabs[0].iGetSize(); i < i_size; i++)
	{
		pi_array[i] = pTabs[1].piGetTable()[i];
	}

	return true;
}

void v_mod_tab(CTable *pcTab, int iNewSize) {
	pcTab->bSetNewSize(iNewSize);
}

void v_mod_tab(CTable cTab, int iNewSize) {
	cTab.bSetNewSize(iNewSize);
}