@echo off

set /p params="Enter parameters: "

cd cmake-build-debug && kp.exe %params%

:: save return code from exe
:: remove /s from string
set code=%errorlevel%
set num=%params:/s =%

if %code% lss 10 (
    echo Przekazano: %num%
    goto exit
)

if %code% equ 11 (
    echo Brak parametrow
    goto exit
)

if %code% equ 12 (
    echo Parameter %num% nie jest cyfra
    goto exit
)

if %code% equ 13 (
    echo Niewlasciwa wartosc parametru %num%
)

:exit