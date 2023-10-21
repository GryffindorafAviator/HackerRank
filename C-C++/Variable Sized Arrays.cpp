#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    int q;
    
    cin >> n >> q;
    
    vector<vector<int>> nvec;
    
    for (int i = 0; i < n; i++) {
        int ni;
        cin >> ni;
        
        vector<int> ivec;
        
        for (int j = 0; j < ni; j++) {
            int item;
            cin >> item;
            
            ivec.push_back(item);
        } 
        
        nvec.push_back(ivec);
    }
    
    for (int k = 0; k < q; k++) {
        int r;
        int idx;
        
        cin >> r >> idx;
        
        cout << nvec[r][idx] << endl;
    }
    
    return 0;
}
