#include <bits/stdc++.h>

using namespace std;

int birthdayCakeCandles(int n, int ar[]) {
    int max=ar[0];
    int count = 0;
    for(int i=0; i < n; i++){
        if(ar[i] > max){
            max = ar[i];
        }
    }
    for(int i=0; i < n; i++){
        if(ar[i] == max)
            count++;
    }
    return count;
    
        
}

int main() {
    int n;
    cin >> n;
    int ar[n];
    for(int i = 0; i < n; i++){
       cin >> ar[i];
    }
    int result = birthdayCakeCandles(n, ar);
    cout << result << endl;
    return 0;
}
