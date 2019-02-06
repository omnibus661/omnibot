@echo off

IF NOT EXIST import mkdir import

python clean.py %*
python omni.py %*
pause