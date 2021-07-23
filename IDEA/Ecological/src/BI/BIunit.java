package BI;

public class BIunit {

    int unitType;
    int hasFood;

    BIunit(int s) {
        unitType = s;
    }

    void giveFood(int i) {
        hasFood = i;
    }

    public int getUnitType() {
        return unitType;
    }

    public int getHasFood() {
        return hasFood;
    }


}