#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i;
    cin>>n;
    int A[n];
    for(i=0;i<n;++i)
    {
        cin>>A[i];
        if(A[i]>=38)
            if(A[i]%5>2)
             A[i]+=(5-A[i]%5);
    }    
    for(i=0;i<n;++i)
        cout<<A[i]<<endl;
    return 0;
}
