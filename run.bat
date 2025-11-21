@echo off
cd /d %~dp0
call python -m venv venv
call venv\Scripts\activate
call pip install -r .\requirements.txt
python -m oceanic.index
pause