-- 1
--SELECT MIN(PP.LastName + ', ' + PP.FirstName) Pracownik, 
--	SOH.SalesPersonID pracID, 
--	YEAR(SOH.OrderDate) "Rok zamowienia", 
--	SUM(SOH.SubTotal) Kwota, 
--	COUNT(SOH.SalesOrderID) "Liczba zamowien"
--FROM Sales.SalesOrderHeader AS SOH
--	JOIN Person.Person AS PP
--	ON PP.BusinessEntityID = SOH.SalesPersonID
--GROUP BY YEAR(SOH.OrderDate), SOH.SalesPersonID
--ORDER BY pracID, "Rok zamowienia";

-- 2
--SELECT DISTINCT PP.LastName + ', ' + PP.FirstName Pracownik, 
--	SOH.SalesPersonID pracID, 
--	YEAR(SOH.OrderDate) "Rok zamowienia", 
--	SUM(SOH.SubTotal) OVER(PARTITION BY SOH.SalesPersonID, YEAR(SOH.OrderDate)) Kwota, 
--	COUNT(SOH.SalesOrderID) OVER(PARTITION BY SOH.SalesPersonID, YEAR(SOH.OrderDate)) "Liczba zamowien"
--FROM Sales.SalesOrderHeader AS SOH
--	INNER JOIN Person.Person AS PP
--	ON PP.BusinessEntityID = SOH.SalesPersonID
--ORDER BY pracID, "Rok zamowienia";

-- 4.1a
DROP TABLE IF EXISTS [251526].dbo.Fact_Orders;
DROP TABLE IF EXISTS [251526].dbo.Dim_Customer;
DROP TABLE IF EXISTS [251526].dbo.Dim_Product;

-- CREATE DATABASE [251526];

CREATE TABLE Dim_Customer (
	CustomerID INT NOT NULL CONSTRAINT PK_Dim_Customer PRIMARY KEY,
	FirstName NVARCHAR(50) NOT NULL,
	LastName NVARCHAR(50) NOT NULL,
	TerritoryName NVARCHAR(50) NOT NULL,
	CountryRegionCode NVARCHAR(3) NOT NULL,
	"Group" NVARCHAR(50) NOT NULL
);

-- 4.1b
CREATE TABLE Dim_Product (
	ProductID INT NOT NULL CONSTRAINT PK_Dim_Product PRIMARY KEY, 
	"Name" NVARCHAR(50) NOT NULL,
	ListPrice MONEY NOT NULL,
	Color NVARCHAR(15) NULL,
	SubCategoryName NVARCHAR(50) NOT NULL,
	CategoryName NVARCHAR(50) NOT NULL
);

-- 4.1c
CREATE TABLE Fact_Orders (
	ProductID INT NOT NULL,
	CustomerID INT NOT NULL,
	OrderDate DATETIME NOT NULL,
	ShipDate DATETIME NULL,
	OrderQty SMALLINT NOT NULL,
	UnitPrice MONEY NOT NULL,
	UnitPriceDiscount MONEY NOT NULL, 
	LineTotal AS ISNULL(([UnitPrice]*((1.0)-[UnitPriceDiscount]))*[OrderQty],(0.0))
);

-- 4.2
ALTER TABLE dbo.Fact_Orders 
ADD 
	CONSTRAINT FK_ProductID FOREIGN KEY (ProductID) REFERENCES Dim_Product(ProductID),
	CONSTRAINT FK_CustomerID FOREIGN KEY (CustomerID) REFERENCES Dim_Customer(CustomerID);

-- 4.3
INSERT INTO [251526].dbo.Dim_Customer
SELECT C.CustomerID, 
	PP.FirstName, 
	PP.LastName, 
	ST.[Name], 
	ST.[CountryRegionCode], 
	ST.[Group]
FROM AdventureWorks2019.Sales.Customer AS C
	JOIN AdventureWorks2019.Person.Person AS PP
	ON PP.BusinessEntityID = C.PersonID
	JOIN AdventureWorks2019.Sales.SalesTerritory AS ST
	ON ST.TerritoryID = C.TerritoryID;

-- SELECT * FROM [251526].dbo.Dim_Customer;

INSERT INTO [251526].dbo.Dim_Product
SELECT DISTINCT PP.ProductID, 
	PP.[Name], 
	PP.ListPrice, 
	PP.Color,
	PSC.[Name],
	PC.[Name]
FROM AdventureWorks2019.Production.Product AS PP
	JOIN AdventureWorks2019.Production.ProductSubcategory AS PSC
	ON PP.ProductSubcategoryID = PSC.ProductSubcategoryID
	JOIN AdventureWorks2019.Production.ProductCategory AS PC
	ON PSC.ProductCategoryID = PC.ProductCategoryID;

-- SELECT * FROM [251526].dbo.Dim_Product;

INSERT INTO [251526].dbo.Fact_Orders
SELECT SOD.ProductID,
	SOH.CustomerID, 
	SOH.OrderDate, 
	SOH.ShipDate,
	SOD.OrderQty,
	SOD.UnitPrice,
	SOD.UnitPriceDiscount
FROM AdventureWorks2019.Sales.SalesOrderHeader AS SOH
	JOIN AdventureWorks2019.Sales.SalesOrderDetail AS SOD
	ON SOH.SalesOrderID = SOD.SalesOrderID;

--SELECT * FROM [251526].dbo.Fact_Orders;

-- 4.4
SELECT DC.LastName + ', ' + DC.FirstName AS "Nazwisko, imie",
	DP.CategoryName "Kategoria Produktu", 
	DP.[Name] "Nazwa produktu", 
	DP.ListPrice Cena
FROM [251526].dbo.Fact_Orders AS FO
	JOIN [251526].dbo.Dim_Customer AS DC
	ON DC.CustomerID = FO.CustomerID
	JOIN [251526].dbo.Dim_Product AS DP
	ON DP.ProductID = FO.ProductID;