@echo off
echo Building clicker.exe...
pyinstaller --onefile --noconsole --name "clicker" main.py
echo.
echo Build completed!
echo Executable: dist\clicker.exe
pause
