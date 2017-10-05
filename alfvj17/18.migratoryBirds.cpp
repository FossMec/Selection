#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i,l,p=5;
    cin>>n;
    int A[n],B[5];
    for(i=0;i<5;++i)
        B[i]=0;
    for(i=0;i<n;++i)
    {
        cin>>A[i];
        if(A[i]==1)
            B[0]++;
        else if(A[i]==2)
            B[1]++;
        else if(A[i]==3)
            B[2]++;
        else if(A[i]==4)
            B[3]++;
        else
            B[4]++;
    }
    l=B[4];
    for(i=3;i>=0;--i)
    {
        if(B[i]>=l)
        {
            l=B[i];
            p=i+1;
        }    
    }
    cout<<p;
    return 0;
}
