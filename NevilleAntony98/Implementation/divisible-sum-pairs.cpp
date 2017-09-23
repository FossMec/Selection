#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, k, count=0;;
    cin>> n >> k;
    int ar[n];
    for(int i=0; i<n; i++)
        cin>> ar[i];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if( i < j && ((ar[i] + ar[j]) % k ==0) )
                count++;
        }
    }
    
    cout<< count;
    
    return 0;
}
