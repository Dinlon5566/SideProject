package BI;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

public class BIfunction {

    List<Integer> typeCount=new ArrayList<>();
    List<BIunit> BIlist=new LinkedList<>();
    int food;

    BIfunction(List<Integer> typeCount,int food){
        this.food=food;
        this.typeCount.clear();
        this.typeCount=typeCount;
    }

    public void setTypeCount(List<Integer> typeCount) {
        this.typeCount.clear();
        this.typeCount = typeCount;
    }

    //build the world
    public void crater(){

    }


    //two BI fight
    static void twoUnitFood(BIunit a, BIunit b){
        if(a.getUnitType()==0||b.getUnitType()==0){
            a.hasFood=b.hasFood=4;
        }
        else if(a.getUnitType()==1&&b.getUnitType()==1){
            a.giveFood(2);
            b.giveFood(2);
        }else if(a.getUnitType()==2&&b.getUnitType()==2){
            a.giveFood(0);
            b.giveFood(0);
        }else{
            if(a.getUnitType()==1){
                a.giveFood(1);
                b.giveFood(3);
            }else{
                a.giveFood(3);
                b.giveFood(1);
            }
        }
    }

    int eatFood(BIunit bi){
        /*
        * 0->dead
        * 1->survive
        * 2->sire
        * */
        int rand=(int)Math.random()*10;
        switch (bi.getHasFood()){
            case 0:
            return 0;
            case  1:
                if(rand>4)
                    return 1;
                return 0;
            case 2:
                return 1;
            case 3:
                if(rand>4)
                    return 2;
                return 1;
            case 4:
                return 2;
        }
        return 0;
    }

}
