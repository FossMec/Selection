#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int main() {
    int i,n=1;
    char c[100000];
    cin>>c;
    int l=strlen(c);
    for(i=0;i<l;++i)
        if(isupper(c[i]))
            n+=1;
    cout<<n; 
    return 0;
}
