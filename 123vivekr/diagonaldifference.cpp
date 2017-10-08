#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
using namespace std;


int main() {
    int n;
    cin >> n;
    int a[n][n];
    for(int i = 0;i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
            cin>>a[i][j];
    }
    int s1 = 0, s2 = 0;
    for(int i = 0;i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
        {
            if(i == j)
                s1+=a[i][j];
            if(i+j == n - 1)
                s2+=a[i][j];
        }
    }
    cout<<abs(s1 - s2)<<endl;
    return 0;
}

