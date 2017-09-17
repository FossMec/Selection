#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    long int sum=0;
    cin >> n;
    long int ar[n];
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    for(int ar_i =  0; ar_i < n; ar_i++){
        sum+=ar[ar_i];        
    }
    cout << sum << endl;
    return 0;
}
