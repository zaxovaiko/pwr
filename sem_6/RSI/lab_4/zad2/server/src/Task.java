import java.io.Serializable;
import java.util.ArrayList;

public class Task implements Serializable {
    private static final long serialVersionUID = 1L;

    public String str;
    public int times;
 
    public ReturnType compute() throws InterruptedException {
        ReturnType res = new ReturnType();

        if (Math.random() > 0.9) {
            res.description = "Something went wrong. Random value is greater than 0.8.";
            res.value = null;
        } else {
            Thread.sleep(this.times * 1000);
            res.description = "Repeated string " + this.times + " times";
            res.value = (String) this.str.repeat(this.times);
        }

        return res;
    }

    public ReturnType computeAnother(int param) throws InterruptedException {
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(11);
        arr.add(22);
        arr.add(33);
        arr.add(44);

        ReturnType res = new ReturnType();
        try {
            res.description = "Elemnent of array";
            res.value = arr.get(param);
        } catch (Exception e) {
            res.description = "Out of range";
            res.value = null;
        }
        return res;
    }
}
