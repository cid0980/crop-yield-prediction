@echo off
setlocal
cd /d "%~dp0"

echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
  echo Failed to create venv. Ensure Python is installed and on PATH.
  exit /b 1
)

echo Activating environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
  echo pip install failed.
  exit /b 1
)

echo Training model...
python src\train.py
if errorlevel 1 (
  echo Training failed.
  exit /b 1
)

echo Setup complete.
echo Launch GUI with: python gui\app.py
