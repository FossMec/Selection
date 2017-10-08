#include <cmath>

#include <iostream>


using namespace std;


int main(){
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        int x;
        int y;
        int z;
        cin >> x >> y >> z;
        if(abs(x-z)==abs(y-z))
            cout<<"Mouse C"<<endl;
        else if(abs(x-z)<abs(y-z))
            cout<<"Cat A"<<endl;
        else
            cout<<"Cat B"<<endl;
    }
    return 0;
}
