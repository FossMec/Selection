#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
     int a,b,c,i;
    char t[8];
    cin>>t;
    a=t[1]-'0';
    b=t[0]-'0';
    c=(b*10+a%10);
    if (t[8]=='A')
    {
        if(c==12)
        {
            cout<<"00";
            for(i=2;i<=7;i++)
                cout<<t[i];
        }
        else
        {
            for(i=0;i<=7;i++)
                cout<<t[i];
        }
    }
    else
    {
        if(c==12)
        {
            for(i=0;i<=7;i++)
                cout<<t[i];
        }
        else
        {
            c=c+12;
            cout<<c;
            for(int i=2;i<=7;i++)
                cout<<t[i];
        }
    }
    return 0;
}    
}    
