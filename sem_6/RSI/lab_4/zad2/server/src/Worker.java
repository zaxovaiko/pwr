import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Worker extends Remote {
<<<<<<< HEAD
    public Object wCompute(Task task, Object[] params) throws RemoteException;
    public boolean hasClassCode(String className) throws RemoteException;
    public void storeClassCode(String className, byte[] t) throws RemoteException;
=======
    public ReturnType compute(Task param) throws RemoteException;
    public ReturnType[] computeAnother(Task param) throws RemoteException;
>>>>>>> 421db498c9e2ff88b7ea9b823040fa35eaf83a9a
}