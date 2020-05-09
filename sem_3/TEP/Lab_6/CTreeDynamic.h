#pragma once
#include "CNodeDynamic.h"

template <typename T>
class CTreeDynamic
{
public:
	CTreeDynamic();
	~CTreeDynamic();
	CNodeDynamic<T>* pcGetRoot() { return pc_root; };
	bool bMoveSubtree(CNodeDynamic<T> *pcParentNode, CNodeDynamic<T> *pcNewChildNode);
	void vPrintTree();
	void vGetMin(T * tMin);

private:
	CNodeDynamic<T>* pc_root;
};

template <typename T>
CTreeDynamic<T>::CTreeDynamic()
{
	pc_root = new CNodeDynamic<T>;
}

template <typename T>
CTreeDynamic<T>::~CTreeDynamic()
{
	delete pc_root;
}

template <typename T>
bool CTreeDynamic<T>::bMoveSubtree(CNodeDynamic<T>* pcParentNode, CNodeDynamic<T>* pcNewChildNode)
{
	if (pcParentNode == NULL) {
		return false;
	}

	if (pcNewChildNode != NULL) {
		pcNewChildNode->vDeleteFromChildren();
	}

	pcParentNode->vAddNewChild(pcNewChildNode);

	return true;
}

template <typename T>
void CTreeDynamic<T>::vPrintTree()
{
	pc_root->vPrintAllBelow();
}

template<typename T>
void CTreeDynamic<T>::vGetMin(T * tMin)
{
	if (tMin == NULL) {
		tMin = pc_root->tGetValue();
	}

	pc_root->vGetMin(tMin);
}