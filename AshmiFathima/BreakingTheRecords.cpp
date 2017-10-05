#include <bits/stdc++.h>

using namespace std;

int main() 
{ 
     int n,highest,lowest;
     int x=0,y=0;
     cin >> n;
     int s[n];
    
     for(int i = 0; i < n; i++){
       cin >> s[i];
    }
     highest=lowest=s[0];
    
     for(int i=0;i<n;++i)
    {
         if (s[i] > highest)
        {
            highest = s[i];
            x++;
        }
         else if (s[i] < lowest)
        {
            lowest = s[i];
             y++;
          
        }
    }
    cout<<x<<" "<<y;
    cout<<endl;
    
}
