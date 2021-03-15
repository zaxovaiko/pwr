import org.apache.xmlrpc.XmlRpcClient;

import java.util.Vector;

public class Main {
    public static void main(String[] args) {
	    try {
            XmlRpcClient srv = new XmlRpcClient("http://156.17.235.81:8080");
            Vector<Integer> params = new Vector<>();
            params.addElement(13);
            params.addElement(21);
            Object result = srv.execute("MojSerwer.echo", params);

            int wynik = (Integer) result;
            System.out.println("Wynik: " + wynik);

            AC cb = new AC();
            Vector<Integer> params2 = new Vector<>();
            params2.addElement(3000);
            srv.executeAsync("MojSerwer.execAsy", params2, cb);
            System.out.println("Wywolano asynchornicznie");
        } catch (Exception exception) {
            System.err.println("Klient XML-RPC: " + exception);
        }
    }
}
