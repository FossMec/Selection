#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, m, d, sum, count=0;
    cin>> n;
    int bar[n];
    for(int i=0; i<n; i++)
        cin>> bar[i];
    cin>> d >> m;
    for(int i=0; i<n-m+1; i++){
        sum = 0;
        for(int j=i; j<i+m; j++)
            sum += bar[j];
        if(sum == d)
            count++;
    }
    cout<< count;    
    
    return 0;
}
