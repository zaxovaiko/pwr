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

CTable::CTable(const CTable &pcOther) : s_name(pcOther.s_name + "_copy"), i_table_size(pcOther.i_table_size) {
	pi_table = new int[pcOther.i_table_size];
	for (int i = 0; i < pcOther.i_table_size; i++)
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

	i_table_size = iTableLen;
	int* pi_temp_table = pi_table;
	pi_table = new int[i_table_size];

	for (int i = 0; i < i_table_size; i++)
	{
		pi_table[i] = pi_temp_table[i];
	}

	delete[] pi_temp_table;
	return true;
}

// TODO
bool bAcc(CTable **pTabs) {
	pTabs[0]->vSetSize(pTabs[0]->iGetSize() + pTabs[1]->iGetSize());

	for (int i = pTabs[0]->iGetSize(); i < pTabs[1]->iGetSize(); i++)
	{
		// write new elements to prev_array
	}

	return true;
}

void v_mod_tab(CTable *pcTab, int iNewSize) {
	pcTab->bSetNewSize(iNewSize);
}

void v_mod_tab(CTable cTab, int iNewSize) {
	cTab.bSetNewSize(iNewSize);
}