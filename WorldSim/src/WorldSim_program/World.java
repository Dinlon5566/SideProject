package WorldSim_program;

import WorldSim_member.LifeMember.Human;

public class World {

    public World(){

    }
    public void run(){

        Human a = new Human();
        Human b = new Human();
        a.lifeIntroduction();
        a.introduction();
        b.lifeIntroduction();
        b.introduction();

    }
}
