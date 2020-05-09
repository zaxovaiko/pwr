package Lab_8;

import java.math.BigInteger;

class Shell {
    private int size;
    private int v = 0;
    private BigInteger[] array;
    private long[][] times = new long[4][3];

    void run() {
        for (int size : new int[] { 5000, 10000, 50000, 100000 }) {
            this.size = size;
            this.array = new BigInteger[size];

            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 3; j++) {
                    switch (i) {
                        case 0: a(); break;
                        case 1: b(); break;
                        case 2: c(); break;
                        case 3: d(); break;
                    }
                    v = j;
                    times[i][j] = getTime();
                }
            }

            // Wyświtlenie wyników
            print(times);
        }
    }

    private void a() {
        for (int i = 0; i < size; i++) {
            array[i] = i == 0 ? BigInteger.valueOf(1) : array[i - 1].multiply(BigInteger.valueOf(3)).add(BigInteger.valueOf(1));
        }
    }

    private void b() {
        for (int i = 0; i < size; i++) {
            array[i] = BigInteger.valueOf((long) (Math.pow(2, (double) (i + 1)) - 1));
        }
    }

    private void c() {
        for (int i = 0; i < size; i++) {
            array[i] = BigInteger.valueOf(i == 0 ? 1 : (long) Math.pow(2, (double) i) + 1);
        }
    }

    private void d() {
        for (int i = 0; i < size; i++) {
            array[i] = i > 1 ? array[i - 1].add(array[i - 2]) : BigInteger.valueOf(i);
        }
    }

    private long getTime() {
        BigInteger[] arr = new BigInteger[size];
        System.arraycopy(array, 0, arr, 0, array.length);

        int start = arr.length / 2;
        long startTime = System.nanoTime();

        while (start > 0) {
            if (start == 1) {
                if (v == 1 || v == 3) {
                    insert(start, arr);
                } else if (v == 2) {
                    bubble(start, arr);
                    bubble(start, arr);
                }
            } else {
                if (v == 1 || v == 2) {
                    insert(start, arr);
                } else if (v == 3) {
                    bubble(start, arr);
                }
            }
            start /= 2;
        }
        return System.nanoTime() - startTime;
    }

    private void bubble(int start, BigInteger[] array) {
        for (int i = start; i < array.length; i++) {
            for (int j = 1; j < array.length - i; j++) {
                if (array[j - 1].compareTo(array[j]) > 0) {
                    BigInteger temp = array[j - 1];
                    array[j - 1] = array[j];
                    array[j] = temp;
                }
            }
        }
    }

    private void insert(int start, BigInteger[] array) {
        for (int j, i = start; i < array.length; i++) {
            BigInteger tmp = array[i];
            for (j = i - 1; j >= 0 && array[j].compareTo(tmp) > 0; j--) {
                array[j + 1] = array[j];
            }
            array[j + 1] = tmp;
        }
    }

    private void print(long[][] times) {
        System.out.printf("Ilość elementów: %d\n", array.length);
        System.out.println("-------------------------------------------------------");
        System.out.printf("| %3s | %13s | %13s | %13s |\n", "C\\W", "1", "2", "3");
        System.out.println("-------------------------------------------------------");
        for (int i = 0; i < times.length; i++) {
            System.out.printf("| %3s |", i);
            for (long resultCell : times[i])
                System.out.printf("%11s ns |", resultCell);
            System.out.println();
        }
        System.out.println("-------------------------------------------------------");
    }
}
