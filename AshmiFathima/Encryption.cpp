#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    string s;
    cin >> s;
    int len=s.length();
    int a=int(floor(sqrt(len)));
    int b=int(ceil(sqrt(len)));
    int r=0,c=0,row,col;
    for(row=a;row<=b;++row){
        for(col=row;col<=b;++col){
            if(row*col>=len ){
                r=row;
                c=col;
        }
    }
}
    for (int i=0;i<c;++i){
        for(int j=0;j<r;++j)
            if(j*c+i<len)
                cout<<s[j*c+i];
        cout<<" ";
            
        
    }
    cout<<endl;
    return 0;
}
