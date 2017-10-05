#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int k,n,i,j,c=0;
    cin>>n>>k;
    int A[n];
    for(i=0;i<n;++i)
        cin>>A[i];
    for(i=0;i<n;++i)
    {
        for(j=i+1;j<n;++j)
            if((A[i]+A[j])%k==0)
                c++;
    }
    cout<<c;
    return 0;
}
