#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,m,i,j,k,max=0,min=101,x=0;
    cin>>n>>m;
    int A[n],B[m];
    for(i=0;i<n;++i)
    {
        cin>>A[i];
        if(A[i]>max)
            max=A[i];
    }
    for(i=0;i<m;++i)
    {
        cin>>B[i];
        if(B[i]<min)
            min=B[i];
    }
    for(i=max;i<=min;++i)
        for(j=0;j<n;++j)
        {
            if(i%A[j]!=0)
                break;
            else
                if(A[j]==A[n-1])
                    for(k=0;k<m;++k)
                    {
                        if(B[k]%i!=0)
                            break;
                        else
                            if(B[k]==B[m-1])
                                x++;        
                    }
        }
    cout<<x;
    return 0;
}
