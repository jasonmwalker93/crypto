# include <iostream>
# include <fstream>
# include <vector>
# include <string>
using namespace std;

int main()
{
	ifstream rgen("rgen.txt");						// input random number file
	ifstream ct("ciphertext.txt");					// input ciphertext file
	ofstream pt("plaintext.txt");
	vector<char> vc;
	vector<int> vn;
	string decrypted;
	int in;
	char c;

	while(!rgen.eof())								// read random number file
	{												// and create vector containing numbers
		rgen >> in;
		vn.push_back(in);
	}
	vn.pop_back();

	while(!ct.eof())								// read ciphertext file
	{												// and create vector containg characters
		c = ct.get();
		vc.push_back(c);
	}
	vc.pop_back();

	if(vc.size() == vn.size())
		for(int a = 0; a < vn.size(); a++)			// for a number of iterations equal to ciphertext length
			decrypted += vc[a] ^ vn[a];				// perform XOR decryption with random numbers and write to string
	else
		cout << "Error: ciphertext and key lengths do not match." << endl;

	pt << decrypted;								// write decrypted to output file
	cout << "ciphertext decrypted: " << decrypted << endl;

	system("pause");
	return 0;
}