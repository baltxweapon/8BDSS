# 8BDSS – 8BitDo Screenshot Service

🎮 Automates screenshots and Xbox Game Bar control using the Guide button on your 8BitDo controller in Windows.

## 🚀 Features

- Quickly tap the Guide button → takes a screenshot using `Win + Alt + PrintScreen`
- Hold the Guide button ≥ 0.3s → opens Xbox Game Bar (`Win + G`)
- Compatible with HDR games (like Genshin Impact)
- Runs silently in the background, no console window
- Minimal CPU and RAM usage (~35–45 MB)

## 📦 Included Files

- `8BDSS.py` – Main Python source code
- `8BDSS.spec` – Optimized PyInstaller build configuration
- `compilar.bat` – Batch script for compiling with UPX

## 🛠 Requirements

- Python 3.10+
- pip install pygame keyboard pyinstaller
- [UPX](https://upx.github.io/)

## ✅ Compilation

```bash
compilar.bat
```

This will generate the `.exe` inside `dist/8BDSS/`
