#include "iostream"
#include "vector"
#include "sstream"
#include "cassert"
using namespace std;

int main(){
    long long r1=0, r2=0;
    vector<string> lines;
    string s,T;
    getline(cin, T);
    stringstream ss(T);
    while (getline(ss,s,',')){
        lines.push_back(s);
    }
    for (auto& line : lines){
        size_t pos = line.find('-');
        if (pos == string::npos)
            continue ;
        //cout << line << " - " << pos <<  endl;
        long long L = stoll(line.substr(0,pos));
        long long R = stoll(line.substr(pos+1));
        long long n = L-1;
        while (++n < R+1){
            s = to_string(n);
            int l = s.size();
            if (l%2 == 0 && s.substr(0,l/2) == s.substr(l/2)){
                r1 += n;
            }
            int sublen = 0;
            while (++sublen < l/2+1){
                if (l%sublen)
                    continue ;
                string sub = s.substr(0,sublen);
                string subs;
                int i = -1;
                while (++i < l / sublen){
                    subs += sub;
                }
                if (s == subs){
                    r2 += n;
                    break ;
                }
            }
            //*/
        }
    }
    /*cout << r1 << endl;
    cout << r2 << endl;
    assert(r1 == 1227775554 || r1 == 55916882972);
    assert(r2 == 4174379265 || r2 == 76169125915);
    */
}
