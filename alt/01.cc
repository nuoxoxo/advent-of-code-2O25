#include "iostream"
using namespace std;

int main() {
    int r1 = 0, i = 50;
    int r2 = 0, j = i;
    string line;
    while (cin >> line){
        char d = line[0];
        int n = stoi(line.substr(1));
        int lr = d == 'L' ? -1 : 1;
        i += n*lr;
        i %= 100;
        r1 += i==0;

        // p2
        int k = -1;
        while (++k < n){
            j += lr;
            j %= 100;
            r2 += j==0;
        }
    }
    cout << "res1/ " << r1 << endl;
    cout << "res2/ " << r2 << endl;
}
