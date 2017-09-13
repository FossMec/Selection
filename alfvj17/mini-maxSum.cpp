#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long int s=0,min,max,s1,s2,i;
    long int A[5];
    for(i=0;i<5;++i)
    {
        cin>>A[i];
        s=s+A[i];
    }
    min=A[0];
    max=A[0];
    for(i=1;i<5;++i)
    {
        if(A[i]>max)
         max=A[i];
        else if(A[i]<min)
         min=A[i];   
    }
    s1=s-max;
    s2=s-min;
    cout<<s1<<" "<<s2;
    
    return 0;
}
