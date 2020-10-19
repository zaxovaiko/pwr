#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string str, s;
    char *p;
    int sum = 0;

    getline(cin, str);
    istringstream iss(str);

    while (getline(iss, s, ' ')) {
        strtol(s.c_str(), &p, 10);
        sum += *p == 0 ? stoi(s) : 0;
    }

    cout << sum << endl;
    return 0;
}
