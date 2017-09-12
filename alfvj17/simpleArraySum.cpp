#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N,i,s=0;
    cin>>N;
    int A[N];
    for(i=0;i<N;++i) 
    {
        cin>>A[i];
        s+=A[i];
    }   
    cout<<s;
    return 0;
}
