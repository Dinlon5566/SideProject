package WorldSim_member.LifeMember;

import WorldSim_environment.*;

public class Human implements Life {

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getLifeType() {
        return lifeType;
    }

    static int humanCount = 0;
    private int id;
    private String name;
    private String sex;
    private String lifeType = "Human";

    public Human() {
        id = humanCount;
        name = "defult";
        sex = "N";
        humanCount++;
    }

    Human(String name) {
        id = humanCount;
        this.name = name;
        sex = "N";
        humanCount++;
    }

    Human(String name,String sex){
        id = humanCount;
        this.name = name;
        this.sex=sex;
        humanCount++;
    }

    Human(String name, String sex,String mode) {
        id = humanCount;
        this.name = name;
        sex = "N";
        humanCount++;
    }

    public void introduction() {
        WSout.voidLineOut();
        WSout.normalOut("Human Introduction:");
        WSout.normalOut("ID    : " + id);
        WSout.normalOut("Name  : " + name);
        WSout.normalOut("Sex   : " + sex);
    }

    @Override
    public void lifeIntroduction() {
        WSout.voidLineOut();
        WSout.normalOut("LIFE Introduction:");
        WSout.normalOut("Life Type : " + lifeType);
    }
}
