#include <iostream>
#include "CFileLastError.h"
#include "CFileThrowEx.h"
#include "CFileErrCode.h"

using namespace std;

string sFilename = "output.txt";

void vOpenFileTenTimes(string sFilename) {
	CFileThrowEx c_file_throw_ex;
	try {
		for (int i = 0; i < 10; i++)
		{
			c_file_throw_ex.vOpenFile(sFilename);
		}
	}
	catch (int e) {
		cout << "error opening file 10 times with throwing exception: " << e << endl;
	}

	CFileLastError c_file_last_error;
	for (int i = 0; i < 10; i++)
	{
		if (c_file_last_error.bGetLastError()) {
			cout << "error opening file 10 times with last_error" << endl;
			i = 10;
		}

		c_file_last_error.vOpenFile(sFilename);
	}

	CFileErrCode c_file_err_code;
	for (int i = 0; i < 10; i++)
	{
		if (!c_file_err_code.bOpenFile(sFilename)) {
			cout << "error opening file 10 times with err_code" << endl;
			i = 10;
		}
	}
}

int main() {
	// Modification
	CFileThrowEx c_file;
	try {
		c_file = "modification.txt";
		c_file.vPrintLine("hello world");
		c_file.vCloseFile();

		cout << "written to modification.txt" << endl;
	}
	catch (int e) {
		cout << "error writing modification" << endl;
	}
	

	// Getting last error
	CFileLastError c_file_last_error;
	c_file_last_error.vOpenFile(sFilename);

	if (!c_file_last_error.bGetLastError()) {
		c_file_last_error.vPrintLine("hello -> c_file_last_error");
		cout << "ended writing c_file_last_error" << endl;
	}
	else {
		cout << "error opening c_file_last_error" << endl;
	}
	
	c_file_last_error.vCloseFile();

	// Throwing exceptino
	CFileThrowEx c_file_throw_ex;
	try {
		c_file_throw_ex.vOpenFile(sFilename);
		c_file_throw_ex.vPrintLine("hello -> c_file_throw_ex");
		cout << "ended writing c_file_throw_ex" << endl;
	}
	catch (int e) {
		cout << "error opening c_file_throw_ex: " << e << endl;
	}
	
	c_file_throw_ex.vCloseFile();

	// Returning bool
	CFileErrCode c_file_err_code;
	
	if (c_file_err_code.bOpenFile(sFilename)) {
		c_file_err_code.bPrintLine("hello -> c_file_err_code");
		cout << "ended writting c_file_err_code" << endl;
	}
	else {
		cout << "error opening c_file_err_code" << endl;
	}

	c_file_err_code.bCloseFile();

	// Custom func
	vOpenFileTenTimes(sFilename);

	cin.get();
	return 0;
}