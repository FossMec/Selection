#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int m, n, x, count=0, flag1=0, flag2=0;
    cin>> m >> n;
    int A[m], B[n];
    for(int i=0; i<m; i++)
        cin>> A[i];
    for(int i=0; i<n; i++)
        cin>> B[i];
    for(int i=A[0]; i <= B[n-1]; i++){
        x = i;
        flag1 = 0;
        flag2 = 0;
        for(int j=0; j<m; j++){
            if( x % A[j] !=0){
                flag1 = 1;
                break;
            } 
        }        
        for(int j=0; j<n; j++){
            if( B[j] % x != 0){
                flag2 = 1;
                break;
            }
        }
            
        if(flag1 == 0 && flag2 == 0)
            count++;
    }
    cout<< count;
    return 0;
}
