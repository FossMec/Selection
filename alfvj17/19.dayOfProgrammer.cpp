#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin>>n;
    if(n==1918)
        cout<<"26.09."<<n;
    else if(n<=1917)
    {
        if(n%4==0)
            cout<<"12.09."<<n;
        else
            cout<<"13.09."<<n;
    }
    else
    {
        if(n%400==0)
            cout<<"12.09."<<n;
        else if((n%4==0)&&(n%100!=0))
            cout<<"12.09."<<n;
        else
            cout<<"13.09."<<n;
    }    
        
    return 0;
}
