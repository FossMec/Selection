#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i;
    float a=0,b=0,c=0;
    cin>>n;
    int A[n];
    for(i=0;i<n;++i)
    {
        cin>>A[i];
        if(A[i]==0)
            c++;
        else if(A[i]>0)
            a++;
        else 
            b++;
    }
    a=a/n;
    b=b/n;
    c=c/n;
    cout<<a<<endl;
    cout<<b<<endl;
    cout<<c;
    return 0;
}
