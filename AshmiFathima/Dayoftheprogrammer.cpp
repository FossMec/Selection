#include <bits/stdc++.h>

using namespace std;

int main() {
    int year;
    cin >> year;
    int daysFeb,date;
    if(year==1918)
        daysFeb=15;
    else if (year<1918)
    {   
        if(year%4==0)
            daysFeb=29;
        else
            daysFeb=28;
    }
    else
    {
        if((year%4==0 && year%100!=0)||year%400==0)
            daysFeb=29;
        else
            daysFeb=28;
    }
    date=256-daysFeb-215;
    cout<<date<<"."<<"09"<<"."<<year;
     
    
    return 0;
}
