import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.out.println("No arguments passed");
            return;
        }

        // if (System.getSecurityManager() == null) {
        //     System.setSecurityManager(new SecurityManager());
        // }

        try {
            Registry reg = LocateRegistry.createRegistry(1099);
        } catch (RemoteException e) {
            e.printStackTrace();
        }

        try {
            WorkerImpl worker = new WorkerImpl();
            Naming.rebind(args[0], worker);

            System.out.println("Server is running");
            System.out.println("Press ctrl + c to stop the server...");
        } catch (Exception e) {
            e.printStackTrace();
            return;
        }
    }
}
