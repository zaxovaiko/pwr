import java.net.URL;

public class AsyncCallback implements org.apache.xmlrpc.AsyncCallback {
    @Override
    public void handleResult(Object o, URL url, String s) {
        System.out.println("Async method works well");
        System.out.println(o);
    }

    @Override
    public void handleError(Exception e, URL url, String s) {
        System.out.println("Something went wrong in async method");
    }
}
