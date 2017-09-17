#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int i;
    int A[3],a=0;
    int B[3],b=0;
    for(i=0;i<3;++i)
    {
        cin>>A[i];
    }
    for(i=0;i<3;++i)
    {  
      cin>>B[i];  
      if(A[i]>B[i])
          a+=1;
      else if(A[i]<B[i])
          b+=1;
      else
      {
          a+=0;
          b+=0;
      }   
           
    }
    cout<<a<<" "<<b;
    return 0;
}
