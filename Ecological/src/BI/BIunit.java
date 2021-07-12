package BI;

public class BIunit{
    String unitType;
    int hasFood;
    BIunit(String s){
        unitType=s;
    }
    void giveFood(int i){
        hasFood=i;
    }
    int eatFood(){
        int tmp=hasFood;
        hasFood=0;
        return tmp;
    }
}