## Instrukcja uruchomienia programu

Aby urochomić ten program, należy:
  - Zresetować poprzednią bazę danych używając komendy `python create_database.py`.
  - Dla testów z gotową BD można użyć `python seeder.py`.
  - Urochomić brokera używając `mosquitto`.
  - Uruchomić scrypt `publisher.py` na urządzeniu Raspberry Pi lub Virtual Machine (z Debianem).
  - Uruchomić scrypt `subscriber.py` na serwerze (PC lub to samo urządzenie Raspberry Pi)
  
## Struktura

```text
.
├── report.csv
├── records.db
├── publisher.py
├── subscriber.py
├── create_database.py
└── seeder.py
```

## Opis składowych i działania aplikacji

**`create_database.py`**

Tworzy bazę danych i usuwa poprzednią.

**`seeder.py`** 

Generuje 1000 fejków w tablicah `workers` i `cards` dla sprawdzenia działalności programu.

**`publisher.py`**

Podłączamy się do Brokera i odsyłujemy Card ID do brokera (topic=`worker/test`).
Sprawdzamy poprawność Card ID (ID może być tylko liczbą). Ten plik będzie używany na
urządzeniu Raspberry Pi (lub na Virtual Machine).

**`subscriber.py`**

Podłączamy się do Brokera, otrzymujemy message w potrzebnym topiku. Używamy ten plik na serwerze, czyli na 
PC lub innym urządzeniu (w tym i Raspberry Pi). Przy uruchomieniu plika mamy utworzony GUI z 
różnymi przyciskami (symulowany system urządzający - admin panel).

## Baza danych projektu

Dla tego projektu jest używana biblioteka `sqlite3`. SQLite jest bardzo wygodna i prosta w 
tej sytuacji.

##### Tablica `workers`

Przechowujemy tu wszystkich pracowników.
```text
workers
+- id           INTEGER, AUTOINCREMENT
+- name         TEXT, NOT NULL
+- card_id      INTEGER, NULLABLE
+- hired_at     DATETIME CURRENT_TIMESTAMP
```

##### Tablica `cards`
Przechowujemy tu wszystkie karty elektroniczne.
```text
cards
+- id           INTEGER, AUTOINCREMENT
+- name         TEXT, NOT NULL
+- worker_id    INTEGER, NULLABLE
+- created_at   DATETIME CURRENT_TIMESTAMP
```

##### Tablica `records`
Przechowujemy tu zapisy wszystkich wyjść/wejść pracowników.
```text
cards
+- id           INTEGER, AUTOINCREMENT
+- card_id      INTEGER, NOT NULL
+- worker_id    INTEGER, NULLABLE
+- timestamp    DATETIME CURRENT_TIMESTAMP
```

## Screenshots

![alt first](https://imgur.com/vngDjtB.png])

![alt second](https://imgur.com/IY9fQ2z.png])

![alt third](https://imgur.com/9vnHAbh.png])