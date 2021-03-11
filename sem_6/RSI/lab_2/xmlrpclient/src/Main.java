import org.apache.xmlrpc.XmlRpcClient;

import java.util.Vector;

public class Main {
    public static void main(String[] args) {
        int port = 10000;
	    try {
            XmlRpcClient srv = new XmlRpcClient("http://localhost:" + port);
            
            Vector<Integer> params = new Vector<>();
            params.addElement(13);
            params.addElement(21);
            int wynik = (Integer) srv.execute("MojSerwer.echo", params);
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
