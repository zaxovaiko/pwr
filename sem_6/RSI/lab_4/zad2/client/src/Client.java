import java.rmi.Naming;

public class Client {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.out.println("Bad number of arguments");
            return;
        }

        ReturnType result;
        Worker worker;
        Worker worker2;

        String address = args[0];

        try {
            worker2 = (Worker) Naming.lookup(address);
        } catch (Exception e) {
            System.out.println("Can not get reference to " + address);
            return;
        }

        try {
            worker = (Worker) Naming.lookup(address);
        } catch (Exception e) {
            System.out.println("Can not get reference to " + address);
            return;
        }
        System.out.println("Reference to " + address + " was found");

        try {
            Task task = new Task();
            task.str = "hello";
            task.times = 3;

            result = worker.compute(task);
            System.out.println("Result: " + result);
        } catch (Exception e) {
            System.out.println("Error while computing");
            e.printStackTrace();
        }

        int times = 2;
        ReturnType[] rt = new ReturnType[times];
        try {
            Task task = new Task();
            task.times = times;
            task.str = "hello";

            rt = worker2.computeAnother(task);
            System.out.println("Results: ");
            for (int i = 0; i < rt.length; i++) {
                System.out.println("Value: " + rt[i].value + " Desc: " + rt[i].description);
            }
        } catch (Exception e) {
            System.out.println("Error while computing");
            e.printStackTrace();
        }
    }
}
