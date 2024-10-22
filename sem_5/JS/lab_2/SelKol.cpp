#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    for (string line, col; getline(cin, line); ) {
        istringstream iss(line);
        vector<string> product;

        while (getline(iss, col, '\t'))
            product.push_back(col);

        for (int i = 1; i < argc; ++i) {
            int index = stoi(argv[i]);
            cout << product[index - 1] << "\t";
            if (i == argc - 1) cout << endl;
        }
    }
}
