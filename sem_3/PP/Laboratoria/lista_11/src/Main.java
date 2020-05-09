import org.w3c.dom.ls.LSOutput;

import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int threads = Runtime.getRuntime().availableProcessors();
        System.out.println("COMPUTER HAS " + threads + " THREADS");

        // Nasza tablica o rozmiarze 100 z losowymi dannymi
        // Ale to bedzie problem dla naprzyklad 15tu elementow
        // poniewaz kazda podtablica bedzie miala tylko 1 element O_o
        int[] array = new int[new Random().nextInt(10) + 1];
        int[][] divided = new int[threads][];
        int toGetSize = array.length / threads; // Size of subArray divided by each thread
        int initialLength = array.length;

        System.out.println("NOT SORTED");

        for (int i = 0; i < array.length; i++)
            array[i] = new Random().nextInt(100);
        System.out.println(Arrays.toString(array));

        if (array.length < threads) {
            int[] newArray = new int[threads];
            System.arraycopy(array, 0, newArray, threads - array.length, array.length);
            array = newArray;
            toGetSize = 1; // update array size for absolute division for each threads
        }

        System.out.println("SUBARRAY SIZE: " + toGetSize);

        for (int i = 0; i < threads; i++) {
            int[] subArr = (i == threads - 1) ? new int[array.length - i * toGetSize] : new int[toGetSize];
            System.arraycopy(array, i * toGetSize, subArr, 0, (i == threads - 1) ? array.length - i * toGetSize : toGetSize);
            divided[i] = subArr;
        }

        // 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 <-- array
        // |_| |_| |_| |_| |__| |___| |___| |...............| <-- subArrays by threads

        int repeats = threads;
        int[][] tempArr;

        while (repeats > 1) {
            tempArr = new int[repeats / 2][];
            for (int i = 0; i < repeats; i += 2) {
                Worker runner1 = new Worker(divided[i]);
                Worker runner2 = new Worker(divided[i + 1]);

                runner1.start();
                runner2.start();
                runner1.join();
                runner2.join();

                tempArr[i / 2] = finalMerge(runner1.getInternal(), runner2.getInternal());
            }
            repeats /= 2;
            divided = tempArr;
        }

        int[] res;
        if (initialLength < threads) {
            res = new int[initialLength];
            System.arraycopy(divided[0], threads - initialLength, res, 0, initialLength);
        } else {
            res = divided[0];
        }

        System.out.println("SORTED\n" + Arrays.toString(res));
    }

    public static int[] finalMerge(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];

        int i = 0;
        int j = 0;
        int r = 0;

        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) {
                result[r] = a[i];
                i++;
            } else {
                result[r] = b[j];
                j++;
            }

            r++;

            if (i == a.length) {
                while (j < b.length) {
                    result[r] = b[j];
                    r++;
                    j++;
                }
            }

            if (j == b.length) {
                while (i < a.length) {
                    result[r] = a[i];
                    r++;
                    i++;
                }
            }
        }
        return result;
    }

    static class Worker extends Thread {
        private int[] internal;

        public int[] getInternal() {
            return internal;
        }

        public void mergeSort(int[] array) {
            if (array.length > 1) {
                int[] left = leftHalf(array);
                int[] right = rightHalf(array);

                mergeSort(left);
                mergeSort(right);

                merge(array, left, right);
            }
        }

        public int[] leftHalf(int[] array) {
            int size1 = array.length / 2;
            int[] left = new int[size1];
            System.arraycopy(array, 0, left, 0, size1);
            return left;
        }

        public int[] rightHalf(int[] array) {
            int size1 = array.length / 2;
            int size2 = array.length - size1;
            int[] right = new int[size2];
            System.arraycopy(array, size1, right, 0, size2);
            return right;
        }

        public void merge(int[] result, int[] left, int[] right) {
            int i1 = 0;
            int i2 = 0;

            for (int i = 0; i < result.length; i++) {
                if (i2 >= right.length || (i1 < left.length && left[i1] <= right[i2])) {
                    result[i] = left[i1];
                    i1++;
                } else {
                    result[i] = right[i2];
                    i2++;
                }
            }
        }

        Worker(int[] arr) {
            internal = arr;
        }

        public void run() {
            mergeSort(internal);
        }
    }
}