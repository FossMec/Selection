#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long int x1,x2,v1,v2,i,a,b,p=1;
    cin>>x1>>v1>>x2>>v2;
    a=x1;
    b=x2;
    for(i=0;i<10000;++i)
    {
        a+=v1;
        b+=v2;
        if(a==b)
        {
            cout<<"YES";
            p=-1;
            break;
        }
    }
    if(p==1)
        cout<<"NO";
    return 0;
}
