#include <iostream>
#include "CFileLastError.h"
#include "CFileThrowEx.h"
#include "CFileErrCode.h"

using namespace std;

string sFilename = "output.txt";

int main() {
	//
	//
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

	//
	//
	CFileThrowEx c_file_throw_ex;
	try {
		c_file_throw_ex.vOpenFile(sFilename);
		c_file_throw_ex.vPrintLine("hello -> c_file_throw_ex");
		cout << "ended writing c_file_throw_ex" << endl;
	}
	catch (int e) {
		cout << "error openning c_file_throw_ex: " << e << endl;
	}
	
	c_file_throw_ex.vCloseFile();

	//
	//
	CFileErrCode c_file_err_code;
	cout << c_file_err_code.bOpenFile(sFilename);
	cout << c_file_err_code.bPrintLine("hello -> c_file_err_code");
	cout << "ended writting to c_file_err_code" << endl;

	c_file_err_code.bCloseFile(sFilename);

	cin.get();
	return 0;
}