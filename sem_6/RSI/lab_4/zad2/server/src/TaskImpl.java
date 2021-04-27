public class TaskImpl implements Task {
    private static final long serialVersionUID = 1L;
 
    public Object compute(Object[] params) {
        ResultType res = new ResultType();
        if (Math.random() > 0.6) {
            res.description = "Something went wrong. Random value is greater than 0.6";
            res.value = null;
        } else {
            res.description = "Repeated string " + params[0] + " times";
            res.value = ((String) params[1]).repeat((int) params[0]);
        }
        return res;
    }
}
