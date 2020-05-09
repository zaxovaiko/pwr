#pragma once
#include <string>

#define DEFAULT_SIZE 5
#define DEFAULT_NAME "Default"

using std::string;

class CTable {
public:
	CTable();
	~CTable();
	CTable(string sName, int iTableLen);
	CTable(const CTable &pcOther);
	void vSetName(string sName) { s_name = sName; };
	void vSetSize(int iSize) { i_table_len = iSize; };
	int iGetTableLen() { return i_table_len; };
	bool bSetNewSize(int iTableLen);
	CTable* pcClone() { return new CTable(*this); };
	void vSetValueAt(int iOffset, int iNewVal);
	void vPrint();
	CTable operator+(CTable & cOther);
	CTable& operator=(CTable && cOther);
	CTable(CTable && cOther);

private:
	string s_name;
	int i_table_len;
	int* pi_table;
};