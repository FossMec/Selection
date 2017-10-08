#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long long int N,i,t,a,p,n;
    cin>>t;
    for(i=0;i<t;++i)
    {
        cin>>N;
        n=0;
        a=N;
        while(a!=0)
        {   
            p=a%10;
            if((p!=0)&&(N%p==0))
                n++;
            a=a/10;
        }
        cout<<n<<endl;
    }
    return 0;
}
