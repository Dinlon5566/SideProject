#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <math.h>
#include <windows.h>
using namespace std;

void initStr(string &str,string unit,int strlen){
    str="";
    for(int i=0;i<strlen;i++){
        str+=unit[i%unit.size()];
    }
}

void printStr(string str){
    for(int i=0;i<str.size();i++){
        cout<<((str[i]=='1')?"¡½":"¡¼");
    }
    cout<<endl;
}

string generation(string str,map<string,string> rule,int ruleLen){
    string res="";
    for(int i=0;i<str.size();i++){
        if(i<ruleLen/2){
            res+=str[i];
            continue;
        }
        if(str.size()-i<=ruleLen/2){
            res+=str[i];
            continue;
        }
        string clip(str.begin()+i-(ruleLen/2),str.begin()+i+(ruleLen/2+1));
        if(rule.count(clip)){
            res+=rule[clip];
        }else{
            res+=str[i];
        }
    }
    return res;
}

int main()
{
    int strlen,unitlen,ruleCount,maxPeriod,ruleLen;
    string str,unit;
    map<string,string> rule;

    cout<<"strLen :";
    cin>>strlen;

    cout<<"Unit (only 0 / 1):";
    cin>>unit;
    initStr(str,unit,strlen);
    printStr(str);

    cout<<"Len of rule :";
    cin>>ruleLen;
    cout<<"Count of rule :";
    cin>>ruleCount;

    for(int i=1;i<=ruleCount;i++){
        string ruleA,ruleB;
        cout<<"--- Rule "<<i<<" ---"<<endl;
        cout<<"After :"<<endl;
        cin>>ruleA;
        cout<<"Before :"<<endl;
        cin>>ruleB;
        rule.insert(pair<string,string>(ruleA,ruleB));
    }

    cout<<"Max Period :";
    cin>>maxPeriod;

    cout<<"--- Generation Start ---"<<endl;
    printStr(str);
    for(int i=0;i<maxPeriod;i++){
        string res=generation(str,rule,ruleLen);
       /*
        if(str==res){
            break;
        }*/
        str=res;
        printStr(str);
        Sleep(20);
    }
    cout<<"--- Generation End ---"<<endl;

    return 0;
}
