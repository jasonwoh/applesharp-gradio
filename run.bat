@echo off
:: 1. Set the path to your Anaconda installation
:: Usually it is in %UserProfile%\anaconda3 or %UserProfile%\miniconda3
set CONDAPATH=%UserProfile%\anaconda3

:: 2. Activate the Conda environment and run the script
call %CONDAPATH%\Scripts\activate.bat sharp
cd /d "%~dp0"
python gui.py

:: 3. Keep the window open if it crashes so you can read the error
pause