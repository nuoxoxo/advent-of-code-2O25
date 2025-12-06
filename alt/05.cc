#include "iostream"
#include "vector"
#include "utility"
#include "sstream"
using namespace std;
using ll = long long;
using pll = pair<ll,ll>;
int main(){
    vector<pll> ranges;
    vector<ll> N;
    string s,T;
    while (getline(cin,s)){
        T += s + "\n";
    }
    size_t spl = T.find("\n\n");
    string UP = T.substr(0,spl);
    string DOWN = T.substr(spl + 2);
    stringstream ss(UP);
    while (getline(ss, s)){
        long long l, r;
        char c;
        stringstream ss2(s);
        ss2 >> l >> c >> r;
        ranges.push_back({l,r});
    }
    stringstream ss3(DOWN);
    long long n;
    while (ss3 >> n)
        N.push_back(n);

    ll p1=0;
    for (ll n : N){
        for (auto &rg : ranges){
            auto [l,r] = rg;
            if (l<=n && n<=r){
                p1++;
                break ;
            }
        }
    }

    sort(ranges.begin(), ranges.end());
    ll L = ranges[0].first, R = ranges[0].second;
    ll p2 = R - L + 1;
    L = R;
    int i = 0;
    while (++i < ranges.size()){
        auto [l,r] = ranges[i];
        if (L < l){
            p2 += r-l+1;
            L = r;
        } else if (L < r) {
            p2 += r-L;
            L = r;
        }
    }
    cout << p1 << endl;
    cout << p2 << endl;
}
