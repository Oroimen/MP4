ChatGPT Plus
# 🎥 Convertidor Universal de Video (MP4 ⇄ iPhone y más)

Este proyecto es un convertidor de videos universal y multiplataforma escrito en **Python**, que permite:

- Convertir videos de **iPhone (.mov) → MP4**
- Convertir videos de **MP4 → iPhone (.mov)**
- Convertir **cualquier video compatible con FFmpeg** a cualquier formato (mp4, mov, avi, mkv, flv, wmv, webm, m4v, etc.)
- Menú interactivo
- ASCII ART incluido
- Uso de **FFmpeg** para máxima compatibilidad

---

## 🚀 Requisitos

### 1. Python 3

Descargar:  
https://www.python.org/downloads/

Verificar:

```bash
python --version

2. FFmpeg
Windows (PowerShell)
winget install Gyan.FFmpeg


O:

choco install ffmpeg

macOS
brew install ffmpeg

Linux (Debian/Ubuntu)
sudo apt install ffmpeg


Verificar:

ffmpeg -version

3. Librerías de Python

El script usa solo librerías estándar (os, subprocess).

Opcional:

pip install moviepy

📦 Instalación del Proyecto
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO

▶️ Ejecución del Convertidor
python convertidor.py


Menú:

1) De iPhone (.mov) → MP4
2) De MP4 → iPhone (.mov)
3) Convertir a cualquier formato (universal)
4) Salir

🔹 Ejemplo (Conversión Universal)
Nombre del archivo de video: ejemplo.avi
Formato de salida (ej. mp4, mov, mkv, flv, wmv, webm, m4v): mp4


Salida:

ejemplo.mp4

🧠 Cómo Funciona

libx264 para video

aac para audio

yuv420p para compatibilidad

+faststart para MP4 optimizado

📁 Archivos Aceptados
Tipo	Extensión	Dirección
Video iPhone	.mov	.mov → .mp4
Video MP4	.mp4	.mp4 → .mov
Otros formatos	.avi, .mkv, .flv, .wmv, .webm, .m4v	Conversión universal
✨ ASCII ART
 __  __ _____ ____    ____                  _             
|  \/  | ____|  _ \  / ___|___  _ __   ___| |_ ___  _ __ 
| |\/| |  _| | | | | | |   / _ \| '_ \ / _ \ __/ _ \| '__|
| |  | | |___| |_| | | |__| (_) | | | |  __/ || (_) | |   
|_|  |_|_____|____/   \____\___/|_| |_|\___|\__\___/|_|   

                   MP4 CONVERTIDOR

🛠 Mejoras Futuras

Soporte para más formatos

Barra de progreso

Interfaz gráfica

Versión .EXE

Conversión masiva

💬 Soporte

Para ayuda, abre un issue o un pull request.
