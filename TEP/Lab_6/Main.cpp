#include <iostream>
#include "CTreeDynamic.h"

using namespace std;

int main() {
	CTreeDynamic<int> * c_root = new CTreeDynamic<int>;
	c_root->pcGetRoot()->vAddNewChild();
	c_root->pcGetRoot()->pcGetChild(0)->vSetValue(9);

	c_root->vPrintTree();

	delete c_root;

	cin.get();
}