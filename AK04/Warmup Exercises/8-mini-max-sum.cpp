//link to sub: https://www.hackerrank.com/challenges/mini-max-sum/submissions/code/53995869

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    long a[5], s=0;
    int i, sm=0, la=0;

    for(i=0; i<5; ++i) {
        cin>>a[i];
        s+=a[i];
    }

    for(i=0; i<5; ++i) {
        if(a[i]>=a[la])
            la=i;
        if(a[i]<=a[sm])
            sm=i;
    }

    cout<<s-a[la]<<" "<<s-a[sm];

    return 0;
}
