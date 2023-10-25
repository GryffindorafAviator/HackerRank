#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v;
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        int cur;
        cin >> cur;
        
        v.push_back(cur);
    }
    
    int rm1;
    cin >> rm1;
    
    v.erase(v.begin() + rm1 - 1);
    
    int rm2b;
    int rm2e;
    cin >> rm2b >> rm2e;
    
    v.erase(v.begin() + rm2b - 1, v.begin() + rm2e - 1);
    
    int len = v.size();
    cout << len << endl;
    
    for (int j = 0; j < len; j++) {
        cout << v[j] << ' ';
    }
       
    return 0;
}
