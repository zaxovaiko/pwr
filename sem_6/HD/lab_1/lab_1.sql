CREATE TABLE [251526].dbo.Klient
(
	PESEL CHAR(11) NOT NULL,
	imie VARCHAR(255) NOT NULL,
	nazwisko VARCHAR(255) NOT NULL,
	wiek TINYINT NOT NULL,
	plec CHAR(1) NOT NULL,
	telefon CHAR(11)
);

CREATE TABLE [251526].dbo.Produkt
(
	kod CHAR(12) NOT NULL,
	nazwa VARCHAR(255) NOT NULL,
	opis VARCHAR(255) NOT NULL,
	cena REAL NOT NULL,
	kategoria VARCHAR(255) NOT NULL
);

CREATE TABLE [251526].dbo.Oferta
(
	ofertaID BIGINT IDENTITY(1,1) NOT NULL,
	produktID CHAR(12) NOT NULL,
	ilosc INT DEFAULT 0
);

CREATE TABLE [251526].dbo.Sklep
(
	nazwa VARCHAR(255) NOT NULL,
	ulica VARCHAR(255) NOT NULL,
	ofertaID BIGINT NOT NULL
);

CREATE TABLE [251526].dbo.Nabywa
(
	nabywaID BIGINT IDENTITY(1, 1) NOT NULL,
	robiZakupyID BIGINT NOT NULL,
	ilosc INT NOT NULL,
	cena REAL NOT NULL
);

CREATE TABLE [251526].dbo.RobiZakupy
(
	robiZakupyID BIGINT IDENTITY(1, 1) NOT NULL,
	klientID CHAR(11) NOT NULL,
	produktID CHAR(12) NOT NULL,
	dataZakupu DATE DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE [251526].dbo.Klient
ADD CONSTRAINT pk_Klient PRIMARY KEY (PESEL),
	CONSTRAINT ck_plec CHECK (plec in ('m', 'k')),
	CONSTRAINT ck_wiek CHECK (wiek > 18);

ALTER TABLE [251526].dbo.Produkt
ADD CONSTRAINT pk_Produkt PRIMARY KEY (kod),
	CONSTRAINT ck_Produkt_cena CHECK (cena >= 0);

ALTER TABLE [251526].dbo.Oferta
ADD CONSTRAINT pk_Oferta PRIMARY KEY (ofertaID),
	CONSTRAINT ck_Oferta_ilosc CHECK (ilosc >= 0),
	CONSTRAINT fk_Oferta_Produkt FOREIGN KEY (produktID) 
	REFERENCES [251526].dbo.Produkt(kod);

ALTER TABLE [251526].dbo.Sklep
ADD CONSTRAINT pk_Sklep PRIMARY KEY (nazwa),
	CONSTRAINT fk_Sklep_Oferta FOREIGN KEY (ofertaID) 
	REFERENCES [251526].dbo.Oferta(ofertaID);

ALTER TABLE [251526].dbo.RobiZakupy
ADD CONSTRAINT pk_RobiZakupy PRIMARY KEY (robiZakupyID),
	CONSTRAINT fk_RobiZakupy_Klient FOREIGN KEY (klientID) 
	REFERENCES [251526].dbo.Klient(PESEL),
	CONSTRAINT fk_RobiZakupy_Produkt FOREIGN KEY (produktID) 
	REFERENCES [251526].dbo.Produkt(kod);

ALTER TABLE [251526].dbo.Nabywa
ADD CONSTRAINT pk_Nabywa PRIMARY KEY (nabywaID),
	CONSTRAINT ck_Nabywa_ilosc CHECK (ilosc > 0),
	CONSTRAINT ck_Nabywa_cena CHECK (cena > 0),
	CONSTRAINT fk_Nabywa_Zakupy FOREIGN KEY (robiZakupyID) 
	REFERENCES [251526].dbo.RobiZakupy(robiZakupyID);


INSERT INTO [251526].dbo.Klient VALUES ('12345678901', 'Volodymyr', 'Zakhovaiko', 19, 'm', '48881035771'); 
INSERT INTO [251526].dbo.Klient VALUES ('12345678900', 'Anna', 'Kowalska', 20, 'k', '48881035772'); 
INSERT INTO [251526].dbo.Klient VALUES ('12345678901', 'Adam', 'Malewski', 20, 'm', '48881035773');  -- error

INSERT INTO [251526].dbo.Produkt VALUES ('000011112222', 'Xiaomi Mi Bend 3', 'Fitness gadzet', 120.87, 'akcesoria');
INSERT INTO [251526].dbo.Produkt VALUES ('000011112223', 'Samsung Galaxy 2', 'Mobile phone', 1200, 'telefony');
INSERT INTO [251526].dbo.Produkt VALUES ('000011112224', 'Lenovo 430s', 'Laptop ultrathin', 8000, 'laptopy');

INSERT INTO [251526].dbo.Oferta VALUES ('000011112222', 12);
INSERT INTO [251526].dbo.Oferta VALUES ('000011112223', 190);

INSERT INTO [251526].dbo.Sklep VALUES ('24/7 Spożywczy', 'Wroclawska 42', 1);
INSERT INTO [251526].dbo.Sklep VALUES (100500, 'Gdanska 43', 2);

INSERT INTO [251526].dbo.RobiZakupy VALUES ('12345678901', '000011112222');

INSERT INTO [251526].dbo.Nabywa VALUES (1, 12, 2100);