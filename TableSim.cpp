/*

EXPERIMENT GABUT KE-1 : { simulasi table }

    [ contoh ] :
            

             vertikal
    |------------------------|

           +>----+-----+-----+    --- 
           |  0  |  1  |  2  |     |
    +>-----+>----+-----+----<+     |
    |  0  || "a" | "b" | "c" |     |
    +>-----+>----+-----+----<+     |  horizontal
    |  1  || "b" | "c" | "a" |     | 
    +>-----+>----+-----+----<+     |
    |  2  || "c" | "a" | "b" |     |
    +>-----+>----+-----+----<+    ---

    pengertian kasus :
        jika vertikal = 0 & horizontal = 1 maka hasilnya "b"


*/
#include <iostream>
using namespace std;
class tableValues{
    public:
        string values[3][3]={
            {"a","b","c"},
            {"b","c","a"},
            {"c","a","b"}
        };string index[3]={"a","b","c"};
};
string logic(int v, int h){
    string out;
    tableValues tVal;
    if(v>2|h>2){
        cout<<"overlord"<<endl;
    }else{
        for(int index1=0;index1<3;index1++){
            for(int index2=0;index2<3;index2++){
                if((tVal.index[v]==tVal.index[index1])&&(tVal.index[h]==tVal.index[index2])){
                    out.append(tVal.values[index1][index2]);
                }
            }
        }return out;
    }
}
void automation_logic(){
    int Auto;Auto=0;
    while(Auto<3){
        cout<<"+------------------------+\n";
        for(int units=0;units<3;units++){
            cout<<"| table [ "<<Auto<<" ]"<<" [ "<<units<<" ] >> "+logic(Auto,units)+" |\n";
        }
        Auto++;
    }
}
int main(){
    system("clear");
    automation_logic();
    return 0;
}