import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Firma {
    private ArrayList<Pracownik> workers = new ArrayList<>();
    private ArrayList<Zadanie> tasks = new ArrayList<>();

    public void addWorker(Pracownik pracownik) {
        workers.add(pracownik);
    }

    public void addTask(Zadanie zadanie) {
        tasks.add(zadanie);
    }

    public Pracownik findByPESEL(String PESEL) {
        return workers.stream().filter(worker -> worker.getPesel().equals(PESEL)).collect(Collectors.toList()).get(0);
    }

    public void increaseIncomes(int percent) {
        workers.forEach(worker -> worker.setPlaca(worker.getPlaca() + worker.getPlaca() * percent));
    }

    public void increaseForIndividualSp(Specjalista s, int p) {
        s.setPremia(p);
    }

    public List<Zadanie> filterTasks(String nazwa, String status, Pracownik pracownik) {
        return tasks.stream()
                .filter(t -> nazwa.equals("") || t.getNazwa().equals(nazwa))
                .filter(t -> status.equals("") || t.getStatus().equals(status))
                .filter(t -> pracownik == null || t.getPracownik().equals(pracownik))
                .sorted((o1, o2) -> {
                    if (o1.getTryb().equals("Pilny") && !o2.getTryb().equals("Pilny")) {
                        return -1;
                    } else if (!o1.getTryb().equals("Pilny") && o2.getTryb().equals("Pilny")) {
                        return 1;
                    }
                        return 0;
                }).collect(Collectors.toList());
    }

    @Override
    public String toString() {
        return "Firma{" +
                "workers=" + workers +
                ", tasks=" + tasks +
                '}';
    }
}
