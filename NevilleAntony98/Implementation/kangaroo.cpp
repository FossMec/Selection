#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int x1, v1, x2, v2, flag=0;
    cin>> x1 >> v1 >> x2 >> v2;
    int s1=x1, s2=x2;
    if( (v1 <= v2) )
        cout<<"NO";
    else{
        for(int i=0; i < 10000; i++){
            s1 += v1;
            s2 += v2;
            if(s1 == s2){
                cout<<"YES";
                flag = 1;
                break;
            }
        }
        if(flag == 0)
            cout<<"NO";
    }
        
        
    
    
    return 0;
}
