#include "iostream"
#include "map"
#include "vector"
#include "sstream"
using namespace std;

int find(int);
void u(int, int);
vector<int> parents;

int main(){
    vector<vector<int>> coors;
    string s;
    while (cin >> s){
        char c;
        stringstream ss(s);
        int l,m,r;
        ss >> l >> c >> m >> c >> r;
        coors.push_back({l,m,r});
    }
    
    vector<vector<long long>> D;
    int N = coors.size();
    int i = -1,j;
    while (++i < N-1){
        j = i;
        while (++j < N){
            long long a,b,c,d;
            a = coors[i][0]-coors[j][0];
            b = coors[i][1]-coors[j][1];
            c = coors[i][2]-coors[j][2];
            d = a*a+b*b+c*c;
            D.push_back({d,i,j});
        }
    }
    sort(D.begin(),D.end());

   //vector<ll> parents;
    i = -1;
    while (++i < N)
        parents.push_back(i);

    int it = 0;
    for (auto & dij : D){
        i = dij[1], j = dij[2];
        u(i,j);
        bool allgood = true;
        int node = -1;
        while (++node < N){
            if (find(0) != find(node)){
                allgood = false;
                break ;
            }
        }
        if (allgood){
            cout << "p2/ " << (long long)coors[i][0]*(long long)coors[j][0] << endl;
            break ;
        }
        if (it == 999){
            vector<int> roots;
            map<int,int> M;
            node = -1;
            while (++node < N)
                roots.push_back( find(node) );
            for (int root : roots)
                M[root]++;
            vector<int> sorted;
            map<int,int>::iterator mit = M.begin();
            while (mit != M.end()){
                sorted.push_back(mit->second);
                ++mit;
            }
            sort(sorted.begin(), sorted.end(), std::greater<>());
            cout << "p1/ " << sorted[0]*sorted[1]*sorted[2] << endl;
        }
        ++it;
    }
}

int find(int node){

    int root = node;

    while (parents[ root ] != root){
        root = parents[ root ];
    }

    while (node != root){
        int parent = parents[node];
        parents[node] = root;
        node = parent;
    }
    return root;
}

void u(int L, int R){
    parents[find(L)] = find(R);
}


