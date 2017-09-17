#include <bits/stdc++.h>

using namespace std;

int main() {
    long int ar[5];
    long int tmp;
    for(int i = 0; i < 5; i++){
       cin >> ar[i];
    }
    for(int i=0; i<5 ; i++){
        for(int j=0; j<4-i; j++){
            if(ar[j] > ar[j+1]){
                tmp = ar[j];
                ar[j] = ar[j+1];
                ar[j+1] = tmp;  
            }
                
        }
    }
    long int minsum = ar[0] + ar[1] + ar[2] + ar[3];
    long int maxsum = ar[1] + ar[2] + ar[3] + ar[4];
    cout<< minsum << " " << maxsum;
    return 0;
}
