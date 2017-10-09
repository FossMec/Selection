#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,p=0,i;
    cin>>n;
    int A[101],count[101]={0};
    for(i=0;i<n;i++) 
    {
        cin>>A[i];
        count[A[i]]++;
    }
    for(i=0;i<101;i++)
    {
        if(count[i]!=0)
            p+=count[i]/2;
    }
    cout<<p;
    return 0;
}
