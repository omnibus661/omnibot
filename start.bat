@echo off

IF NOT EXIST import mkdir import
REM IF NOT EXIST export mkdir export

python clean.py %*
python omni.py %*

pause