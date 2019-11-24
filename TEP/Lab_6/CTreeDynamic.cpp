#include "CTreeDynamic.h"
#include "CNodeDynamic.h"

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