import WorldSim_environment.*;
import WorldSim_member.LifeMember.Human;
import WorldSim_program.World;

public class Main {
    public static void main(String[] args) {
        WSout.systemOut("WorldSim Main program running.");

        World world = new World();
        world.run();

        WSout.systemOut("Main program finish.");
    }
}