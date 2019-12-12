#include "CMxString.h"
#include <iostream>

#define _CRT_SECURE_NO_WARNINGS

using namespace std;

CMxString::CMxString(string sText)
{
	i_size = sText.length();
	pc_char = new char[i_size];
	strcpy(pc_char, sText.c_str());
}

CMxString::CMxString(const CMxString & pcOther)
{
	i_size = pcOther.i_size;
	pc_char = new char[i_size];
	strcpy(pc_char, pcOther.pc_char);
}

CMxString::CMxString(CMxString && pcOther)
{
	i_size = pcOther.i_size;
	pc_char = pcOther.pc_char;
	pcOther.pc_char = NULL;
}

CMxString & CMxString::operator=(const CMxString & pcOther)
{
	i_size = pcOther.i_size;
	pc_char = new char[i_size];
	strcpy(pc_char, pcOther.pc_char);
	return *this;
}

CMxString & CMxString::operator=(CMxString && pcOther)
{
	if (this != &pcOther) {
		pc_char = pcOther.pc_char;
		i_size = pcOther.i_size;
		pcOther.pc_char = NULL;
		i_size = 0;
	}

	return *this;
}