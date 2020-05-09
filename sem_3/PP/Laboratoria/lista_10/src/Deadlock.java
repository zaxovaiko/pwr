public class Deadlock {
    public static void main(String[] args) {
        final A a = new A();
        final B b = new B();

        // Thread 1
        Runnable block1 = () -> {
            synchronized (a) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                // Thread 1 have A but need B also
                synchronized (b) {
                    System.out.println("In block 1, i = " + b.i);
                }
            }
        };

        // Thread 2
        Runnable block2 = () -> {
            synchronized (b) {
                // Thread 2 have B but need A also
                synchronized (a) {
                    System.out.println("In block 2, i = " + a.i);
                }
            }
        };

        new Thread(block1).start();
        new Thread(block2).start();
    }

    // Resource A
    static class A {
        int i = 10;
    }

    // Resource B
    static class B {
        int i = 20;
    }
}