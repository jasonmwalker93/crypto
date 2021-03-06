# include <iostream>
# include <random>
# include <fstream>
# include <vector>
using namespace std;

int main()
{
	int counter = 0;
	ifstream infile("plaintext.txt");			// input plaintext
	ofstream ofile("rgen.txt");
    random_device rd;							// ************************
    mt19937 gen(rd());							// random number generation
    uniform_int_distribution<> dist(1,26);		// ************************

	while(!infile.eof())						// counts number of character in plaintext file
	{
		infile.get();
		counter++;
	}

    for (int i = 0; i < counter-1; ++i) {		// for a number of iterations equal to the characters
        ofile << dist(gen) << " ";				// creates random number and write it to output file
		cout << "Random number: " << dist(gen) << " generated for character: " << i+1 << endl;
    }

	cout << "Number generation complete. Output file created." << endl;

	system("pause");
	return 0;
}