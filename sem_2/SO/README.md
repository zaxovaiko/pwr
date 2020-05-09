## Zadanie 1  

Program ma symulować działanie algorytmów planowania dostępu do procesora dla zgłaszających się procesów. 
Zbadać średni czas oczekiwania procesów dla różnych algorytmów planowania: 
- FCFS 
- SJF (z wywłaszczaniem i bez) 
- rotacyjnego (z możliwością wyboru kwantu czasu) 
Należy samodzielnie sformułować założenia symulacji. 
Wskazówki: 
- algorytmy najlepiej sprawdzać dla tych samych danych testowych (tj. tych samych ciągów testowych zgłaszających się procesów) 
- ciągów testowych powinno być więcej (20? 50?); wynikiem będą wartości średnie. 
- w każdym ciągu będzie N procesów o losowych długościach fazy procesora (rozkład długości faz dobrać tak, by odpowiadał sytuacji w rzeczywistym systemie, w którym nie jest równomierny), zgłaszających się w losowych momentach (dobrać parametry tak, by mogła powstać kolejka procesów oczekujących na przydział procesora).
- możliwa reprezentacja procesu: rekord (numer, dł.fazy procesora, moment zgłoszenia się, czas oczekiwania /początkowo równy 0/...) 
 
## Zadanie 2  

Symulacja algorytmów planowania dostępu do dysku.
* 'Dysk' to w naszym przypadku liniowo uporządkowany ciąg bloków o nr od 1 do MAX.
* Kryterium oceny algorytmów będzie suma przemieszczeń głowicy dysku, jak wiadomo proporcjonalna do czasu realizacji zleceń.   
* 1.Sprawdzić algorytmy FCFS, SSTF, SCAN i C-SCAN.
* 2.Następnie założyć, że w systemie istnieją także aplikacje real-time, które musza być obsłużone za pomocą EDF i/lub FD-SCAN. Jak wpływa to na wyniki?

Mam na myśli:
- wielkość 'dysku' (ilość bloków)
- liczba i sposób generowania zgłoszeń (pełna kolejka od początku? zgłoszenia w trakcie? rozkład zgłoszeń- równomierny, inny?) 
- sposób uwzględnienia obsługi zgłoszeń real-time

## Zadanie 3

Badanie algorytmów zastępowania stron. 
Należy samodzielnie sformułować założenia symulacji: 

- rozmiar pamięci wirtualnej (ilość stron).
- rozmiar pamięci fizycznej (ilość ramek). 
- długość (powinna być znaczna - min. 1000) i sposób generowania ciągu odwołań do stron (koniecznie uwzględnić zasadę lokalności odwołań).

Działanie programu: 
- wygenerować losowy ciąg n odwołań do stron 
- dla wygenerowanego ciągu podać liczbę błędów strony dla różnych algorytmów zastępowania stron: 
  + 1. FIFO (usuwamy stronę najdłużej przebywającą w pamięci fizycznej) 
  + 2. OPT (optymalny - usuwamy stronę, która nie będzie najdłużej używana) 
  + 3. LRU (usuwamy stronę, do której najdłużej nie nastąpiło odwołanie) 
  + 4. aproksymowany LRU (wiadomo) 
  + 5. RAND (usuwamy losowo wybraną stronę) 
- symulacje przeprowadzić (na tym samym ciągu testowym) dla różnej liczby ramek (np. kilku (3, 5, 10?)  wartości podanych przez użytkownika)