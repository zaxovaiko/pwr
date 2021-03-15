import java.net.URL;
import java.util.Scanner;
import java.util.Vector;

import org.apache.xmlrpc.XmlRpcClient;

public class Client {
    public static final String serverName = "server";

    public static void main(String[] args) {
	    try {
            Scanner sc = new Scanner(System.in);
            URL url = new URL("http", sc.next(), sc.nextInt(), "");
            XmlRpcClient srv = new XmlRpcClient(url);

            // Call server show method to get all available server's methods
            Object res = srv.execute(serverName + ".show", new Vector());
            System.out.println("Show method was executed.");

            // For each method in response call server method with random parameters
            for (Object method: (Vector) res) {
                Vector array = (Vector) method;

                String methodName = (String) array.elementAt(0);
                String description = (String) array.elementAt(1);
                String params = (String) array.elementAt(2);
                String returnType = (String) array.elementAt(3);

                Vector<Object> passedParams = new Vector<>();
                String[] paramsTypes = params.split(",");

                // For each type generate random value
                for (String type: paramsTypes) {
                    if (type.equals("int")) {
                        passedParams.addElement((int) (Math.random() * 20));
                    }
                    if (type.equals("string")) {
                        String str = "";
                        for (int i = 0; i < 5; i++) {
                            str += (char)(Math.random() * 26 + 65);
                        }
                        passedParams.addElement(str);
                    }
                    if (type.equals("boolean")) {
                        passedParams.addElement(Math.random() > 0.5);
                    }
                }
                System.out.println("Params: " + passedParams.toString());
                Object result = srv.execute(serverName + "." + methodName, passedParams);

                System.out.println("Name: \t\t" + methodName);
                System.out.println("Desc: \t\t" + description);
                System.out.println("Params: \t" + params);
                System.out.println("Return: \t" + returnType);
                System.out.println("Result: \t" + result.toString());
                System.out.println();
            }
        } catch (Exception exception) {
            System.err.println("Klient XML-RPC: " + exception);
        }
    }
}
