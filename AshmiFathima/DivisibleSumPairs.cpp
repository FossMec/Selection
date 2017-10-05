#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    int k;
    cin >> n >> k;
    int a[n];
    int i,j,c=0;
    for(i = 0; i < n; i++)
       cin >> a[i];
    for(i = 0; i < n; i++)
    {   
        for(j=i+1;j<n;j++)
            if((a[i] +a[j])%k==0)
                c++;
    }
    cout<<c<<endl;   
    return 0;
}
