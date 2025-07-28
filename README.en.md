# 8BDSS – 8BitDo Screenshot Service

🎮 Take screenshots using the Windows Game Bar combination by pressing the Guide (heart) button on the 8BitDo Ultimate 2C controller in Windows.

## 🚀 Features

- Quickly tap the Guide button → takes a screenshot using `Win + Alt + PrintScreen`
- Hold the Guide button ≥ 0.3s → opens the Xbox Game Bar (`Win + G`)
- Compatible with HDR games since the capture is done via Windows Game Bar
- For games like Genshin Impact that run with Administrator privileges, the tool must also be run as Administrator
- Runs silently in the background, no console window
- Recommended to run with elevated privileges using Windows Task Scheduler
- Minimal CPU and RAM usage (~35–45 MB)

## 📦 Included Files

- `8BDSS.py` – Main Python source code
- `8BDSS.spec` – Optimized PyInstaller build configuration
- `compilar.bat` – Batch script for automatic UPX compilation

## 🛠 Requirements

- **Python 3.10 or higher**
- Install dependencies with:

```bash
pip install pygame keyboard pyinstaller
```

- [Download UPX](https://upx.github.io/) and extract to `C:\Herramientas\upx` (or edit the path in `compilar.bat`)

## ✅ Compilation

Run:

```bash
compilar.bat
```

This will generate the `.exe` inside the `dist/8BDSS/` folder.

This setup uses `--onedir`, which creates a folder with the executable and libraries for better memory efficiency, it can also be compiled using --onefile to pack everything in the exe file.

## 🔄 Auto-run with elevated privileges

To run the program automatically at startup **with Administrator rights**:

1. Press `Win + R`, type `taskschd.msc` and press Enter
2. On the right panel, click **Create Task...**
3. Under the **General** tab:
   - Name the task (e.g., `8BDSS`)
   - Check **Run with highest privileges**
4. Go to the **Triggers** tab and click **New...**:
   - Begin the task: **At log on**
5. In the **Actions** tab, click **New...**:
   - Program/script: browse to the `.exe` inside `dist/8BDSS/`
6. Click OK and restart your PC to test
