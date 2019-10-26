#include <string>

#define DEFAULT_SIZE 5
#define DEFAULT_NAME "Default"

using std::string;

class CTable {
public:
	CTable();
	CTable(string sName, int iTableLen);
	CTable(const CTable &pcOther);
	~CTable();
	void vSetName(string sName) { s_name = sName; };
	void vSetSize(int iSize) { i_table_size = iSize; };
	bool bSetNewSize(int iTableLen);
	int iGetSize() { return i_table_size; };
	string sGetName() { return s_name; };
	CTable* pcClone() { return new CTable(*this); };
	int* piGetTable() { return pi_table; };

private:
	string s_name;
	int i_table_size;
	int* pi_table;
};

void v_mod_tab(CTable* pcTab, int iNewSize);
void v_mod_tab(CTable cTab, int iNewSize);