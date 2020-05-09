#pragma once
#include <string>
#include <vector>

using std::vector;
using std::string;

class CFileThrowEx
{
public:
	CFileThrowEx();
	CFileThrowEx(string sFileName);
	~CFileThrowEx();

	void vOpenFile(string sFileName);
	void vCloseFile();
	void vPrintLine(string sText);
	void vPrintManyLines(vector<string> sText);
	CFileThrowEx& operator=(const string& sFile);

private:
	FILE *pf_file;
};