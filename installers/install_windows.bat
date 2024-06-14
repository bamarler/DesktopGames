@echo off
setlocal

:: Determine the user's desktop path
for /f "tokens=2* delims=:" %%a in ('reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v "Desktop"') do set DESKTOP_PATH=%%b
set INSTALL_PATH=%DESKTOP_PATH%\Desktop Games

:: Create the install directory if it doesn't exist
if not exist "%INSTALL_PATH%" (
    mkdir "%INSTALL_PATH%"
)

:: Download the source code (using GitHub token for private repo access)
:: Replace YOUR_GITHUB_TOKEN with your actual token
curl -L -H "Authorization: token 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" -o "%INSTALL_PATH%\source_code.zip" https://github.com/bamarler/DesktopGames/releases/latest/download/source_code.zip

:: Unzip the source code
tar -xf "%INSTALL_PATH%\source_code.zip" -C "%INSTALL_PATH%"

:: Navigate to the source code directory
cd "%INSTALL_PATH%\DesktopGames-main"

:: Install Python and dependencies (assuming Python is installed)
python -m pip install --upgrade pip
pip install -r requirements.txt

:: Build the game with PyInstaller
pyinstaller DesktopGmaes-win.spec

:: Move the built executable to the install path
move dist\DesktopGames.exe "%INSTALL_PATH%\DesktopGames.exe"

:: Clean up
rd /s /q dist
del "%INSTALL_PATH%\source_code.zip"

echo Game installed successfully at "%INSTALL_PATH%"
pause
endlocal
