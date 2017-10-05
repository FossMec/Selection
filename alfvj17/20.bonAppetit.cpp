#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long int n,k,i,c;
    double s;
    s=0;
    cin>>n>>k;
    double A[n];
    for(i=0;i<n;++i)
    {
        cin>>A[i];
        if(i!=k)
            s=s+A[i]/2;
    }
    cin>>c;
    if(s==c)
        cout<<"Bon Appetit";
    else
        cout<<c-s;
    return 0;
}
