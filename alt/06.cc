#include "iostream"
#include "vector"
#include "sstream"
using namespace std;
void p1(vector<string>);
void p2(vector<string>);

int main(){
    vector<string> LINES;
    string temp;
    while (getline(cin,temp))
        LINES.push_back(temp);

    p1(LINES);
    p2(LINES);
}

void p2(vector<string> LINES) {

    vector<string> A(LINES.begin(), LINES.end()-1);
 
    char chr;
    vector<char> ops;
    stringstream ss(LINES[LINES.size()-1]);
    while(ss >> chr)
        ops.push_back(chr);

    vector<long long> cal(ops.size());
    int i = -1;
    while (++i < ops.size())
        cal[i] = ops[i] == '*';

    int R = A.size(), C = A[0].size();
    vector<long long> COLS(C, 0);
    int r,c=-1;
    while (++c < C){
        r = -1;
        while (++r < R){
            if (A[r][c] != ' '){
                COLS[c] = COLS[c]*10 + A[r][c] - '0';
            }
        }
    }

    c = 0;
    i = -1;
    while (++i < ops.size()){
        if (ops[i] == '+'){
            while (c<C && COLS[c]){
                cal[i] += COLS[c];
                ++c;
            }
            if (c<C && ! COLS[c])
                ++c;
        }else{
            while (c<C && COLS[c]){
                cal[i] *= COLS[c];
                ++c;
            }
            if (c<C && ! COLS[c]){
                ++c;
            }
        }
    }
    long long res = 0;
    for (long long n : cal)
        res += n;
    cout << res << endl;
}

void p1(vector<string> LINES) {

    vector<char> ops;
    vector<vector<long long>> LLS;
    //while (cin >> temp)
    char c;
    stringstream ss(LINES[LINES.size()-1]);
    while(ss >> c)
        ops.push_back(c);
    int i = -1;
    while (++i < LINES.size()-1){
        stringstream ssn(LINES[i]);
        vector<long long> lls;
        long long n;
        while (ssn >> n)
            lls.push_back(n);
        LLS.push_back(lls);
    }

    long long res = 0;
    vector<long long> cal(ops.size());
    i = -1;
    while (++i < ops.size())
        cal[i] += ops[i] != '+';
    i = -1;
    while (++i < ops.size()){
        if (ops[i] == '+'){
            for (auto& ll : LLS)
                cal[i] += ll[i];
        }else{
            for (auto & ll : LLS)
                cal[i] *= ll[i]; 
        }
    }
    for (long long n : cal)
        res += n;
    cout << res << endl;
}

