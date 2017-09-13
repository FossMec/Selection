#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int i,j,n,s1=0,s2=0;
    cin>>n;
    int A[n][n];
    for(i=0;i<n;++i)
     for(j=0;j<n;++j)
         cin>>A[i][j];
    for(i=0;i<n;++i)   
     for(j=0;j<n;++j)
     {
         if(i==j)
          s1+=A[i][j];
         if((i+j)==(n-1))
          s2+=A[i][j];   
     }
    int sum=s1-s2;
    if(sum<0)
        sum=sum*(-1);
     cout<<sum;
    return 0;
}
