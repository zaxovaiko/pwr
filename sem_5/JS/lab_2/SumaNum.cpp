#include <iostream>
#include <sstream>

using namespace std;

int main() {
    double sum = 0;
    string str;
    while (getline(cin, str)) {
        double num;
        if ((istringstream(str) >> num >> ws).eof())
            sum += num;
    }
    cout << sum << endl;
}