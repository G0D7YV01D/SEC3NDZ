@echo off
mode con lines=30 cols=70
color 02
cls
title Furry pings - Made by VENXM
echo HOE HOE HOE  MERRY CHRISTMASS, NEW UPDATE SOON. DM SGSXM ON INSTA FOR IT
echo.
echo.
echo use at your own risk. i wont be held responsible for your actions
set /p IP=[40;30m [40;31mPEEPS IP Address:[40;35m 
echo.
:cros
PING -n 1 %IP% | FIND "TTL=">nul
IF ERRORLEVEL 1 goto sub
IF NOT ERRORLEVEL 1 goto rcc
:sub
echo  [41;37m%IP%[40;37m) IS [40;33mOFFLINE [40;37m:: [40;31mGONE 
echo.
goto cros
:rcc
echo  [40;37m([40;36m%IP%[40;37m) IS [40;32mONLINE [40;37m:: [40;34mBRO FUCK EM
echo.
goto cros
