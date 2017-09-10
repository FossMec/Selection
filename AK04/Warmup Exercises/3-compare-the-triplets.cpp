// Link to sub: https://www.hackerrank.com/challenges/compare-the-triplets/submissions/code/53472645

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    int a[3], b[3], c=0, d=0;


    for(int i=0; i<3; ++i) {
        cin>>a[i];
    }

    for(int i=0; i<3; ++i) {
        cin>>b[i];
    }

    for(int i=0; i<3; ++i) {
        if(a[i] > b[i])
            c++;
        else if(a[i] < b[i])
            d++;
    }

    cout<<c<<" "<<d;

    return 0;
}
