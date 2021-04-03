import java.io.Serializable;

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
}
