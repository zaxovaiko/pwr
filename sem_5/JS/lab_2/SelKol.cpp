#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream input( "../Zakup.txt" );

    for (string line; getline(input, line); ) {
        string s;
        istringstream iss(line);
        int j = 0;
        while (getline(iss, s, ' ')) {
            for (int i = 1; i < argc; ++i) {
                if (j == stoi(argv[i]) - 1) {
                    cout << s << "\t";
                }
            }
            j++;
        }
        cout << endl;
    }

    return 0;
}
