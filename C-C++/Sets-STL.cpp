#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    int nq;
    cin >> nq;
    
    int x;
    int y;
    set<int> s;
    
    for (int i = 0; i < nq; i++) {
        cin >> y;
        cin >> x;
        
        if (y == 1) {
            s.insert(x);
        } 
        else if (y == 2) {
            set<int>::iterator itr2 = s.find(x);
            
            if (itr2 != s.end()) {
                s.erase(itr2);
            }
        }
        else {
            set<int>::iterator itr3 = s.find(x);
            
            if (itr3 != s.end()) {
                cout << "Yes" << endl;
            }
            else {
                cout << "No" << endl;
            }
        }
    }
    
    return 0;
}



