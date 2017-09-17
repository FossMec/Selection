#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,m,d,i,j,s,c=0;
    cin>>n;
    int A[n],S[n];
    for(i=0;i<n;++i)
        cin>>A[i];
    cin>>m>>d;
    for(i=0;i<=n-d;++i)
    {
        S[i]=0;
        for(j=i;j<i+d;++j)
            S[i]+=A[j];
        if(S[i]==m)
            c++;
    }    
    cout<<c;        
    return 0;
}

