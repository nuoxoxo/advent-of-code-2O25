#include "iostream"
#include "vector"
#include "sstream"
using namespace std;
using vvc = vector<vector<char>>;
using ll = long long;
void print(vvc);
void p1(vvc);
void p2(vvc);

int main(){
    vvc G;
    string temp;
    while (getline(cin,temp)){
        vector<char> g;
        for (char c: temp)
            g.push_back(c);
        G.push_back(g);
    }
    p1(G);
    p2(G);
}

void p2(vvc G){
    int R=G.size(),C=G[0].size();
    vector<vector<ll>> DP (R,vector<ll>(C,0));
    int c = -1;
    while (++c<C){
        DP[R-1][c]=1;
    }
    bool found = false;
    int SR=-1,SC=-1;
    int r = -1;
    while (++r < R){
        c=-1;
        while (++c<C){
            if (G[r][c] == 'S'){
                SR=r,SC=c,found=true;
                break ;
            }
        }
        if (found) break ;
    }
    r = R-1;
    while (--r>-1){
        c = -1;
        while (++c<C){
            ll temp = 0;
            if (G[r+1][c] ^ 'S' && G[r+1][c] ^ '^'){
                temp = DP[r+1][c];
            }else{
                ll left=0,right=0;
                if (c+1<C)
                    right = DP[r+1][c+1];
                if (c-1>-1)
                    left = DP[r+1][c-1];
                temp = left+right;
            }
            DP[r][c] = temp;
        }
    }
    ll res = DP[SR][SC];
    cout << res;
}

void p1(vvc G){
    int R=G.size(),C=G[0].size();
    int r = -1, c;
    while (++r < R){
        c = -1;
        while (++c < C){
            if (G[r][c] == '^'){
                if (c-1>-1){
                    int rr = r;
                    while (++rr < R){
                        if (G[rr][c-1] ^ '^')
                            G[rr][c-1] = '|';
                        else
                            break ;
                    }
                }
                if (c+1<C){
                    int rr = r;
                    while (++rr < R){
                        if (G[rr][c+1] ^ '^')
                            G[rr][c+1] = '|';
                        else
                            break ;
                    }
                }
            } else if (G[r][c] == 'S'){
                int rr = r;
                while (++rr < R){
                    if (G[rr][c] ^ '^')
                        G[rr][c] = '|';
                    else
                        break ;
                }
            }
        }
    }
    int res = 0;
    r=0;
    while (++r < R){
        c=-1;
        while (++c < C){
            if (G[r][c]=='^' && G[r-1][c]=='|')
                ++res;
        }
    }
    //print (G);
    cout << res << " ";
}

void print(vvc G){
    for (auto g : G){
        for (char c : g){
            cout << c;
        }
        cout << endl;
    }
}
