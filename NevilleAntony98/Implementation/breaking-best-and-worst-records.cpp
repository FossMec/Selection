#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int max , min, maxrec=0, minrec=0;
    cin>> n;
    int score[n];
    for(int i=0; i<n; i++)
        cin>> score[i];
    max = score[0];
    min = score[0];
    for(int i=1; i<n; i++){
        if(score[i] > max){
            max = score[i];
            maxrec++;               
        }
        if(score[i] < min){
            min = score[i];
            minrec++;
        }
    }  
    cout<< maxrec << " " << minrec;         
    
    return 0;
}
