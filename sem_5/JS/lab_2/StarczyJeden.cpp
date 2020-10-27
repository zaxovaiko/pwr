#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream input("Zakup.txt");
    for (string line; getline(input, line);) {
        for (int i = 1; i < argc; ++i) {
            if (line.find(argv[i]) != string::npos) {
                cout << line << endl;
                break;
            }
        }
    }
}