import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CalcObjImpl extends UnicastRemoteObject implements CalcObject {
    private static final long serialVersionUID = 101L;

    public CalcObjImpl() throws RemoteException {
        super();
    }

    @Override
    public double calculate(double a, double b) throws RemoteException {
        return a + b;
    }
}
