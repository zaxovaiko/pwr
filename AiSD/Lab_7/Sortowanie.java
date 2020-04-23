package Lab_7;

import java.util.Random;

class Sortowanie {
    private int[] array = new int[5000];

    Sortowanie(int type) {
        if (type == 0) {
            for (int i = 0; i < array.length; i++) {
                array[i] = new Random().nextInt(5000) + 1;
            }
        } else if (type == 1) {
            for (int i = 1; i <= array.length; i++) {
                array[i - 1] = i;
            }
        } else {
            for (int i = array.length; i > 0; i--) {
                array[i - 1] = i;
            }
        }

        int[] array_quick = new int[this.array.length];
        int[] array_merge = new int[this.array.length];
        System.arraycopy(array, 0, array_quick, 0, array.length);
        System.arraycopy(array, 0, array_merge, 0, array.length);

        System.out.printf(" %8s | %8s | %8s | %8s | %9s | %8s", insert(), bubble(), select(), heap(), quick(array_quick, 0, array_quick.length - 1), merge(array_merge, 0, array_merge.length - 1));
    }

    void merged(int arr[], int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; ++i) {
            L[i] = arr[l + i];
        }

        for (int j = 0; j < n2; ++j) {
            R[j] = arr[m + 1 + j];
        }

        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    long merge(int[] merged, int l, int r) {
        long start = System.nanoTime();
        if (l < r) {
            int m = (l + r) / 2;
            merge(merged, l, m);
            merge(merged, m + 1, r);
            merged(merged, l, m, r);
        }
        return System.nanoTime() - start;
    }

    int partition(int[] array, int low, int high) {
        int pivot = array[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (array[j] <= pivot) {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }

        int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;

        return i + 1;
    }

    long quick(int[] array, int low, int high) {
        long start = System.nanoTime();

        if (low < high) {
            int pi = partition(array, low, high);
            quick(array, low, pi - 1);
            quick(array, pi + 1, high);
        }

        return System.nanoTime() - start;
    }

    long heap() {
        int[] array = new int[this.array.length];
        System.arraycopy(this.array, 0, array, 0, this.array.length);

        long start = System.nanoTime();
        int n = array.length;

        // будуємо курган
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(array, n, i);
        }

        // вставляємо вершину в кінець масиву
        for (int i = n - 1; i >= 0; i--) {
            int temp = array[0];
            array[0] = array[i];
            array[i] = temp;
            heapify(array, i, 0);
        }

        return System.nanoTime() - start;
    }

    void heapify(int arr[], int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if (l < n && arr[l] > arr[largest]) {
            largest = l;
        }

        if (r < n && arr[r] > arr[largest]) {
            largest = r;
        }

        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            heapify(arr, n, largest);
        }
    }

    long select() {
        int[] array = new int[this.array.length];
        System.arraycopy(this.array, 0, array, 0, this.array.length);

        long start = System.nanoTime();
        int n = array.length;

        // шукаємо мінімум в підмасиві і заміняємо з тєкущєм
        for (int i = 0; i < n - 1; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if (array[j] < array[min]) {
                    min = j;
                }
            }

            int temp = array[min];
            array[min] = array[i];
            array[i] = temp;
        }
        return System.nanoTime() - start;
    }

    long bubble() {
        int[] array = new int[this.array.length];
        System.arraycopy(this.array, 0, array, 0, this.array.length);

        long start = System.nanoTime();
        int n = array.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        return System.nanoTime() - start;
    }

    long insert() {
        int[] array = new int[this.array.length];
        System.arraycopy(this.array, 0, array, 0, this.array.length);

        long start = System.nanoTime();
        int n = array.length;
        for (int i = 1; i < n; ++i) {
            int key = array[i];
            int j = i - 1;

            // якшо менше заміняємо на перший елемент підмасиву і сунемо вліво підмасив
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = key;
        }
        return System.nanoTime() - start;
    }
}
