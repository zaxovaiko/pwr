#include <iostream>

using namespace std;

int main(int argc, char* argv[], char* env[]) {
    cout << endl << "Program arguments: " << endl;
    for (int i = 0; i < argc; ++i) {
        cout << argv[i] << endl;
    }

    cout << endl << "Environment variables: " << endl;
    while (*env) {
        cout << *env++ << endl;
    }

    return 0;
}
