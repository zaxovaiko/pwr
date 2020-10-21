#include <iostream>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {
    for (string line; getline(cin, line);) {
        for (int i = 1; i < argc; ++i) {
            if (line.find(argv[i]) != string::npos) {
                cout << line << endl;
                break;
            }
        }
    }
}

