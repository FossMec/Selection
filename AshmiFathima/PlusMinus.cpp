#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    float n,a,b,c;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
    for (int i=0;i<n;++i){
         if (arr[i]>0)
             a++;
         else if(arr[i]<0)
             b++;
         else if (arr[i]==0)
             c++;
    }
    cout<<a/n<<endl;
    cout<<b/n<<endl;
    cout<<c/n<<endl;

    return 0;
}
