#include <iostream>
#include "CTable.h"

using namespace std;

int main()
{
	/*cout << "-- Static initialization (bezp and params):" << endl;
	CTable tab_stat_def;
	CTable tab_stat_cus = CTable("test_stat", 25);

	cout << "\n-- Dynamic initialization (bezp and params):" << endl;
	CTable *p_tab_dyn_def = new CTable();
	CTable *p_tab_dyn_cus = new CTable("test_dyn", 20);

	cout << "\n-- Dynamic array initialization (bezp):" << endl;
	CTable *pc_new_tab_dyn = new CTable[3];

	cout << "\n-- v_mod_tab (not change):" << endl;
	v_mod_tab(tab_stat_def, 20);
	cout << tab_stat_def.iGetSize() << endl;

	cout << "\n-- v_mod_tab (change):" << endl;
	v_mod_tab(p_tab_dyn_def, 20);
	cout << p_tab_dyn_def->iGetSize() << endl;

	cout << "\n-- Cloning of p_tab_dyn_def instance:" << endl;
	CTable* p_tab_dyn_def_copy = p_tab_dyn_def->pcClone();

	cout << "\n-- Modifying cloned instances:" << endl;
	p_tab_dyn_def_copy->vSetName("dynamic_copy");
	p_tab_dyn_def_copy->vSetSize(25);

	cout << p_tab_dyn_def_copy->sGetName() << endl;
	cout << p_tab_dyn_def_copy->iGetSize() << endl;

	cout << "\n-- Removing instances:" << endl;

	delete p_tab_dyn_def;
	delete p_tab_dyn_cus;
	delete[] pc_new_tab_dyn;
	delete p_tab_dyn_def_copy;*/

	// Modification TODO
	CTable *p_tabs = new CTable[2];
	p_tabs[0] = CTable("A", 2);
	p_tabs[1] = CTable("B", 3);

	bAcc(p_tabs);

	for (int i = 0; i < p_tabs[0].iGetTableLen(); i++)
	{
		cout << p_tabs[0].piGetTable()[i] << " ";
	}

	cin.get();
	return 0;
}
