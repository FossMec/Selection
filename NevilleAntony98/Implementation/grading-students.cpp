#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std; 

void grade(int n,int ar[]){
    int tmp, diff;
    for(int i =0; i<n; i++){
        if(ar[i] >= 38){
            tmp = ar[i] % 10;
            if(tmp < 5)
                diff = 5 - tmp;
            else if(tmp > 5)
                diff = 10 - tmp;
            else
                diff = 0;
            if(diff < 3)
                ar[i] = ar[i] + diff;   
        }
    }
    for(int i=0; i<n; i++)
        cout<< ar[i] << endl;
        
}


int main() {
    int n;
    cin>> n;
    int ar[n];
    for(int i=0; i<n; i++){
        cin>> ar[i];
    }
    grade(n,ar);        
    return 0;
}
