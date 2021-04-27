<<<<<<< HEAD
import java.io.FileOutputStream;
=======
>>>>>>> 421db498c9e2ff88b7ea9b823040fa35eaf83a9a
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class WorkerImpl extends UnicastRemoteObject implements Worker {
    private static final long serialVersionUID = 1L;

    public WorkerImpl() throws RemoteException {
        super();
    }

    @Override
<<<<<<< HEAD
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
=======
    public ReturnType compute(Task param) throws RemoteException {
        try {
            return param.compute();
        } catch (InterruptedException e) {
            e.printStackTrace();
            return null;
>>>>>>> 421db498c9e2ff88b7ea9b823040fa35eaf83a9a
        }
    }

    @Override
<<<<<<< HEAD
    public void storeClassCode(String className, byte[] classByteCode) throws RemoteException {
        FileOutputStream out;
        try {
            out = new FileOutputStream(className + ".class");
            out.write(classByteCode);
            out.close();
        } catch (Exception e) {
            System.out.println("Error writing class code");
            e.printStackTrace();
=======
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
>>>>>>> 421db498c9e2ff88b7ea9b823040fa35eaf83a9a
        }
    }
}
