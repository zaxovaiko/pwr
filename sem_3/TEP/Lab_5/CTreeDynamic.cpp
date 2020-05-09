#include "CTreeDynamic.h"
#include "CNodeDynamic.h"

CTreeDynamic::CTreeDynamic()
{
	pc_root = new CNodeDynamic;
}

CTreeDynamic::~CTreeDynamic()
{
	delete pc_root;
}

bool CTreeDynamic::bMoveSubtree(CNodeDynamic* pcParentNode, CNodeDynamic* pcNewChildNode)
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

void CTreeDynamic::vPrintTree()
{
	pc_root->vPrintAllBelow();
}