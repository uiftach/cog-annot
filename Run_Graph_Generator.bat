@echo off
PowerShell -ExecutionPolicy Bypass -File "%~dp0Run_Graph_Generator.ps1" -Section "%~1"
