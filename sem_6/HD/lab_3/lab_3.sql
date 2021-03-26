-- 1
SELECT MIN(PP.LastName + ', ' + PP.FirstName) Pracownik, 
	SOH.SalesPersonID pracID, 
	YEAR(SOH.OrderDate) "Rok zamowienia", 
	SUM(SOH.SubTotal) Kwota, 
	COUNT(SOH.SalesOrderID) "Liczba zamowien"
FROM Sales.SalesOrderHeader AS SOH
	JOIN Person.Person AS PP
	ON PP.BusinessEntityID = SOH.SalesPersonID
GROUP BY YEAR(SOH.OrderDate), SOH.SalesPersonID
ORDER BY pracID, "Rok zamowienia";

-- 2
SELECT DISTINCT PP.LastName + ', ' + PP.FirstName Pracownik, 
		SOH.SalesPersonID pracID, 
		YEAR(SOH.OrderDate) "Rok zamowienia", 
		SUM(SOH.SubTotal) OVER(PARTITION BY SOH.SalesPersonID, YEAR(SOH.OrderDate)) Kwota, 
		COUNT(SOH.SalesOrderID) OVER(PARTITION BY SOH.SalesPersonID, YEAR(SOH.OrderDate)) "Liczba zamowien"
FROM Sales.SalesOrderHeader AS SOH
	INNER JOIN Person.Person AS PP
	ON PP.BusinessEntityID = SOH.SalesPersonID
ORDER BY 2, 3;

-- 4
--CREATE DATABASE [251526];

--CREATE TABLE Dim_Customer (
--	CustomerID INT NOT NULL CONSTRAINT PK_Dim_Customer PRIMARY KEY,
--	FirstName NVARCHAR(50) NOT NULL,
--	LastName NVARCHAR(50) NOT NULL,
--	TerritoryName NVARCHAR(50) NOT NULL,
--	CountryRegionCode NVARCHAR(3) NOT NULL,
--	"Group" NVARCHAR(50) NOT NULL
--);