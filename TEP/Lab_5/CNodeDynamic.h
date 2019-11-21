#pragma once
#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::cout;
using std::string;

class CNodeDynamic
{
public:
	CNodeDynamic() { i_val = 0; pc_parent_node = NULL; };
	~CNodeDynamic();
	CNodeDynamic *pcGetChild(int iChildOffset);
	
	void vSetValue(int iNewVal) { i_val = iNewVal; };
	int iGetChildrenNumber() { return v_children.size(); };
	void vAddNewChild();
	void vAddNewChild(CNodeDynamic* cChild);
	void vPrint() { cout << " " << i_val; };
	void vPrintAllBelow();
	void vPrint(int iLevel);
	void vDeleteFromChildren();

private:
	vector<CNodeDynamic*> v_children;
	CNodeDynamic *pc_parent_node;
	int i_val;
};