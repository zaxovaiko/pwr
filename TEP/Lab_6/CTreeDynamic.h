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

private:
	CNodeDynamic<T>* pc_root;
};