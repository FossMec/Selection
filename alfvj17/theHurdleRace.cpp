#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int i,n,k,x=0;
    cin>>n>>k;
    int A[n];
    for(i=0;i<n;++i)
    {
        cin>>A[i];
        if(A[i]>k)
        {
            x+=A[i]-k;
            k+=A[i]-k;
        }    
    }
    cout<<x;
    return 0;
}
