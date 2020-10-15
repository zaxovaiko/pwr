#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cstring>

using namespace std;

int main(int argc, char *argv[], char *env[]) {
    bool silent = argc > 1 && (!strcmp(argv[1], "/s") || !strcmp(argv[1], "/S"));

    cout << endl << "Environment variables: " << endl;
    for (int i = 1 + silent; i < argc; i++) {
        char **env_l = env;
        bool isUsed = false;

        while (*env_l) {
            vector<string> tokens;
            string token;
            istringstream tokensStream(*env_l);

            while (getline(tokensStream, token, '=')) {
                tokens.push_back(token);
            }

            if (tokens.at(0).find(argv[i]) != string::npos) {
                isUsed = true;
                cout << tokens.at(0) << endl << "=" << endl;

                vector<string> ts;
                string t;

                istringstream tokenStream(tokens.at(1));
                while (getline(tokenStream, t, ';')) {
                    ts.push_back(t);
                }

                for (auto &item : ts)
                    cout << item << endl;
                cout << endl;
            }
            env_l++;
        }

        if (!isUsed && !silent) {
            cout << argv[i] << " = NONE" << endl;
        }
    }

    return 0;
}