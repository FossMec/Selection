#include <bits/stdc++.h>

using namespace std;

void solve(int a0, int a1, int a2, int b0, int b1, int b2){
    int r[2]={0,0};
    if(a0 > b0)
        r[0]+=1;
    else if(a0 < b0)
        r[1]+=1;
    if(a1 > b1)   
        r[0]+=1;
    else if(a1 < b1)
        r[1]+=1;
    if(a2 > b2)
        r[0]+=1;
    else if(a2 < b2)
        r[1]+=1;
    for (int i = 0; i < 2; i++)
        cout << r[i] << " ";
}

int main() {
    int a0;
    int a1;
    int a2;
    cin >> a0 >> a1 >> a2;
    int b0;
    int b1;
    int b2;
    cin >> b0 >> b1 >> b2;
    solve(a0, a1, a2, b0, b1, b2);
    cout << endl;
    return 0;
}
