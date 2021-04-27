import java.io.Serializable;

public class ResultType implements Serializable {
    private static final long serialVersionUID = 11L;

    public String description;
    public Object value;

    @Override
    public String toString() {
        return "Value: " + this.value + ";\nDescription: " + this.description;
    }
}
