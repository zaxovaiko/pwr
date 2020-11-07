@echo OFF
set /P COUNTRY="Enter country: "
set /A SUM=0
set T=%time%

echo > tmp.txt
for /F "delims=\t" %%L in ('findStr %COUNTRY% Covid.txt') do (
    for /F "tokens=5" %%A in ("%%L") do (
        set /A "SUM+=%%A"
    )
)

echo %SUM%
echo %time% - %T% 