public class Main {
    public static void main(String[] args) {
        Firma Nokia = new Firma();

        Pracownik a = new Pracownik("A", "A.imie", "0A", 1200);
        Pracownik b = new Pracownik("B", "B.imie", "0B", 1500);
        Pracownik c = new Pracownik("C", "C.imie", "0C", 3000);
        a.dacPodwyzke(50); // 1800

        Specjalista d = new Specjalista("D", "D.imie", "0D", 3000);
        Nokia.increaseForIndividualSp(d, 2000);

        Nokia.addWorker(a);
        Nokia.addWorker(b);
        Nokia.addWorker(c);
        Nokia.addWorker(d);

        System.out.println("Pracownik Nokii z peselem 0D - " + Nokia.findByPESEL("0C"));

        Zadanie t1 = new Zadanie("Task 1","Pilny");
        Zadanie t2 = new Zadanie("Task 2","Normalny");
        Zadanie t3 = new Zadanie("Task 3","Normalny");

        t1.setPracownik(a);
        t2.setPracownik(b);

        try {
            t3.finish();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        Nokia.addTask(t1);
        Nokia.addTask(t2);
        Nokia.addTask(t3);
        Nokia.increaseIncomes(100);

        System.out.println(Nokia.filterTasks("", "", null));
        System.out.println(Nokia);
    }
}