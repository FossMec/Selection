#include <bits/stdc++.h>

using namespace std;

int main() {
    int x1;
    int v1;
    int x2;
    int v2;
    cin >> x1 >> v1 >> x2 >> v2;
    int c;
    int k1 = x1;
    int k2 = x2;
    if(x2>x1&&v2>v1)
        cout<<"NO";
    else
    {
        for(int i=0;i<10000;i++)
        {
            k1+=v1;
            k2+=v2;
            if(k1==k2)
            {
                c++;
                break;
            }
        }
    if(c!=0)
        cout<<"YES";
    else
        cout<<"NO";
    return 0;

    }
}    
