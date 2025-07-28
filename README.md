# 8BDSS – 8BitDo Screenshot Service

🎮 Realiza capturas de pantalla con la combinacíón de botones de Windows Game Bar usando el botón Guía (corazón) del control 8BitDo Ultimate 2C en Windows.

## 🚀 Características

- Pulsa rápidamente el botón Guía → toma captura con `Win + Alt + PrintScreen`
- Mantén presionado ≥ 0.3s → abre la Xbox Game Bar (`Win + G`)
- Compatible con juegos HDR ya que la captura se hace a través de WGB
- Para juegos como Genshin Impact que corren como Administrador, la herramienta debe ejecutarse como Administrador tambien.
- Funciona en segundo plano, sin consola (se recomienda ejecutar con persmisos elevados desde el Programador de tareas de Windows)
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

Al compilar desde fuente se utiliza --onedir, lo cual genera el ejecutable y la carpeta de instalación, lo cual ahorra un poco de RAM.
