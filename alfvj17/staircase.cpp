#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i,j,k,a,b=1,c;
    cin>>n;
    c=n-1;
    for(i=0;i<n;++i)
    {
     a=c;
     for(j=0;j<a;++j)
      cout<<" ";
     for(k=0;k<b;++k)
      cout<<"#";
     --c;
     ++b;
     cout<<endl;   
    }    
    return 0;
}
