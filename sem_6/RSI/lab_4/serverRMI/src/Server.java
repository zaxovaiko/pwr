import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {

    public static void main(String[] args) {
	    if (args.length == 0) {
            System.out.println("You have to enter RMI object address in the form: //host_address/service_name");
            return;
        }

	    if (System.getSecurityManager() == null) {
	        System.setSecurityManager(new SecurityManager());
        }

	    try {
            Registry reg = LocateRegistry.createRegistry(1099);
        } catch (RemoteException e) {
	        e.printStackTrace();
        }

	    try {
	        CalcObjImpl implObiektu = new CalcObjImpl();
            Naming.rebind(args[0], implObiektu);

            System.out.println("Server is registered now");
        } catch (Exception e) {
            System.out.println("Server cant be registered");
            e.printStackTrace();
        }

        try {
            CalcObjImpl2 implObiektu2 = new CalcObjImpl2();
            Naming.rebind(args[1], implObiektu2);

            System.out.println("Server2 is registered now");
            System.out.println("Press Ctrl + C to stop...");
        } catch (Exception e) {
            System.out.println("Server cant be registered");
            e.printStackTrace();
        }
    }
}
