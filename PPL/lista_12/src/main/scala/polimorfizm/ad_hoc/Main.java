package polimorfizm.ad_hoc;

public class Main {
    public static void main(String[] args) {
        Addition ob = new Addition();
        System.out.println("sum of the 2 int values: " + ob.add(1, 2));
        System.out.println("sum of the 3 int values: " + ob.add(1,2,3));
        System.out.println("sum of the 3 double values: " + ob.add(1.1,2.0,3.3));
        System.out.println("sum of the 2 int values with msg: " + ob.add("Add two ints", 4, 8));
        System.out.println("sum of the 2 int values with msg: " + ob.add(14, 8, "Add two ints at the end"));
    }
}
