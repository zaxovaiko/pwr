@echo OFF
set /A SUM=0
set T=%time%

echo > tmp.txt
for /F "delims=\t" %%L in (Covid.txt) do (
    for /F "tokens=5" %%A in ("%%L") do (
        set /A "SUM+=%%A"
    )
)

echo %SUM%
echo %time% - %T% 