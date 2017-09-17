#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    float positive=0, negative=0, zero=0;
    cin>> n;
    int ar[n];
    for(int i=0; i<n; i++)
        cin>> ar[i];
    for(int i=0; i<n; i++){
        if(ar[i] == 0)
            zero++;
        else if(ar[i] > 0)
            positive++;
        else 
            negative++;      
    }
    zero = zero/n;
    positive = positive/n;
    negative = negative/n;
    cout<< positive << endl << negative << endl << zero;
    return 0;
}
