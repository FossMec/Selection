// link to sub: https://www.hackerrank.com/challenges/staircase/submissions/code/53932402

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin>>n;

    for(int i=1; i<=n; ++i) {

        for(int k=0; k<n-i; ++k)
            cout<<" ";
        for(int k=i; k>0; --k)
            cout<<"#";
        cout<<endl;
    }
    return 0;
}
