#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,p;
    cin>>n>>p;
    if(p/2<(n/2-p/2))
        cout<<p/2;
    else
        cout<<(n/2-p/2);
    return 0;
}    
