import java.io.Serializable;

public class InputType implements Serializable {
    private static final long serialVersionUID = 101L;

    String operation;
    public double x1;
    public double x2;

    public double getX1() {
        return x1;
    }

    public double getX2() {
        return x2;
    }
}
