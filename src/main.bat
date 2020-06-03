@echo off
SET mypath=%~dp0
echo %mypath:~0,-1%
cd %mypath%
"C:\Python_Environments\py37_web\python.exe" "%mypath%\main.py"
pause