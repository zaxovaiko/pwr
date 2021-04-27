import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
<<<<<<< HEAD
    public static void main(String[] args) {
=======
    public static void main(String[] args) throws Exception {
>>>>>>> 421db498c9e2ff88b7ea9b823040fa35eaf83a9a
        if (args.length == 0) {
            System.out.println("No arguments passed");
            return;
        }

<<<<<<< HEAD
        if (System.getSecurityManager() == null) {
            System.setSecurityManager(new SecurityManager());
        }
=======
        // if (System.getSecurityManager() == null) {
        //     System.setSecurityManager(new SecurityManager());
        // }
>>>>>>> 421db498c9e2ff88b7ea9b823040fa35eaf83a9a

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
<<<<<<< HEAD
=======
            return;
>>>>>>> 421db498c9e2ff88b7ea9b823040fa35eaf83a9a
        }
    }
}
