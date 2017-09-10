//link to sub: https://www.hackerrank.com/challenges/diagonal-difference/submissions/code/53625250

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a[100][100], n, sum1=0, sum2=0, m;

    cin>>n;
    m=n-1;

    for(int i=0; i<n; ++i) {
        for(int j=0; j<n; ++j) {
            cin>>a[i][j];
            if(i==j)
                sum1+=a[i][j];
        }
        sum2+=a[i][m];
        --m;
    }

    int s = sum1 - sum2;

    if(s<0) {
        cout<<s*-1;
        return 0;
    }

    cout<<s;

    return 0;
}
