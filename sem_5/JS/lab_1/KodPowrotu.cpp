#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {
    bool silent = argc > 1 && (!strcmp(argv[1], "/s") || !strcmp(argv[1], "/S"));
    if (silent) argc--;

    int code = 0;
    if (argc == 1) code = 11;
    if (argc == 2) {
        char *s;
        code = strtol(argv[argc - !silent], &s, 10);
        if (*s) code = 12;
        else if (code < 0 || code > 9) code = 12;
    }

    if (argc > 2) code = 13;
    if (!silent) cout << "code: " << code << endl;
    return code;
}
