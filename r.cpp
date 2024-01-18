#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    char x;
    cin>>s>>x;
    for(int i=0;i<s.size();i++){
        if(s[i]==x){
            cout<<i<<" ";
        }
    }
}