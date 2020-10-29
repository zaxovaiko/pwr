#include <iostream>
#include <fstream>
#include <regex>

using namespace std;

int main(int argc, char *argv[]) {
    string text;
    ifstream input("./Nostromo.txt");
    getline(input, text, (char) input.eof());

    // remove \n
    text.erase(remove(text.begin(), text.end(), '\n'), text.end());

    regex rgx(argc == 2 ? R"([^.!?\s][^.!?]*(?:[.!?](?!['"]?\s|$)[^.!?]*)*[.!?]?['"]?(?=\s|$))" : "(\\w+)");
    regex_iterator<string::iterator> it(text.begin(), text.end(), rgx);
    regex_iterator<string::iterator> end;

    for (; it != end; ++it)
        cout << it->str() << endl;
}
