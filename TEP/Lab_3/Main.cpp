#include <iostream>
#include "CTable.h"

using namespace std;

int main() {
	CTable c_tab_0, c_tab_1;
	c_tab_0.bSetNewSize(6);
	c_tab_1.bSetNewSize(4);

	for (int i = 0; i < c_tab_0.iGetTableLen(); c_tab_0.vSetValueAt(i++, i + 1));
	for (int i = 0; i < c_tab_1.iGetTableLen(); c_tab_1.vSetValueAt(i++, i + 51));

	c_tab_0 = c_tab_1;
	c_tab_1.vSetValueAt(2, 123);
	c_tab_0.vPrint();
	c_tab_1.vPrint();

	CTable c_tab_2;
	c_tab_2 = c_tab_0 + c_tab_1;
	c_tab_2.vPrint();

	CTable c_tab_a, c_tab_b;
	for (int i = 0; i < c_tab_a.iGetTableLen(); c_tab_a.vSetValueAt(i++, i));
	c_tab_b.vSetValueAt(0, 1);
	c_tab_b.vSetValueAt(1, 3);
	c_tab_b.vSetValueAt(2, 4);
	c_tab_b.vSetValueAt(3, 3);
	c_tab_b.vSetValueAt(4, 1);

	cout << "c_tab_a: ";
	c_tab_a.vPrint();

	cout << "c_tab_b: ";
	c_tab_b.vPrint();

	CTable c_tab_3;
	c_tab_3 = c_tab_a * c_tab_b;
	c_tab_3.vPrint();

	return 0;
}