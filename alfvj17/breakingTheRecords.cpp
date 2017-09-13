#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i,a=0,b=0,max,min;
    cin>>n;
    int A[n];
    for(i=0;i<n;++i)
        cin>>A[i];
    max=A[0];
    min=A[0];
    for(i=1;i<n;++i)
    {
        if(A[i]>max)
        {
            max=A[i];
            a++;
        }
        if(A[i]<min)
        {
            min=A[i];
            b++;
        }
    }
    cout<<a<<" "<<b;
    return 0;
}
