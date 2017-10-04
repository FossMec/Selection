
#include <iostream>

using namespace std;


int main(){
    int n;
    cin >> n;
    int a[n][n];
    int d1=0;
    int d2=0;
    
    for(int i=0;i<n;i++){
       for(int j = 0;j<n;j++){
          cin >> a[i][j];
          if(i==j)
              d1+=a[i][j];
          if(i+j==n-1)
              d2+=a[i][j];
       }
    }
    cout<<abs(d1-d2)<<endl;
    return 0;
}
