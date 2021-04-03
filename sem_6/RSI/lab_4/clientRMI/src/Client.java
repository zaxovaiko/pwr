import java.rmi.Naming;

public class Client {

    public static void main(String[] args) {
	    double res;
	    CalcObject zObiekt;
	    CalcObject2 zObiekt2;
	    ResultType res2;
	    InputType inObj;

	    if (args.length == 0) {
            System.out.println("You have to enter RMI obj");
            return;
        }

	    String adres = args[0];
	    String adres2 = args[1];

	    try {
            zObiekt = (CalcObject) Naming.lookup(adres);
        }
	    catch (Exception e) {
            System.out.println("Nie mozna pobrac referencji do " + adres);
            e.printStackTrace();
            return;
        }

	    inObj = new InputType();
	    inObj.x1 = 100.2;
	    inObj.x2 = 200.1;
        inObj.operation = "add";

        try {
            zObiekt2 = (CalcObject2) Naming.lookup(adres2);
        }
        catch (Exception e) {
            System.out.println("Nie mozna pobrac referencji do " + adres2);
            e.printStackTrace();
            return;
        }

        System.out.println("Referencja do " + adres + " jest pobrana");
        System.out.println("Referencja do " + adres2 + " jest pobrana");

        try {
            res = zObiekt.calculate(1.1, 2.2);
        } catch (Exception e) {
            System.out.println("Blad zdalnego wywolania");
            e.printStackTrace();
            return;
        }

	    try {
            res2 = zObiekt2.calculate(inObj);
        } catch (Exception e) {
            System.out.println("Blad zdalnego wywolania");
            e.printStackTrace();
            return;
        }

        System.out.println("Wynik = " + res);
        System.out.println("Wynik2 = " + res2.result + ", " + res2.result_description);
    }
}
