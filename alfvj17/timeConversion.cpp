#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    char t[8];
    cin>>t;
    int h1=(int)t[1]-'0';
    int h2=(int)t[0]-'0';
    int hh=(h2*10 + h1%10);
    if (t[8]=='A')
    {
        if (hh==12)
        {
            cout<<"00";
            for(int i=2;i<=7;i++)
                cout<<t[i];
        }
        else
        {
            for(int i=0;i<=7;i++)
                cout<<t[i];
        }
    }
    else
    {
        if(hh == 12)
        {
            for(int i=0;i<=7;i++)
                cout<<t[i];
        }
        else
        {
            hh=hh+12;
            cout<<hh;
            for(int i=2;i<=7;i++)
                cout<<t[i];
        }
    }
    return 0;
}    
