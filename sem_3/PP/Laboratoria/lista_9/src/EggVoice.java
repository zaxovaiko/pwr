class EggVoice extends Thread {
    public EggVoice(String name) {
        super(name);
        System.out.println("Thread with name: " + getName());
    }

    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            try {
                sleep(1000); // wait 1 second
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("Egg"); // print 'Egg' 5 times
        }
    }
}
