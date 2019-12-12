#pragma once
#define _CRT_SECURE_NO_WARNINGS
#include <string>

using std::string;

class CMxString
{
public:
	CMxString(string sText);
	CMxString(const CMxString & pcOther);
	CMxString(CMxString && pcOther);
	CMxString& operator=(const CMxString & pcOther);
	CMxString& operator=(CMxString && pcOther);
	string getString() { return string(pc_char); };

private:
	char* pc_char = NULL;
	int i_size = 0;
};