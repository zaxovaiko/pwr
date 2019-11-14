#define _CRT_SECURE_NO_WARNINGS

#include "CFileThrowEx.h"

CFileThrowEx::CFileThrowEx() {}

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
		throw -1;
	}

	pf_file = fopen(sFileName.c_str(), "a+");
}

void CFileThrowEx::vCloseFile()
{
	if (pf_file == NULL) {
		throw -1;
	}

	fclose(pf_file);
}

void CFileThrowEx::vPrintLine(string sText)
{
	if (pf_file == NULL) {
		throw -1;
	}

	fprintf(pf_file, "%s\n", sText.c_str());
}

void CFileThrowEx::vPrintManyLines(vector<string> sText)
{
	if (pf_file == NULL) {
		throw -1;
	}

	for (int i = 0; i < sText.size(); i++)
	{
		fprintf(pf_file, "%s\n", sText[i].c_str());
	}
}