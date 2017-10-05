
#include <iostream>


using namespace std;


int main(){
    int s;
    int t;
    cin >> s >> t;
    int a;
    int b;
    cin >> a >> b;
    int m;
    int n;
    cin >> m >> n;
    int applecount=0;
    int orangecount=0;
    int i,d;
    for(i=0;i<m;++i)
    {
        cin>>d;
        d+=a;
        if(d>=s && d<=t)
            applecount++;
    }
    for(i=0;i<n;++i)
    {
        cin>>d;
        d+=b;
        if(d>=s && d<=t)
            orangecount++;
    }
    cout<<applecount<<endl;
    cout<<orangecount<<endl;
    return 0;
}
