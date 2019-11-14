#define _CRT_SECURE_NO_WARNINGS

#include "CFileLastError.h"
#include <cstdio>

bool CFileLastError::b_last_error = false;

CFileLastError::CFileLastError() { pf_file = NULL; }

CFileLastError::CFileLastError(string sFileName) {
	vOpenFile(sFileName);
}

CFileLastError::~CFileLastError() {
	if (pf_file != NULL) {
		fclose(pf_file);
	}
}

void CFileLastError::vOpenFile(string sFileName) {
	b_last_error = false;

	if (pf_file != NULL) {
		b_last_error = true;
		return;
	}

	pf_file = fopen(sFileName.c_str(), "a+");
}

void CFileLastError::vCloseFile() {
	b_last_error = false;

	if (pf_file == NULL) {
		b_last_error = true;
		return;
	}

	fclose(pf_file);
}

void CFileLastError::vPrintLine(string sText) {
	b_last_error = false;

	if (pf_file == NULL) {
		b_last_error = true;
		return;
	}

	fprintf(pf_file, "%s\n", sText.c_str());
}

void CFileLastError::vPrintManyLines(vector<string> sText) {
	b_last_error = false;

	if (pf_file == NULL) {
		b_last_error = true;
		return;
	}

	for (int i = 0; i < sText.size(); i++)
	{
		fprintf(pf_file, "%s\n", sText[i].c_str());
	}
}

// Don't Repeat Yourself xD