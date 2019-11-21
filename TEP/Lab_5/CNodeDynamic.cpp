#include "CNodeDynamic.h"

using std::endl;

CNodeDynamic::~CNodeDynamic()
{
	for (int i = 0; i < v_children.size(); i++)
	{
		delete v_children[i];
	}
}

CNodeDynamic * CNodeDynamic::pcGetChild(int iChildOffset)
{
	return (this == NULL || iChildOffset < 0 || iChildOffset >= v_children.size())
		? NULL
		: v_children[iChildOffset];
}

void CNodeDynamic::vAddNewChild()
{
	if (this == NULL) {
		return;
	}

	CNodeDynamic *c_child = new CNodeDynamic;
	c_child->pc_parent_node = this;

	v_children.push_back(c_child);
}

void CNodeDynamic::vAddNewChild(CNodeDynamic * cChild)
{
	if (this == NULL) {
		return;
	}

	cChild->pc_parent_node = this;
	v_children.push_back(cChild);
}

void CNodeDynamic::vPrintAllBelow()
{
	if (this == NULL) {
		return;
	}

	vPrint();

	for (int i = 0; i < v_children.size(); i++)
	{
		v_children[i]->vPrintAllBelow();
	}
}

void CNodeDynamic::vPrint(int iLevel)
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
		v_children[i]->vPrint(iLevel + 1);
	}
}

void CNodeDynamic::vDeleteFromChildren()
{
	for (int i = 0; i < this->pc_parent_node->v_children.size(); i++)
	{
		if (this->pc_parent_node->v_children[i] == this) {
			this->pc_parent_node->v_children.erase(this->pc_parent_node->v_children.begin() + i);
			return;
		}
	}
}
