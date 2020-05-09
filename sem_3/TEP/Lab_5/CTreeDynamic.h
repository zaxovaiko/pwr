#pragma once
#include "CNodeDynamic.h"

class CTreeDynamic
{
public:
	CTreeDynamic();
	~CTreeDynamic();
	CNodeDynamic* pcGetRoot() { return pc_root; };
	bool bMoveSubtree(CNodeDynamic *pcParentNode, CNodeDynamic *pcNewChildNode);
	void vPrintTree();

private:
	CNodeDynamic* pc_root;
};