import java.io.File;
import java.io.FileInputStream;
import java.rmi.Naming;

public class Client {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.out.println("Bad number of arguments");
            return;
        }

        Worker worker;
        String address = args[0];

        try {
            worker = (Worker) Naming.lookup(address);
        } catch (Exception e) {
            System.out.println("Can not get reference to " + address);
            return;
        }
        System.out.println("Reference to " + address + " was found");

        try {
            String className = "Object";

            boolean isOK = worker.hasClassCode(className);
            if (!isOK) {
                File file = new File(className + ".class");
                byte[] t = new byte[(int) file.length()];
                FileInputStream in = new FileInputStream(className + ".class");
                in.read(t);
                in.close();
                worker.storeClassCode(className, t);
            }

            ResultType result;
            TaskImpl task = new TaskImpl();
            Object[] params = {"hello", 3};

            result = (ResultType) worker.wCompute(task, params);
            System.out.println("Result: " + result);
        } catch (Exception e) {
            System.out.println("Error while computing");
            e.printStackTrace();
        }
    }
}
