#pragma once
#include "CNodeStatic.h"

class CTreeStatic
{
public:
	CNodeStatic *pcGetRoot() { return &c_root; }
	void vPrintTree();
	bool bMoveSubtree(CNodeStatic* pcParentNode, CNodeStatic* pcNewChildNode);

private:
	CNodeStatic c_root;
};