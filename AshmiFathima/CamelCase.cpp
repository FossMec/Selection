
#include <iostream>

#include <string>

using namespace std;


int main(){
    string s;
    cin >> s;
    int len=s.length();
    int c,i;
    c=1;
    for(i=0;i<len;++i)
        if(isupper(s[i]))
            c++;
    cout<<c;
    return 0;
}
