#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i,max,c=0;
    cin>>n;
    int A[n];
    for(i=0;i<n;++i)
     cin>>A[i];
    max=A[0];
    for(i=1;i<n;++i)
    {
        if(A[i]>max)
         max=A[i];   
    }    
    for(i=0;i<n;++i)
      if(A[i]==max)
       c++;
    cout<<c;
    return 0;
}
