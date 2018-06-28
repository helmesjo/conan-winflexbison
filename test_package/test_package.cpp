#include <cstdio>
#include <iostream>
using namespace std;

extern "C" int yylex();
extern "C" int yyparse();
extern FILE *yyin;

int main(int, char**) {
    const auto file = "parseme.txt";
	// open a file handle to a particular file:
	FILE *myfile = fopen(file, "r");
	// make sure it is valid:
	if (!myfile) {
		cout << "I can't open " << file << "!" << endl;
		return -1;
	}
	// set flex to read from it instead of defaulting to STDIN:
	yyin = myfile;
	
	// parse through the input until there is no more:
	do {
		yyparse();
	} while (!feof(yyin));
	
    return EXIT_SUCCESS;
}