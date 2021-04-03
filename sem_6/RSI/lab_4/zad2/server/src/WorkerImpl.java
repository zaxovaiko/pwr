import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class WorkerImpl extends UnicastRemoteObject implements Worker {
    private static final long serialVersionUID = 1L;

    public WorkerImpl() throws RemoteException {
        super();
    }

    @Override
    public ReturnType compute(Task param) throws RemoteException {
        try {
            return param.compute();
        } catch (InterruptedException e) {
            e.printStackTrace();
            return null;
        }
    }
}
