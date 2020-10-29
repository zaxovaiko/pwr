@echo off

for %%a in (Europe America Africa Asia Oceania) do (
    echo %%a
    type Covid.txt | sk 5 11 | findStr %%a | sk 1 | sn
)