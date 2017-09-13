#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i;
    cin>>n;
    long int A[n],s=0;
    for(i=0;i<n;++i)
    {
        cin>>A[i];
        s+=A[i];
    }
    cout<<s;
    return 0;
}
