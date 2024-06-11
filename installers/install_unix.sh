#!/bin/bash

# Set the path where the game will be installed
INSTALL_PATH="$HOME/Desktop/Desktop Games"

# Create the install directory if it doesn't exist
mkdir -p "$INSTALL_PATH"

# Download the source code (using GitHub token for private repo access)
# Replace YOUR_GITHUB_TOKEN with your actual token
curl -L -H "Authorization: token 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" -o "$INSTALL_PATH/source_code.zip" https://github.com/bamarler/DesktopGames/releases/latest/download/source_code.zip

# Unzip the source code
unzip "$INSTALL_PATH/source_code.zip" -d "$INSTALL_PATH"

# Navigate to the source code directory
cd "$INSTALL_PATH/DesktopGames-main"

# Install Python and dependencies (assuming Python is installed)
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# Build the game with PyInstaller
pyinstaller --onefile --name DesktopGames src/main.py

# Move the built executable to the install path
mv dist/DesktopGames "$INSTALL_PATH/DesktopGames"

# Clean up
rm -rf dist
rm "$INSTALL_PATH/source_code.zip"

echo "Game installed successfully at $INSTALL_PATH"
