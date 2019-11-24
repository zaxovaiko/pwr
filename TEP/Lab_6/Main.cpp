#include <iostream>
#include "CTreeDynamic.h"
#include "CNodeDynamic.h"
#include "CTreeDynamic.cpp"
#include "CNodeDynamic.cpp"

using namespace std;

void v_nodes() {
	CNodeDynamic<int> * c_root = new CNodeDynamic<int>;
	c_root->vAddNewChild();
	c_root->pcGetChild(0)->vSetValue(9);

	c_root->vPrintAllBelow();
	cout << endl;

	delete c_root;
}

void v_tree() {
	CTreeDynamic<int> * c_root = new CTreeDynamic<int>;
	c_root->pcGetRoot()->vAddNewChild();
	c_root->pcGetRoot()->pcGetChild(0)->vSetValue(9);

	c_root->vPrintTree();

	delete c_root;
}

int main() {
	v_nodes();
	v_tree();

	cin.get();
}