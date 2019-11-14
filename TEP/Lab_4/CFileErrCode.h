#pragma once
#include <string>
#include <vector>

using std::vector;
using std::string;

class CFileErrCode
{
public:
	CFileErrCode();
	CFileErrCode(string sFileName);
	~CFileErrCode();

	bool bOpenFile(string sFileName);
	bool bCloseFile(string sFileName);
	bool bPrintLine(string sText);
	bool bPrintManyLines(vector<string> sText);

private:
	FILE *pf_file = NULL;
};