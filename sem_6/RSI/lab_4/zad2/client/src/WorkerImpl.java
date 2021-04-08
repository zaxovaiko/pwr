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

    @Override
    public ReturnType[] computeAnother(Task param) throws RemoteException {
        try {
            ReturnType[] rt = new ReturnType[param.times];
            for (int i = 0; i < param.times; i++) {
                param.times = (int) (Math.random() * 5 + 1);
                System.out.println("Wait (secs): " + param.times);
                rt[i] = param.compute();
            }
            return rt;
        } catch (InterruptedException e) {
            e.printStackTrace();
            return null;
        }
    }
}
