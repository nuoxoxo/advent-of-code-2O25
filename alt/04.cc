#include "iostream"
#include "vector"
#include "set"
using namespace std;

int main(){
    string s;
    vector<string> G;
    while (cin >> s){
        G.push_back(s);
    }
    vector<vector<int>> D = {{-1,1},{1,-1},{-1,-1},{1,1},{-1,0},{0,1},{0,-1},{1,0}};
    int R=G.size(),C=G[0].size();
    int r = -1, c;
    int res1 = 0;
    while (++r < R){
        c = -1;
        while (++c < C){
            if (G[r][c] == '@'){
                int count = 0;
                for (auto& d: D){
                    int dr = d[0], dc = d[1];
                    int rr = r+dr, cc = c+dc;
                    if (rr<R && rr>-1 && cc<C && cc>-1 && G[rr][cc]=='@')
                        ++count;
                }
                res1 += count < 4;
            }
        }
    }
    set<vector<int>> S;
    bool mod = true;
    int res2 = 0;
    int it = 0;
    while (mod){
        mod = false;
        r = -1;
        ++it;
        cout << "it/" << it << endl;
        while (++r < R){
            c = -1;
            while (++c < C){
                if (S.find({r,c})==S.end() && G[r][c]=='@'){
                    int count = 0;
                    for (auto& d: D){
                        int dr = d[0], dc = d[1];
                        int rr = r+dr, cc = c+dc;
                        if (rr<R && rr>-1 && cc<C && cc>-1 && G[rr][cc]=='@'&&\
                            S.find({rr,cc})==S.end()){
                            ++count;
                        }
                    }
                    if (count < 4){
                        S.insert({r,c});
                        mod = true;
                    }
                }
            }
        }
    }
    cout << res1 << ' ' << S.size();
}
