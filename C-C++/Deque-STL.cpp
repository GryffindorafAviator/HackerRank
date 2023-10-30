#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k) {
	deque<int> dq;
    int glbMax = 0;
    dq.push_back(0);
    
    for (int ki = 1; ki < k; ki++) {
        if (arr[ki] >= arr[glbMax]) {
            glbMax = ki; 
        }
        
        dq.push_back(ki);
    }
    
    cout << arr[glbMax] << " ";
    
    for (int i = k; i < n; i++) {
        if (arr[i] >= arr[glbMax]) {
            glbMax = i; 
        }
        else if (arr[dq.front()] == arr[glbMax]) {
            int start = dq.front() + 1;
            glbMax = start;

            for (int ki = start + 1; ki < start + k; ki++) {
                if (arr[ki] >= arr[glbMax]) {
                    glbMax = ki;
                }
            }
        }
        
        cout << arr[glbMax] << " ";
        dq.pop_front();
        dq.push_back(i);
    }
    
    cout << endl;
}

int main() {
	int t;
	cin >> t;
    
	while (t > 0) {
		int n, k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
        
    	for (i = 0; i < n; i++) {
            cin >> arr[i];
        }
      		
    	printKMax(arr, n, k);
    	t--;
  	}
      
  	return 0;
}
