#define _CRT_SECURE_NO_WARNINGS

#include "CFileErrCode.h"

CFileErrCode::CFileErrCode() { pf_file = NULL; }

CFileErrCode::CFileErrCode(string sFileName)
{
	bOpenFile(sFileName);
}

CFileErrCode::~CFileErrCode()
{
	if (pf_file != NULL) {
		fclose(pf_file);
	}
}

bool CFileErrCode::bOpenFile(string sFileName)
{
	if (pf_file != NULL) {
		return false;
	}

	pf_file = fopen(sFileName.c_str(), "a+");
	return true;
}

bool CFileErrCode::bCloseFile()
{
	if (pf_file == NULL) {
		return false;
	}

	fclose(pf_file);
	return true;
}

bool CFileErrCode::bPrintLine(string sText)
{
	if (pf_file == NULL) {
		return false;
	}

	fprintf(pf_file, "%s\n", sText.c_str());
	return true;
}

bool CFileErrCode::bPrintManyLines(vector<string> sText)
{
	if (pf_file == NULL) {
		return false;
	}

	for (int i = 0; i < sText.size(); i++)
	{
		fprintf(pf_file, "%s\n", sText[i].c_str());
	}

	return true;
}