import java.rmi.Remote;
import java.rmi.RemoteException;

public interface CalcObject extends Remote {
    public double calculate(double a, double b) throws RemoteException;
}
