import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys


base_dir = os.path.dirname(os.path.abspath(__file__))
yt_dlp_path = os.path.join(base_dir, "yt-dlp.exe")


def download_audio():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Pon una URL")
        return

    subprocess.run([
        yt_dlp_path,
        "-x",
        "--audio-format",
        "mp3",
        url
    ])
    messagebox.showinfo("Éxito", "Audio descargado correctamente en: " + base_dir)

def download_video():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Pon una URL")
        return

    subprocess.run([yt_dlp_path, url])
    messagebox.showinfo("Éxito", "Video descargado correctamente en: " + base_dir)

def create_ui():
    global entry, download_audio_btn, download_video_btn

    root = tk.Tk()
    root.title("YT-DLP Simple GUI")
    root.geometry("400x150")

    tk.Label(root, text="URL").pack()

    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    download_audio_btn = tk.Button(root, text="Download audio", command=download_audio)
    download_audio_btn.pack(pady=5)

    download_video_btn = tk.Button(root, text="Download video", command=download_video)
    download_video_btn.pack()

    root.mainloop()



if getattr(sys, 'frozen', False):

    base_dir = os.path.dirname(sys.executable)
else:

    base_dir = os.path.dirname(os.path.abspath(__file__))

yt_dlp_path = os.path.join(base_dir, "yt-dlp.exe")
if not os.path.isfile(yt_dlp_path):
    messagebox.showerror(
        "Error",
        f"No se encontró yt-dlp.exe en:\n{base_dir}"
    )
    sys.exit()
else:
    create_ui()
