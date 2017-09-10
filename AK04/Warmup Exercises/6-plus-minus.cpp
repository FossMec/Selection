//link to sub: https://www.hackerrank.com/challenges/plus-minus/submissions/code/53929560

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    float a=0, b=0, c=0, n, x, ap, bp, cp;

    cin>>n;

    for(int i=0; i<n; ++i) {
        cin>>x;
        if(x>0)
            ++a;
        else if(x<0)
            ++b;
        else
            ++c;
    }

    ap=float(a/n);
    bp=float(b/n);
    cp=float(c/n);

    cout<<std::fixed;
    cout<<std::setprecision(6);

    cout<<ap<<endl<<bp<<endl<<cp;

    return 0;
}
