import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Worker extends Remote {
    public ReturnType compute(Task param) throws RemoteException;
    public ReturnType[] computeAnother(Task param) throws RemoteException;
}