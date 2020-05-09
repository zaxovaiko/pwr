class RaceCondition {
    public static void main(String[] args) {
        final double AMOUNT     = 100;
        final int REPETITIONS   = 100;
        final int THREADS       = 100;

        BankAccount account = new BankAccount();

        for (int i = 0; i < THREADS; i++) {
            DepositRunnable d = new DepositRunnable(account, AMOUNT, REPETITIONS);
            WithdrawRunnable w = new WithdrawRunnable(account, AMOUNT, REPETITIONS);

            Thread dt = new Thread(d);
            Thread wt = new Thread(w);

            dt.start();
            wt.start();
        }
    }

    public static class BankAccount {
        private double balance = 0;

        public void deposit(double amount) {
            System.out.println("Depositing " + amount);
            double newBalance = balance + amount;

            System.out.println("New balance is " + newBalance);
            balance = newBalance;
        }

        public void withdraw(double amount) {
            System.out.println("Withdrawing " + amount);
            double newBalance = balance - amount;

            System.out.println("New balance is " + newBalance);
            balance = newBalance;
        }
    }

    public static class WithdrawRunnable implements Runnable {
        private static final int DELAY = 1;
        private BankAccount account;
        private double amount;
        private int count;

        public WithdrawRunnable(BankAccount anAccount, double anAmount, int aCount) {
            account = anAccount;
            amount = anAmount;
            count = aCount;
        }

        public void run() {
            try {
                for (int i = 1; i <= count; i++) {
                    account.withdraw(amount);
                    Thread.sleep(DELAY);
                }
            } catch (InterruptedException ignored) { }
        }
    }

    public static class DepositRunnable implements Runnable {
        private static final int DELAY = 1;
        private BankAccount account;
        private double amount;
        private int count;

        public DepositRunnable(BankAccount anAccount, double anAmount, int aCount) {
            account = anAccount;
            amount = anAmount;
            count = aCount;
        }

        public void run() {
            try {
                for (int i = 1; i <= count; i++) {
                    account.deposit(amount);
                    Thread.sleep(DELAY);
                }
            } catch (InterruptedException ignored) { }
        }
    }
}