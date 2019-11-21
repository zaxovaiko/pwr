#define _CRT_SECURE_NO_WARNINGS

#include "CFileThrowEx.h"
#include <iostream>

using namespace std;

CFileThrowEx::CFileThrowEx() { pf_file = NULL; }

CFileThrowEx::CFileThrowEx(string sFileName)
{
	vOpenFile(sFileName);
}

CFileThrowEx::~CFileThrowEx()
{
	if (pf_file != NULL) {
		fclose(pf_file);
	}
}

void CFileThrowEx::vOpenFile(string sFileName)
{
	if (pf_file != NULL) {
		throw 1;
	}

	pf_file = fopen(sFileName.c_str(), "a+");

	if (pf_file == NULL) {
		throw 1;
	}
}

void CFileThrowEx::vCloseFile()
{
	if (pf_file == NULL) {
		throw 1;
	}

	fclose(pf_file);
}

void CFileThrowEx::vPrintLine(string sText)
{
	if (pf_file == NULL) {
		throw 1;
	}

	fprintf(pf_file, "%s\n", sText.c_str());
}

void CFileThrowEx::vPrintManyLines(vector<string> sText)
{
	if (pf_file == NULL) {
		throw 1;
	}

	for (int i = 0; i < sText.size(); i++)
	{
		fprintf(pf_file, "%s\n", sText[i].c_str());
	}
}

CFileThrowEx& CFileThrowEx::operator=(const string & sFile)
{
	vOpenFile(sFile);
	return *this;
}