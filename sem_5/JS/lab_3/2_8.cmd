@echo off

set /A "CONT=0"
set /A "MAX=0"

for %%a in (Europe America Asia Oceania Africa) do (
    type Covid.txt | sk 1 6 11 | findStr %%a | findStr "\.05\." | sk 2 | sn >> tmp.txt
    set /p NUM=<tmp.txt

    if !MAX! LSS !NUM! set /A "MAX=NUM" & set "CONT=%%a"
)

echo %MAX%
echo %CONT%