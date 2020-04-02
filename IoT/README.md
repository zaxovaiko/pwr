### Instrukcja uruchomienia programu

 - Pobierz pliki programu
 - Użyj komendy `python main.py`

### Struktura
```text
.
├── resources
│   ├── cards.json
│   ├── records.json
│   ├── terminals.json
│   └── workers.json
├── main.py
├── system.py
└── README.md
```

`./resources/` - Folder z prostą bazą danych (JSON).

### Opis składowych i działania aplikacji

Ten projekt jest napisany w stylu OOP z używaniem dodatkowych 
modułów `datetime, csv, json, sys`. Projekt zawiera dwa pliki `main.py` i `system.py`.

##### `main.py`
Używamy, żeby urochomić program.

##### `system.py` 
 Jest on głównym plikiem w tej aplikacji. Ma realizowaną klasę `System`. 

 - `loop` - główna pętla programu
 - `connect_terminal` - podłączamy terminal do systemu
 - `disconnect_terminal` - odłączamy terminal od systemu
 - `pin_card_to_worker` - przypisuje kartę do użytkownika
 - `unpin_card_from_worker` - usuwa kartę od użytkownika
 - `add_card` - dodaje kartę do systemu
 - `remove_card` - usuwa kartę z systemu
 - `generate_report` - generuje raport
 - `exit` - kończy działanie systemu
 - `register_card` - odczyta kartę terminalem
 - `__print_menu` - dodatkowa funkcja dla wyświetlenia listy (menu)
 - `__check_input` - dodatkowa funkcja dla sprawdzenia wyboru z menu

### Baza Danych dla projektu

W tej aplikacji używam pliki typu `json` dla szybkiego i komfortnego odczuty i zapisu danych.
`JSON` jest bardzo wygodny dla użycia w programie napisanej na Pythonie, bo jest podobny do słownika.

Przykłady:  

`cards.json`
```json
[
  {
    "id": 1,
    "user_id": -1
  },
  {
    "id": 2,
    "user_id": 3
  },
  {
    "id": 3,
    "user_id": 2
  }
]
```
Zawiera numer karty również numer użytkownika, do którego ta karta jest przypisana.

> `-1` oznacza brak przypisanego użytkownika.

### Screenshots
Główne menu programu:

![Główne menu](https://imgur.com/TWWtccW.png)