@echo off
echo =================== hiBuddy Packages Installer ======================
echo.
echo      Press Enter to install Python 3 and the ping3 Python package
pause > nul

echo.
echo ===================== Installing Python... ==========================
echo.
curl -o python_installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
start /wait python_installer.exe /quiet PrependPath=1
del python_installer.exe

echo.
echo =================== Installing ping3 package... =====================
echo.
python -m pip install ping3

echo.
echo =================== Installing art package... =====================
echo.
python -m pip install art

echo.
echo ==================== Installation completed. ========================
pause
