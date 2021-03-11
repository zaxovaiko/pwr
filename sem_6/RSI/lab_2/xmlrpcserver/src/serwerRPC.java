import java.util.ArrayList;

import org.apache.xmlrpc.WebServer;

public class serwerRPC {
    public static void main(String[] args) {
        int PORT = 10000;
        try {
            WebServer server = new WebServer(PORT);

            server.addHandler("MojSerwer", new serwerRPC());
            server.start();

            System.out.println("Server listening on port " + PORT);
        } catch (Exception exception) {
            System.err.println("Serwer XML-RPC: " + exception);
        }
    }

    /**
     * 
     * @param x Timeout in ms
     * @return  123
     */
    public int execAsy(int x) {
        try {
            Thread.sleep(x);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
            Thread.currentThread().interrupt();
        }
        return 123;
    }

    /**
     * Returns rounded number is flag was set.
     * Else returns not rounded number.
     * 
     * @param x     Number to calculate
     * @param pow   Power of number
     * @param flag  Flag to round number of not
     * @return      Number with floated point
     */
    public double pow(int x, int pow, boolean flag) {
        double num = Math.pow(x, pow);
        return flag ? Math.floor(num) : num;
    }

    /**
     * Repeats string n times.
     * 
     * @param str   string to repeat
     * @param times number how many times repeat the string
     * @return      repeated string
     */
    public String repeat(String str, int times) {
        return str.repeat(times);
    }

    /**
     * Returns array with methods. Each element of array represents each public method of server.
     * Third element of subarray allows you to parse types of passed params.
     * 
     * @return Array with methods (name, description, params)
     */
    public ArrayList<ArrayList<String>> show() {
        ArrayList<ArrayList<String>> methods = new ArrayList<>();

        ArrayList<String> pow = new ArrayList<>();
        pow.add("pow");
        pow.add("Returns number in power rounded or not defined with flag");
        pow.add("int, int, boolean");

        ArrayList<String> repeat = new ArrayList<>();
        repeat.add("repeat");
        repeat.add("Returns string repeated N times");
        repeat.add("string, int");

        ArrayList<String> show = new ArrayList<>();
        show.add("show");
        show.add("Returns array with description of all server methods.");
        show.add("");

        return methods;
    }
}
