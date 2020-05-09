public class Livelock {
    static class Car1 {
        private boolean honking = true;

        public void passBridge(Car2 car2) {
            while (car2.hasPassedBridge()) {
                System.out.println("Car 1 is waiting to pass the bridge");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
            }

            System.out.println("Car 1 has passed bridge");
            honking = false;
        }

        public boolean hasPassedBridge() {
            return honking;
        }
    }

    public static class Car2 {
        private boolean honking = true;

        public void passBridge(Car1 car1) {
            while (car1.hasPassedBridge()) {
                System.out.println("Car 2 is waiting to pass the bridge");

                try {
                    Thread.sleep(1000);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
            }

            System.out.println("Car 2 has passed the bridge");
            honking = false;
        }

        public boolean hasPassedBridge() {
            return honking;
        }
    }

    public static class BridgeCheck {
        static final Car1 car1 = new Car1();
        static final Car2 car2 = new Car2();

        public static void main(String[] args) {
            Thread t1 = new Thread(() -> car2.passBridge(car1));
            t1.start();

            Thread t2 = new Thread(() -> car1.passBridge(car2));
            t2.start();
        }
    }
}