#pragma once
#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::cout;
using std::endl;
using std::string;

template <typename T>
class CNodeDynamic
{
public:
	CNodeDynamic() { i_val = 0; pc_parent_node = NULL; };
	~CNodeDynamic();
	CNodeDynamic<T> *pcGetChild(int iChildOffset);

	void vSetValue(int iNewVal) { i_val = iNewVal; };
	int iGetChildrenNumber() { return v_children.size(); };
	void vAddNewChild();
	void vAddNewChild(CNodeDynamic<T>* cChild);
	void vPrint() { cout << " " << i_val; };
	void vPrintAllBelow();
	void vPrint(int iLevel);
	void vDeleteFromChildren();

private:
	vector<CNodeDynamic*> v_children;
	CNodeDynamic *pc_parent_node;
	T i_val;
};

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