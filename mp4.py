import subprocess
import os

ASCII_ART = r"""
 __  __ _____ ____    ____                  _             
|  \/  | ____|  _ \  / ___|___  _ __   ___| |_ ___  _ __ 
| |\/| |  _| | | | | | |   / _ \| '_ \ / _ \ __/ _ \| '__|
| |  | | |___| |_| | | |__| (_) | | | |  __/ || (_) | |   
|_|  |_|_____|____/   \____\___/|_| |_|\___|\__\___/|_|   

                   MP4 CONVERTIDOR
"""
# Extensiones comunes para referencia, no limitante
COMMON_FORMATS = [
    "mp4", "mov", "avi", "mkv", "flv", "wmv", "webm", "m4v"
]

def convert_video(input_file, output_format):
    if not os.path.exists(input_file):
        print(f"❌ El archivo '{input_file}' no existe. :( ")
        return

    base, _ = os.path.splitext(input_file)
    output_file = f"{base}.{output_format}"

    # Comando FFmpeg genérico
    cmd = [
        "ffmpeg", "-i", input_file,
        "-c:v", "libx264",      # Video H.264
        "-c:a", "aac",          # Audio AAC
        "-pix_fmt", "yuv420p",  # Compatible con la mayoría de reproductores
        "-movflags", "+faststart",  # Optimizado para MP4/MOV
        output_file
    ]

    print(f"\nConvirtiendo {input_file} → {output_file} ...\n")
    subprocess.run(cmd)
    print("\n✅ Conversión completa.\n")


def menu():
    print(ASCII_ART)
    print("Formato de entrada: cualquier archivo de video compatible con FFmpeg")
    print("Formato de salida: mp4, mov, avi, mkv, flv, wmv, webm, m4v, etc.\n")

    input_file = input("Nombre del archivo de video: ").strip()
    output_format = input("Formato de salida deseado (ej. mp4): ").strip().lower()

    if not output_format:
        print("❌ Debes ingresar un formato de salida válido.")
        return

    convert_video(input_file, output_format)

    input("\nPresiona ENTER para continuar....")
    menu()


if __name__ == "__main__":
    menu()
