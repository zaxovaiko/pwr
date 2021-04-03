import java.io.Serializable;

public class ReturnType implements Serializable {
    private static final long serialVersionUID = 11L;

    public String description;
    public Object value;

    @Override
    public String toString() {
        return "Value: " + this.value + "; Description: " + this.description;
    }
}
