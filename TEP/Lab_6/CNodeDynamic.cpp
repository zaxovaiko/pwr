#include "CNodeDynamic.h"

using std::endl;

template <typename T>
CNodeDynamic<T>::~CNodeDynamic()
{
	for (int i = 0; i < v_children.size(); i++)
	{
		delete v_children[i];
	}
}

template <typename T>
CNodeDynamic<T> * CNodeDynamic<T>::pcGetChild(int iChildOffset)
{
	return (this == NULL || iChildOffset < 0 || iChildOffset >= v_children.size())
		? NULL
		: v_children[iChildOffset];
}

template <typename T>
void CNodeDynamic<T>::vAddNewChild()
{
	if (this == NULL) {
		return;
	}

	CNodeDynamic<T> *c_child = new CNodeDynamic<T>;
	c_child->pc_parent_node = this;

	v_children.push_back(c_child);
}

template <typename T>
void CNodeDynamic<T>::vAddNewChild(CNodeDynamic * cChild)
{
	if (this == NULL) {
		return;
	}

	cChild->pc_parent_node = this;
	v_children.push_back(cChild);
}

template <typename T>
void CNodeDynamic<T>::vPrintAllBelow()
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

template <typename T>
void CNodeDynamic<T>::vPrint(int iLevel)
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

template <typename T>
void CNodeDynamic<T>::vDeleteFromChildren()
{
	for (int i = 0; i < this->pc_parent_node->v_children.size(); i++)
	{
		if (this->pc_parent_node->v_children[i] == this) {
			this->pc_parent_node->v_children.erase(this->pc_parent_node->v_children.begin() + i);
			return;
		}
	}
}