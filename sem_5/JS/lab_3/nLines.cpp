#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    string s;
    for (int i = stoi(argv[1]); getline(cin, s) && i > 0; --i) {
        cout << s << endl;
    }
}