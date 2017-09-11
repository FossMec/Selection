//link to sub: https://www.hackerrank.com/challenges/birthday-cake-candles/submissions/code/53997158

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    long n, i, x, c=0, l=0;    
    cin>>n;

    for(i=0; i<n; ++i) {
        cin>>x;
        if(x==l)
            c++;
        if(x>l) {
            c=1;
            l=x;
        }
    }

    cout<<c;
    return 0;
}
