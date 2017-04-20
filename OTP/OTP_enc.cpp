# include <iostream>
# include <fstream>
# include <vector>
# include <string>
using namespace std;

int main()
{
	ifstream rgen("rgen.txt");						// input random numbers
	ifstream pt("plaintext.txt");					// input plaintext
	ofstream ct("ciphertext.txt");
	vector<int> vn;
	vector<char> vc;
	string encrypted;
	int in;
	char c;

	while(!rgen.eof())								// read random number file
	{												// and create vector containing numbers
		rgen >> in;
		vn.push_back(in);
	}
	vn.pop_back();

	while(!pt.eof())								// read plaintext file
	{												// and create vector contains characters
		c = pt.get();
		vc.push_back(c);
	}
	vc.pop_back();

	if (vc.size() == vn.size())
		for(int a = 0; a < vc.size(); a++)			// for a number of iterations equal to plaintext length
			encrypted += vc[a] ^ vn[a];				// perform XOR encryption with random numbers and write to string
	else
		cout << "Error: plaintext and key lengths do not match." << endl;

	ct << encrypted;								// write encrypted text to output file
	cout << "ciphertext created: " << encrypted << endl;

	system("pause");
	return 0;
}