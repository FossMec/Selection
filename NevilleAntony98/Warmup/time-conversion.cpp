#include <bits/stdc++.h>

using namespace std;

void timeConversion(char t[]){
    int h = (t[0] - '0')*10 + t[1] - '0';
    if(t[8] == 'A'){
        if(h == 12){
            cout<< "00";
            for(int i=2; i<8; i++)
                cout<< t[i];
            
        }
        else
            for(int i=0; i<8; i++)
                cout<< t[i];
    }
    else{
        if(h != 12)
            h += 12;
        cout<< h;
        for(int i=2; i<8; i++)
            cout<< t[i];
    }
}
                   
        
          


int main() {
    char time[10];
    for(int i=0; i<10; i++)
        cin>> time[i];
    timeConversion(time);    
    return 0;
}
