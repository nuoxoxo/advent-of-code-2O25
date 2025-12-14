#include "iostream"
#include "unordered_map"
#include "sstream"
#include "vector"
using namespace std;
using ll = long long;

unordered_map<string, vector<string>> D;
unordered_map<string, ll> memo;

ll p1(void);
ll p2(string,bool,bool);

int main(){
    string line;
    while (getline(cin, line)){//cin >> line){
        size_t idx = line.find(':');
        string l = line.substr(0,idx), r = line.substr(idx+1);
        stringstream ss(r);
        string word;
        while (ss >> word) D[l].push_back(word);
    }
    ll res = p1();
    ll res2 = p2("svr",false,false);
    cout << res << endl;
    cout << res2 << endl;
}

ll p2(string node, bool dac, bool fft){

    if ( node == "out" ){
        return dac && fft ? 1 : 0;
    }
    string k = node + ',' + (dac? '0': '1') + ',' + (fft? '0': '1');
    if ( memo.find(k) != memo.end() ){
        return memo[k];
    }
    ll curr = 0;
    for (string next : D[node]){
        curr += p2( next, dac || (next=="dac"), fft || (next=="fft") );
    }
    memo[k] = curr;
    return curr;
}

ll p1(){

    vector<pair<string,ll>> Q;
    Q.push_back({"you",1});
    ll res = 0;
    while (!Q.empty()){
        auto [ node, curr ] = Q.back();
        Q.pop_back();
        if (node == "out"){
            res += curr;
        } else {
            for (string next : D[node]){
                Q.push_back({next,curr});
            }
        }
    }
    return res;
}

