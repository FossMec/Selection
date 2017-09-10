//link to sub: https://www.hackerrank.com/challenges/time-conversion/submissions/code/54000169

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char t[10];
    int i, j, k, l;

    for(j=0; j<10;++j)
        cin>>t[j];

    k = t[0] - '0';
    l = t[1] - '0';
    i = 10*k + l;

    if(t[8]=='P') {
        if(i!=12)
            i+=12;
        cout<<i;
        for(j=2; j<8;++j)
            cout<<t[j];
    }
    else {
        if(i==12) {
            cout<<"00";
            for(j=2; j<8;++j)
                cout<<t[j];
            return 0;
        }
        for(j=0; j<8;++j)
            cout<<t[j];
    }
    return 0;
}
