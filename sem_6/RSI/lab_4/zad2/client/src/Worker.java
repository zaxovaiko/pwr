import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Worker extends Remote {
    public Object wCompute(Task task, Object[] params) throws RemoteException;
    public boolean hasClassCode(String className) throws RemoteException;
    public void storeClassCode(String className, byte[] t) throws RemoteException;
}