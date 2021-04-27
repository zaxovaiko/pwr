-- 1
WITH Group_Year_CTE (Rok, Liczba) 
AS
(
	SELECT YEAR(SOH.OrderDate), COUNT(SOH.OrderDate)
	FROM Sales.SalesOrderHeader AS SOH
	GROUP BY YEAR(SOH.OrderDate)
),
Group_Territory_CTE (Rok, Liczba, TerritoryID) 
AS 
(
	SELECT YEAR(SOH.OrderDate), COUNT(*), TerritoryID
	FROM Sales.SalesOrderHeader AS SOH
	GROUP BY YEAR(SOH.OrderDate), TerritoryID
)
SELECT 
	GYC.Rok,
	GYC.Liczba "Liczba zamowien",
	ST.[Name] Terytorium,
	GTC.Liczba "Liczba zam. na terytorium",
	FORMAT(GTC.Liczba * 100.0 / GYC.Liczba, '###.##') AS "% udzial"
FROM Group_Year_CTE AS GYC
	JOIN Group_Territory_CTE AS GTC ON GTC.Rok = GYC.Rok 
	JOIN Sales.SalesTerritory AS ST ON GTC.TerritoryID = ST.TerritoryID
ORDER BY Rok;

-- 2
SELECT *, FORMAT("Liczba zam. na terytorium" * 100.0 / "Liczba zamowien", '###.##') AS "% udzial"
FROM (
	SELECT DISTINCT
		YEAR(soh.OrderDate) Rok,
		COUNT(soh.OrderDate) OVER(PARTITION BY YEAR(soh.OrderDate)) "Liczba zamowien",
		ST.[Name] Terytorium,
		COUNT(soh.OrderDate) OVER (PARTITION BY ST.[Name], YEAR(soh.OrderDate)) "Liczba zam. na terytorium"
	FROM Sales.SalesOrderHeader AS soh
		JOIN Sales.SalesTerritory AS ST 
		ON ST.TerritoryID = soh.TerritoryID
) AS A
ORDER BY Rok;
