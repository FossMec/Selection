#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    int sum1=0;
    int sum2 =0;
    cin>> n;
    int ar[n][n];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin>>ar[i][j];
        }
   }
    for (int i = 0; i<n; i++) {
      for (int j = 0; j<n; j++) {
         if (i == j)
            sum1 += ar[i][j];
         if((i + j )== (n-1))
            sum2 += ar[i][j];
      }
   }
    int result = fabs(sum1 - sum2);
    cout<< result << endl;    
    return 0;
}


