#pragma once
#include <vector>
#include <iostream>

using std::vector;
using std::cout;

class CNodeStatic
{
public:
	CNodeStatic() { i_val = 0; pc_parent_node = NULL; };
	CNodeStatic *pcGetChild(int iChildOffset);
	
	int iGetChildrenNumber() { return v_children.size(); };
	void vSetValue(int iNewVal) { i_val = iNewVal; };
	void vAddNewChild();
	void vAddNewChild(CNodeStatic cOther);
	void vPrint() { cout << " " << i_val; };
	void vPrintAllBelow();
	void vPrintUp();
	void vPrint(int iLevel);
	void vDeleteFromChildren();

private:
	vector<CNodeStatic> v_children;
	CNodeStatic *pc_parent_node;
	int i_val;
};