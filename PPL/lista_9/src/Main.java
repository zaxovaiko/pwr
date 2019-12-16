public class Main {
    static EggVoice thread;

    public static void main(String[] args) {
        thread = new EggVoice("Egg");
        System.out.println("What was the first?");
        thread.start();

        for (int i = 0; i < 5; i++) {
            try {
                Thread.sleep(1100); // stop for 1.1 sec
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Chicken");
        }

        // word 'chicken' was said 5 times
        // if thread is still alive
        if (thread.isAlive()) {
            try {
                thread.join(); // wait for ending
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("Egg appeared the first.");
        } else {
            System.out.println("Chicken appeared the first.");
        }

        System.out.println("The end");
    }
}