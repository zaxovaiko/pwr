#include <iostream>
#include "CTable.h"
#include "CMxString.h"
#include <string>

using namespace std;

CTable cCreateTab()
{
	CTable c_result;
	c_result.bSetNewSize(5);
	return move(c_result);
}

int i_ms_test()
{
	CTable c_tab = cCreateTab();
	return 0;
}

int i_ignore_result()
{
	cCreateTab();
	return 0;
}

void v_test() {
	CTable c_tab("A", 3);
	CTable c_other("B", 5);

	for (int i = 0; i < 3; i++)
	{
		c_tab.vSetValueAt(i, i + 10);
	}

	for (int i = 0; i < 5; i++)
	{
		c_other.vSetValueAt(i, i + 50);
	}

	c_tab = move(c_other);
	c_tab.vPrint();
}

void v_test_operators() {
	CTable c_tab_0("A", 3);
	CTable c_tab_1("B", 5);
	CTable c_tab_2("C", 2);

	for (int i = 0; i < 3; i++)
	{
		c_tab_0.vSetValueAt(i, i + 10);
	}

	for (int i = 0; i < 5; i++)
	{
		c_tab_1.vSetValueAt(i, i + 50);
	}

	c_tab_2 = c_tab_0 + c_tab_1;
	c_tab_2.vPrint();

	c_tab_0.vPrint();
	c_tab_1.vPrint();
}

void v_modification() {
	CMxString c_str_0("hello");
	CMxString c_str_1("how are you?");

	CMxString c_str_2("custom text");
	CMxString c_str_3("default text");

	// with copy
	c_str_0 = c_str_1;
	cout << c_str_0.getString() << endl;
	
	// with move semantic
	c_str_2 = move(c_str_3);
	cout << c_str_2.getString() << endl;
}

int main() {
	i_ms_test();
	i_ignore_result();
	v_test();
	v_test_operators();
	v_modification();

	cin.get();
}