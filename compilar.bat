@echo off
set UPX_PATH=C:\Herramientas\upx
pyinstaller --noconsole --onedir --upx-dir "%UPX_PATH%" 8BDSS.spec
pause
