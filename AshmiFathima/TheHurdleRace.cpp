
#include <iostream>

using namespace std;


int main(){
    int n,k,i,max,a;
    cin >> n >> k;
    int height[100];
    for(i = 0;i < n;i++)
       cin >> height[i];
    max=height[0];
    for(i=0;i<n;++i)
        if(height[i]>max)
            max=height[i];
    a=max-k;
    if(a>0)
        cout<<a;
    else
        cout<<"0";
    
    return 0;
}
