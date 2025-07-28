# 8BDSS – 8BitDo Screenshot Service

🎮 Toma capturas de pantalla utilizando la combinación de la Game Bar de Windows con solo presionar el botón Guía (corazón) del control 8BitDo Ultimate 2C en Windows.

## 🚀 Características

- Pulsa rápidamente el botón Guía → toma una captura con `Win + Alt + PrintScreen`
- Mantén presionado el botón Guía ≥ 0.3s → abre la Xbox Game Bar (`Win + G`)
- Compatible con juegos HDR (la captura se realiza a través de Game Bar)
- Para juegos como Genshin Impact (que se ejecutan como administrador), este script también debe ejecutarse como administrador
- Se ejecuta en segundo plano de forma silenciosa (sin consola)
- Recomendado para ejecutarse con privilegios elevados usando el Programador de tareas de Windows
- Uso mínimo de CPU y RAM (~35–45 MB)

## 📦 Archivos incluidos

- `8BDSS.py` – Código fuente principal
- `8BDSS.spec` – Configuración optimizada para PyInstaller
- `compilar.bat` – Script por lotes para compilar automáticamente con UPX

## 🛠 Requisitos

- **Python 3.10 o superior**
- Instalar dependencias con:

```bash
pip install pygame keyboard pyinstaller
```

- [Descargar UPX](https://upx.github.io/) y extraerlo en `C:\Herramientas\upx` (o cambiar la ruta en `compilar.bat`)

## ✅ Compilación

Ejecuta:

```bash
compilar.bat
```

Esto generará el `.exe` dentro de la carpeta `dist/8BDSS/`.

Este setup usa `--onedir`, lo que crea una carpeta con el ejecutable y sus librerías, permitiendo mejor rendimiento y menor consumo de RAM aunque tambien se puede modificar y compilar con --onefile para empaquetar todo dentro del ejecutable.

## 🔄 Ejecución automática con privilegios elevados

Para que se ejecute con Windows (y tenga privilegios de administrador):

1. Presiona `Win + R`, escribe `taskschd.msc` y presiona Enter.
2. En el panel derecho, haz clic en **Crear tarea...**
3. En la pestaña **General**:
   - Escribe un nombre (ej. `8BDSS`)
   - Marca la casilla **Ejecutar con los privilegios más altos**
4. En la pestaña **Desencadenadores**, haz clic en **Nuevo...**:
   - Comienza la tarea: **Al iniciar sesión**
5. En la pestaña **Acciones**, clic en **Nuevo...**:
   - Programa/script: navega al `.exe` generado dentro de `dist/8BDSS/`
6. Acepta todo y reinicia para probar.
