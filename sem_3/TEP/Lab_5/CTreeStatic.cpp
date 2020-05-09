#include "CTreeStatic.h"
#include "CNodeStatic.h"

void CTreeStatic::vPrintTree()
{
	c_root.vPrintAllBelow();
}

bool CTreeStatic::bMoveSubtree(CNodeStatic * pcParentNode, CNodeStatic * pcNewChildNode)
{
	if (pcParentNode == NULL || pcNewChildNode == NULL) {
		return false;
	}

	pcParentNode->vAddNewChild(*pcNewChildNode);
	pcNewChildNode->vDeleteFromChildren();

	return true;
}