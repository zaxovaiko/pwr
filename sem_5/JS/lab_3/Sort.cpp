#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    vector<vector<string>> main;
    for (string line, col; getline(cin, line); ) {
        istringstream iss(line);
        vector<string> arr;

        while (getline(iss, col, '\t'))
            arr.push_back(col);

        main.push_back(arr);
    }

    // Bubble sort
    for (int i = 0; i < main.size() - 1; ++i) {
        for (int j = 0; j < main.size() - i - 1; ++j) {
            if (stoi(main[j][stoi(argv[1]) - 1]) < stoi(main[j + 1][stoi(argv[1]) - 1])) {
                vector<string> temp = main[j];
                main[j] = main[j + 1];
                main[j + 1] = temp;
            }
        }
    }

    // Print to use later
    for (auto & i : main) {
        for (auto & j : i)
            cout << j << "\t";
        cout << endl;
    }
}