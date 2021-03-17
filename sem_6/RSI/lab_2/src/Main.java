import java.io.IOException;
import java.net.URL;
import java.util.Vector;

import org.apache.xmlrpc.XmlRpcClient;
import org.apache.xmlrpc.XmlRpcException;

public class Main {
    public final static String serverName = "Zakhovaiko";
    public final static String IP = "156.17.130.166";
    public final static int PORT = 63012;

    public static void main(String[] args) throws XmlRpcException, IOException {
        URL url = new URL("http", IP, PORT, "");
        XmlRpcClient srv = new XmlRpcClient(url);

        // Pass two params to first procedure
        Vector<Object> params = new Vector<>();
        params.addElement(serverName);
        params.addElement("251526");
        Object res = srv.execute(serverName + ".viewProc", params);
        System.out.println("Show method was executed." + res);

        // Call third procedure
        AsyncCallback callback = new AsyncCallback();
        Vector<Object> asyncProcedureParams = new Vector<>();
        asyncProcedureParams.addElement("Zakhovaiko");
        asyncProcedureParams.addElement(80);
        srv.executeAsync(serverName + ".fun203", asyncProcedureParams, callback);

        // Pass two params to first procedure
        params.clear();
        params.addElement("Hello");
        params.addElement(55);
        params.addElement(true);
        res = srv.execute(serverName + ".fun14", params);
        System.out.println("Show method was executed." + res);
    }
}
