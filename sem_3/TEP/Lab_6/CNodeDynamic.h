#pragma once
#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::endl;

template <typename T>
class CNodeDynamic
{
public:
	CNodeDynamic() { t_val = 0; pc_parent_node = NULL; };
	~CNodeDynamic();
	CNodeDynamic *pcGetChild(int iChildOffset);
	void vSetValue(T tNewVal) { t_val = tNewVal; };
	T * tGetValue() { return &t_val; };
	int iGetChildrenNumber() { return v_children.size(); };
	void vAddNewChild();
	void vAddNewChild(CNodeDynamic *cChild);
	void vPrint() { cout << " " << t_val; };
	void vPrintAllBelow();
	void vPrint(int iLevel);
	void vDeleteFromChildren();
	void vGetMin(T * tMin);

private:
	vector<CNodeDynamic*> v_children;
	CNodeDynamic *pc_parent_node;
	T t_val;
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

	CNodeDynamic *c_child = new CNodeDynamic;
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
		cout << "|- " << t_val << endl;
	}
	else {
		cout << t_val << endl;
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

template<typename T>
void CNodeDynamic<T>::vGetMin(T * tMin)
{
	if (*tMin > t_val) {
		*tMin = t_val;
	}

	for (int i = 0; i < v_children.size(); i++)
	{
		v_children[i]->vGetMin(tMin);
	}
}