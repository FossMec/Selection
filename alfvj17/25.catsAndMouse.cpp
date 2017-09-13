#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int q,i,j,a,b;
    cin>>q;
    int A[q][3];
    for(i=0;i<q;++i)
        for(j=0;j<3;++j)
            cin>>A[i][j];
    for(i=0;i<q;++i)
        {
            if((A[i][0]-A[i][2])<0)
                a=-(A[i][0]-A[i][2]);
            else
                a=A[i][0]-A[i][2];
            if((A[i][1]-A[i][2])<0)
                b=-(A[i][1]-A[i][2]);
            else
                b=A[i][1]-A[i][2]; 
            if(a<b)
                cout<<"Cat A"<<endl;
            else if(b<a)
                cout<<"Cat B"<<endl;
            else
                cout<<"Mouse C"<<endl;
        
        }   
    
    return 0;
}
