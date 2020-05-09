package polimorfizm.ad_hoc;

public class Addition {
    public int add(int a, int b) {
        return a + b;
    }

    // WE CAN OVERRIDE BY NUMBER OF PARAMETERS
    public int add(int a, int b, int c){
        return a+b+c;
    }

    // WE CAN OVERRIDE BY TYPE OF PARAMETERS
    public double add(double a, double b, double c){
        return a+b+c;
    }

    public double add(String msg, int a, int b) {
        System.out.println(msg);
        return a + b;
    }

    // BY CHANGING POSITION OF PARAMETERS
    public double add(int a, int b, String msg) {
        System.out.println(msg);
        return a + b;
    }
}
