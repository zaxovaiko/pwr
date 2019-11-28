#include <iostream>
#include "CTreeDynamic.h"
#include <string>

using namespace std;

int main() {
	CTreeDynamic<int> * c_root_1 = new CTreeDynamic<int>;
	c_root_1->pcGetRoot()->vSetValue(10);
	c_root_1->pcGetRoot()->vAddNewChild();
	c_root_1->pcGetRoot()->vAddNewChild();

	c_root_1->pcGetRoot()->pcGetChild(0)->vSetValue(2);
	c_root_1->pcGetRoot()->pcGetChild(1)->vSetValue(3);

	c_root_1->pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root_1->pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root_1->pcGetRoot()->pcGetChild(0)->pcGetChild(0)->vSetValue(8);
	c_root_1->pcGetRoot()->pcGetChild(0)->pcGetChild(1)->vSetValue(0);

	c_root_1->pcGetRoot()->vPrint(0);

	int i_min = 10;
	c_root_1->vGetMin(&i_min);
	cout << i_min << endl;

	delete c_root_1;
	cin.get();
}