#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    int q;
    cin >> q;
    
    map<string, int> m;
    
    while (q > 0) {
        int type;
        string name;
        cin >> type >> name;
        
        if (type == 1) {
            int mark;
            cin >> mark;
            
            m[name] += mark;
        }
        else if (type == 2) {
            m.erase(name);
        }
        else {
            cout << m[name] << endl;
        }
        
        q--;
    }   
    
    return 0;
}



