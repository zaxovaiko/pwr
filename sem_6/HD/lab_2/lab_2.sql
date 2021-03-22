-- 1.1
SELECT DISTINCT YEAR(OrderDate) FROM Sales.SalesOrderHeader;

-- 1.2
SELECT SalesOrderID, YEAR(OrderDate) as "Year", TotalDue 
	FROM Sales.SalesOrderHeader 
	WHERE YEAR(OrderDate) = (
		SELECT MIN(YEAR(OrderDate)) FROM Sales.SalesOrderHeader
	);

-- 1.3
SELECT YEAR(OrderDate) as "Year", MONTH(OrderDate) as "Month", SalesOrderID, TotalDue
	FROM Sales.SalesOrderHeader 
	WHERE MONTH(OrderDate) = 5; 

-- 2.1 without CTE
SELECT CustomerID as "klientId", 
	LastName + ', ' + FirstName as "Nazwisko, imie", 
	COUNT(SalesOrderID) as "Liczba zamowien"
FROM Sales.SalesOrderHeader 
JOIN Person.Person ON Sales.SalesOrderHeader.CustomerID = Person.BusinessEntityID
GROUP By CustomerID, LastName, FirstName
HAVING COUNT(SalesOrderID) > 25;

-- 2.1 with CTE
WITH clientsCTE ( klientId, "Nazwisko, imie", "Liczba zamowien") 
AS (
	SELECT S.CustomerID as "klientId", P.LastName + ', ' + P.FirstName as "Nazwisko, imie", 
	COUNT(S.SalesOrderID) as "Liczba zamowien"
	FROM Sales.SalesOrderHeader as S
	JOIN Person.Person P ON S.CustomerID = P.BusinessEntityID
	GROUP By S.CustomerID, P.LastName, P.FirstName
	HAVING COUNT(S.SalesOrderID) > 25
)

SELECT klientId, "Nazwisko, imie", "Liczba zamowien" FROM clientsCTE ORDER BY 3 DESC;

-- 2.2
SELECT SR.[Name] as "Nazwa", COUNT(SR.[Name]) as "Powod"
	FROM Sales.SalesOrderHeaderSalesReason as OSR
	JOIN Sales.SalesReason as SR
	ON OSR.SalesReasonID = SR.SalesReasonID
	GROUP BY SR.[Name]
	ORDER BY COUNT(SR.[Name]) DESC;

-- 3
SELECT * FROM ( 
	SELECT SalesPersonId, CustomerID, TotalDue, YEAR(OrderDate) AS "Year"
		FROM Sales.SalesOrderHeader 
		WHERE SalesPersonId IS NOT NULL
		GROUP BY CustomerID, SalesPersonId, TotalDue, YEAR(OrderDate)	
) SalesResult
PIVOT (
	SUM([TotalDue])
	FOR [Year] in ([2011], [2012], [2013], [2014])
) AS P;

-- Dynamic
DECLARE @year VARCHAR (1000) = (
SELECT STRING_AGG (CONCAT(CONVERT(VARCHAR(1),'['), [Year],CONVERT(VARCHAR(1),'[')), ',')
FROM (SELECT DISTINCT [Year] = YEAR (OrderDate) 
   FROM Sales.SalesOrderHeader) Y)
SELECT @year

DECLARE @year VARCHAR (1000) = (
	SELECT STRING_AGG(CONCAT(CONVERT(VARCHAR(1), '['), CONVERT(VARCHAR(4), [Year]), CONVERT(VARCHAR(1), ']')), ',')
	FROM (SELECT DISTINCT [Year] = YEAR (OrderDate) 
	FROM Sales.SalesOrderHeader) Y
)

DECLARE @SQL_EX VARCHAR (2000) = (
	'SELECT CustomerID, ' + @year + '
	FROM ( 
		SELECT CustomerID, TotalDue, YEAR(OrderDate) AS "Year"
		FROM Sales.SalesOrderHeader 
		WHERE SalesPersonId IS NOT NULL
		GROUP BY CustomerID, TotalDue, YEAR(OrderDate)  
	) SalesResult
	PIVOT (
	  AVG([TotalDue])
	  FOR [Year] in ('+ @year+')
	) AS P;'
);

EXEC (@SQL_EX);

-- 4.1
SELECT * FROM ( 
	SELECT CustomerID, TotalDue, YEAR(OrderDate) AS "Year"
		FROM Sales.SalesOrderHeader 
		WHERE SalesPersonId IS NOT NULL
		GROUP BY CustomerID, TotalDue, YEAR(OrderDate)	
) SalesResult
PIVOT (
	AVG([TotalDue])
	FOR [Year] in ([2011], [2012], [2013], [2014])
) AS P;

-- 4.2
SELECT CustomerID,  
	AVG(CASE WHEN YEAR(OrderDate) = 2011 THEN [TotalDue] END) "2011", 
	AVG(CASE WHEN YEAR(OrderDate) = 2012 THEN [TotalDue] END) "2012",
	AVG(CASE WHEN YEAR(OrderDate) = 2013 THEN [TotalDue] END) "2013",
	AVG(CASE WHEN YEAR(OrderDate) = 2014 THEN [TotalDue] END) "2014"
   FROM Sales.SalesOrderHeader
   GROUP BY CustomerID
	ORDER BY CustomerID;
