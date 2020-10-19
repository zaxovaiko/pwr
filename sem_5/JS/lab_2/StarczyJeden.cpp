#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream input( "../Zakup.txt" );

    for (string line; getline(input, line); ) {
        string s;
        istringstream iss(line);

        // code

        cout << endl;
    }

    return 0;
}

