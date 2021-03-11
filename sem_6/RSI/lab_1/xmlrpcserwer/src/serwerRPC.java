import org.apache.xmlrpc.WebServer;

public class serwerRPC {

    public static void main(String[] args) {
        try {
            System.out.println("Startuje serwer XML_RPC...");
            int port = 10000;
            WebServer server = new WebServer(port);

            server.addHandler("MojSerwer", new serwerRPC());
            server.start();

            System.out.println("Server listening on port " + port);
        } catch (Exception exception) {
            System.err.println("Serwer XML-RPC: " + exception);
        }
    }

    public int execAsy(int x) {
        System.out.println("... wywolano asy - odliczam...");
        try {
            Thread.sleep(x);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
            Thread.currentThread().interrupt();
        }
        System.out.println("... asy - koniec odliczania");
        return 123;
    }

    public Integer echo(int x, int y) {
        return x + y;
    }
}
