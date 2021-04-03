import java.rmi.Naming;

public class Client {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.out.println("Bad number of arguments");
            return;
        }

        ReturnType result;
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
            Task task = new Task();
            task.str = "hello";
            task.times = 3;

            result = worker.compute(task);
        } catch (Exception e) {
            System.out.println("Error while computing");
            e.printStackTrace();
            return;
        }

        System.out.println("Result: " + result);
    }
}
