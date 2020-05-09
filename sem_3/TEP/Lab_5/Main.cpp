#include <iostream>
#include "CTreeStatic.h"
#include "CTreeDynamic.h"

using namespace std;

void v_tree_test()
{
	CNodeStatic c_root;
	c_root.vAddNewChild();
	c_root.vAddNewChild();
	c_root.pcGetChild(0)->vSetValue(1);
	c_root.pcGetChild(1)->vSetValue(2);
	c_root.pcGetChild(0)->vAddNewChild();
	c_root.pcGetChild(0)->vAddNewChild();
	c_root.pcGetChild(0)->pcGetChild(0)->vSetValue(11);
	c_root.pcGetChild(0)->pcGetChild(1)->vSetValue(12);
	c_root.pcGetChild(1)->vAddNewChild();
	c_root.pcGetChild(1)->vAddNewChild();
	c_root.pcGetChild(1)->pcGetChild(0)->vSetValue(21);
	c_root.pcGetChild(1)->pcGetChild(1)->vSetValue(22);

	c_root.vPrintAllBelow();
	cout << endl;
	c_root.pcGetChild(0)->pcGetChild(1)->vPrintUp();
}

void v_tree_static() {
	CTreeStatic c_root;
	c_root.pcGetRoot()->vAddNewChild();
	c_root.pcGetRoot()->vAddNewChild();
	c_root.pcGetRoot()->pcGetChild(0)->vSetValue(1);
	c_root.pcGetRoot()->pcGetChild(1)->vSetValue(2);

	c_root.pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root.pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root.pcGetRoot()->pcGetChild(0)->pcGetChild(0)->vSetValue(11);
	c_root.pcGetRoot()->pcGetChild(0)->pcGetChild(1)->vSetValue(12);

	c_root.pcGetRoot()->pcGetChild(1)->vAddNewChild();
	c_root.pcGetRoot()->pcGetChild(1)->vAddNewChild();
	c_root.pcGetRoot()->pcGetChild(1)->pcGetChild(0)->vSetValue(21);
	c_root.pcGetRoot()->pcGetChild(1)->pcGetChild(1)->vSetValue(22);

	CTreeStatic c_root_1;
	c_root_1.pcGetRoot()->vAddNewChild();
	c_root_1.pcGetRoot()->vAddNewChild();
	c_root_1.pcGetRoot()->pcGetChild(0)->vSetValue(10);
	c_root_1.pcGetRoot()->pcGetChild(1)->vSetValue(20);

	c_root_1.pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root_1.pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root_1.pcGetRoot()->pcGetChild(0)->pcGetChild(0)->vSetValue(110);
	c_root_1.pcGetRoot()->pcGetChild(0)->pcGetChild(1)->vSetValue(120);

	c_root_1.pcGetRoot()->pcGetChild(1)->vAddNewChild();
	c_root_1.pcGetRoot()->pcGetChild(1)->vAddNewChild();
	c_root_1.pcGetRoot()->pcGetChild(1)->pcGetChild(0)->vSetValue(210);
	c_root_1.pcGetRoot()->pcGetChild(1)->pcGetChild(1)->vSetValue(220);

	c_root.bMoveSubtree(
		c_root.pcGetRoot()->pcGetChild(1)->pcGetChild(1),
		c_root_1.pcGetRoot()->pcGetChild(0)
	);

	cout << "c_root_1: ";
	c_root_1.pcGetRoot()->vPrintAllBelow();
	cout << endl;

	c_root.pcGetRoot()->vPrint(0);
}

void v_dynamic_tree_test() {
	CTreeDynamic* c_root = new CTreeDynamic;

	c_root->pcGetRoot()->vAddNewChild();
	c_root->pcGetRoot()->vAddNewChild();

	c_root->pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root->pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root->pcGetRoot()->pcGetChild(1)->vAddNewChild();
	c_root->pcGetRoot()->pcGetChild(1)->vAddNewChild();

	c_root->pcGetRoot()->pcGetChild(0)->vSetValue(1);
	c_root->pcGetRoot()->pcGetChild(1)->vSetValue(2);

	c_root->pcGetRoot()->pcGetChild(0)->pcGetChild(0)->vSetValue(11);
	c_root->pcGetRoot()->pcGetChild(0)->pcGetChild(1)->vSetValue(12);
	c_root->pcGetRoot()->pcGetChild(1)->pcGetChild(0)->vSetValue(21);
	c_root->pcGetRoot()->pcGetChild(1)->pcGetChild(1)->vSetValue(22);

	c_root->vPrintTree();

	CTreeDynamic* c_root_1 = new CTreeDynamic;

	c_root_1->pcGetRoot()->vAddNewChild();
	c_root_1->pcGetRoot()->vAddNewChild();

	c_root_1->pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root_1->pcGetRoot()->pcGetChild(0)->vAddNewChild();
	c_root_1->pcGetRoot()->pcGetChild(1)->vAddNewChild();
	c_root_1->pcGetRoot()->pcGetChild(1)->vAddNewChild();

	c_root_1->pcGetRoot()->pcGetChild(0)->vSetValue(10);
	c_root_1->pcGetRoot()->pcGetChild(1)->vSetValue(20);

	c_root_1->pcGetRoot()->pcGetChild(0)->pcGetChild(0)->vSetValue(110);
	c_root_1->pcGetRoot()->pcGetChild(0)->pcGetChild(1)->vSetValue(120);
	c_root_1->pcGetRoot()->pcGetChild(1)->pcGetChild(0)->vSetValue(210);
	c_root_1->pcGetRoot()->pcGetChild(1)->pcGetChild(1)->vSetValue(220);

	cout << endl;
	c_root_1->vPrintTree();

	c_root->bMoveSubtree(c_root->pcGetRoot()->pcGetChild(1)->pcGetChild(0), c_root_1->pcGetRoot()->pcGetChild(1));
	
	cout << endl << "New tree:" << endl;
	c_root->vPrintTree();

	cout << endl;
	c_root->pcGetRoot()->vPrint(0);

	delete c_root;
	delete c_root_1;
}

int main() {
	cout << endl << "CNodeStatic tree:" << endl;
	v_tree_test();

	cout << endl << endl << "CTreeStatic tree:" << endl;
	v_tree_static();

	cout << endl << endl << "CNodeDynamic tree:" << endl;
	v_dynamic_tree_test();

	cout << endl << endl;

	cin.get();
	return 0;
}