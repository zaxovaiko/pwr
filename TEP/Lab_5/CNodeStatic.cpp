#include "CNodeStatic.h"

using std::endl;

CNodeStatic * CNodeStatic::pcGetChild(int iChildOffset)
{
	return (iChildOffset >= v_children.size() || iChildOffset < 0) 
		? NULL 
		: &v_children[iChildOffset];
}

void CNodeStatic::vAddNewChild()
{
	CNodeStatic c_child;
	c_child.pc_parent_node = this;

	v_children.push_back(c_child);
}

void CNodeStatic::vAddNewChild(CNodeStatic cOther)
{
	cOther.pc_parent_node = this;
	v_children.push_back(cOther);
}

void CNodeStatic::vPrintAllBelow()
{
	vPrint();

	for (int i = 0; i < v_children.size(); i++)
	{
		v_children[i].vPrintAllBelow();
	}
}

// Dla tej metody potrzebujemy tylko 
// wskaźnik pc_parent_node na rodzica
void CNodeStatic::vPrintUp()
{
	vPrint();

	 if (pc_parent_node != NULL) {
		pc_parent_node->vPrintUp();
	 }
}

void CNodeStatic::vPrint(int iLevel)
{
	for (int i = 0; i < iLevel - 1; i++)
	{
		cout << "|  ";
	}
	
	if (pc_parent_node != NULL) {
		cout << "|- " << i_val << endl;
	}
	else {
		cout << i_val << endl;
	}
	
	for (int i = 0; i < v_children.size(); i++)
	{
		v_children[i].vPrint(iLevel + 1);
	}
}

void CNodeStatic::vDeleteFromChildren()
{
	for (int i = 0; i < pc_parent_node->v_children.size(); i++)
	{
		if (&pc_parent_node->v_children[i] == this) {
			pc_parent_node->v_children.erase(this->pc_parent_node->v_children.begin() + i);
			return;
		}
	}
}
