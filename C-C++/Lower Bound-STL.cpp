#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int num;
    vector<int> v;
    
    for (int i = 0; i < n; i++) {
        cin >> num;
        v.push_back(num);
    } 
    
    int nq;
    cin >> nq;
    
    int q;
    
    for (int j = 0; j < nq; j++) {
        cin >> q;
        
        std::vector<int>::iterator low;
        low = std::lower_bound(v.begin(), v.end(), q);
        
        if (v[low - v.begin()] == q) {
            cout << "Yes " << (low - v.begin() + 1) << endl;
        }
        else{
            cout <<"No " << (low - v.begin() + 1) << endl;
        }
    }
    
    return 0;
}
