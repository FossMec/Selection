#include <bits/stdc++.h>

using namespace std;

int main() {
    int a_triplet[3];
    int b_triplet[3];
    int alicepoints=0;
    int bobpoints=0;
    int i;
    for(i=0;i<3;++i)
        cin>>a_triplet[i];
    for(i=0;i<3;++i)
        cin>>b_triplet[i];
    for(i=0;i<3;++i)
    {
        if(a_triplet[i]>b_triplet[i])
            alicepoints++;
        if(a_triplet[i]<b_triplet[i])  
            bobpoints++;
    }
    cout<<alicepoints<<" "<<bobpoints;
    cout << endl;
    

    return 0;
}
