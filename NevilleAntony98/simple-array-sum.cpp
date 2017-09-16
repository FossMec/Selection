#include <bits/stdc++.h>

using namespace std;


int main() {
    int n,sum=0;
    cin >> n;
    int ar[n];
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
        sum=sum+ar[ar_i];
    }
    cout << sum << endl;
    return 0;
}
