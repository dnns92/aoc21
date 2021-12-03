@echo off
mkdir %1

copy template.py %1\%1-1.py
copy template.py %1\%1-2.py
