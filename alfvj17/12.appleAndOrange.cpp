#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int a,s,t,b,m,n,i,x=0,y=0;
    cin>>s>>t>>a>>b>>m>>n;
    int A[m],B[n];
    for(i=0;i<m;++i)
        cin>>A[i];
    for(i=0;i<n;++i)
        cin>>B[i];
    for(i=0;i<m;++i)
    {
        if(((a+A[i])>=s)&&((a+A[i])<=t))
            x++;
    }
    for(i=0;i<n;++i)
    {
        if(((b+B[i])>=s)&&((b+B[i])<=t))
            y++;
    }
    cout<<x<<endl;
    cout<<y;
    return 0;
}
