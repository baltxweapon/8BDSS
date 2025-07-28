# 8BDSS – 8BitDo Screenshot Service

🎮 Automatiza capturas de pantalla y la Game Bar usando el botón Guía del control 8BitDo en Windows.

## 🚀 Características

- Pulsa rápidamente el botón Guía → toma captura con `Win + Alt + PrintScreen`
- Mantén presionado ≥ 0.3s → abre la Xbox Game Bar (`Win + G`)
- Compatible con juegos HDR (como Genshin Impact)
- Funciona en segundo plano, sin consola
- Uso mínimo de CPU y RAM (~35–45 MB)

## 📦 Archivos incluidos

- `8BDSS.py` – Código fuente principal
- `8BDSS.spec` – Configuración PyInstaller optimizada
- `compilar.bat` – Script de compilación automática con UPX

## 🛠 Requisitos

- Python 3.10+
- pip install pygame keyboard pyinstaller
- [UPX](https://upx.github.io/)

## ✅ Compilación

```bash
compilar.bat
```

Esto generará el `.exe` en `dist/8BDSS/`
