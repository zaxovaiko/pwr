#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <sstream>

using namespace std;

int main() {
    fstream input("Covid.txt");

    auto t0 = chrono::high_resolution_clock::now();
    int sum = 0;
    for (string line, col; getline(input, line); ) {
        istringstream iss(line);
        vector<string> l;

        while (getline(iss, col, '\t'))
            l.push_back(col);

        try {
            sum += stoi(l[4]);
        } catch(...) {}
    }

    cout << sum << endl;
    auto t1 = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = t1 - t0;

    cout << elapsed.count() << endl;
    return 0;
}