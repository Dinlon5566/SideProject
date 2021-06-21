package WorldSim_environment;

public class WSout {
    public int getPrint_count() {
        return Print_count;
    }

    private static int Print_count;

    public WSout() {
        int Print_count = 0;
    }

    public static void voidLineOut() {
        System.out.printf("ID%4d  [_]\n", Print_count);
        Print_count++;
    }

    public static void normalOut(String str) {
        System.out.printf("ID%4d  [*]%s\n", Print_count, str);
        Print_count++;
    }

    public static void systemOut(String str) {
        System.out.printf("ID%4d  [#]%s\n", Print_count, str);
        Print_count++;
    }

    public static void alertOut(String str) {
        System.out.printf("ID%4d  [!][!][!]%s\n", Print_count, str);
        Print_count++;
    }
}

