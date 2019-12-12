#include <iostream>
#include "CMySmartPointer.h"

using namespace std;

void v_test(int* pi_a, int* pi_b) {
	CMySmartPointer<int> ps_a(pi_a);
	CMySmartPointer<int> ps_b(ps_a);

	cout << "pi_a = " << *ps_b.getT() << endl;
	
	CMySmartPointer<int> ps_c(pi_b);
	CMySmartPointer<int> ps_d(ps_c);

	// pointer d = b with operator=
	ps_d = ps_b;

	cout << "pi_d = " << *ps_d.getT() << endl;
}

void v_static_error() {
	int i = 5;
	CMySmartPointer<int> ps_stat(&i);
	cout << endl << *ps_stat.getT(); // <- error cuz we can not delete static vars
}

void v_another_test(int * pi_array) {
	CMySmartPointer<int> p(pi_array);
	p.vSetSize(3);

	try {
		cout << p.at(2) << endl;
	}
	catch (const exception &e) {
		cout << e.what() << endl;
	}
}

int main() {
	int* pi_a = new int(77);
	int* pi_b = new int(99);

	v_test(pi_a, pi_b);

	cout << "pi_a = " << *pi_a << endl;
	cout << "pi_b = " << *pi_b << endl;

	// Modification
	int * pi_array = new int[3];
	for (int i = 0; i < 3; i++)
	{
		pi_array[i] = i + 1;
	}

	v_another_test(pi_array);

	cin.get();
}