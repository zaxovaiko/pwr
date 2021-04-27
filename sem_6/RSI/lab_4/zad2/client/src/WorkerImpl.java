import java.io.FileOutputStream;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class WorkerImpl extends UnicastRemoteObject implements Worker {
    private static final long serialVersionUID = 1L;

    public WorkerImpl() throws RemoteException {
        super();
    }

    @Override
    public Object wCompute(Task task, Object[] params) throws RemoteException {
        return task.compute(params);
    }

    @Override
    public boolean hasClassCode(String className) {
        try {
            Class.forName(className);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    @Override
    public void storeClassCode(String className, byte[] classByteCode) throws RemoteException {
        FileOutputStream out;
        try {
            out = new FileOutputStream(className + ".class");
            out.write(classByteCode);
            out.close();
        } catch (Exception e) {
            System.out.println("Error writing class code");
            e.printStackTrace();
        }
    }
}
