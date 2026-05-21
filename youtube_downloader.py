import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading

#  FUNCTIONS 

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)

def download_video():
    url = url_var.get()
    save_path = path_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    if not save_path:
        messagebox.showerror("Error", "Please select a download folder")
        return

    status_label.config(text="Downloading video...", fg="#00C897")
    progress_bar.start()

    threading.Thread(target=start_download, args=(url, save_path), daemon=True).start()

def start_download(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        progress_bar.stop()

        status_label.config(
            text="Download Completed Successfully ✓",
            fg="#00FF99"
        )

        messagebox.showinfo(
            "Success",
            "Your video has been downloaded successfully!"
        )

    except Exception as e:
        progress_bar.stop()

        status_label.config(
            text="Download Failed ✗",
            fg="red"
        )

        messagebox.showerror("Error", str(e))

#  MAIN WINDOW 

root = tk.Tk()
root.title("YouTube Downloader App")
root.geometry("760x500")
root.config(bg="#0F172A")
root.resizable(False, False)


#  VARIABLES 

url_var = tk.StringVar()
path_var = tk.StringVar()

#  HEADER 

header_frame = tk.Frame(root, bg="#111827", height=90)
header_frame.pack(fill="x")

company_label = tk.Label(
    header_frame,
    text="Avnish Ojha",
    font=("Segoe UI", 24, "bold"),
    bg="#111827",
    fg="#38BDF8"
)
company_label.pack(pady=(15, 0))

subtitle_label = tk.Label(
    header_frame,
    text="Professional YouTube Media Downloader",
    font=("Segoe UI", 11),
    bg="#111827",
    fg="#CBD5E1"
)
subtitle_label.pack()

#  MAIN CARD 

main_frame = tk.Frame(
    root,
    bg="#1E293B",
    bd=0
)
main_frame.pack(padx=40, pady=35, fill="both", expand=True)

#  URL SECTION 

url_title = tk.Label(
    main_frame,
    text="Enter YouTube Video URL",
    font=("Segoe UI", 12, "bold"),
    bg="#1E293B",
    fg="white"
)
url_title.pack(anchor="w", padx=30, pady=(30, 8))

url_entry = tk.Entry(
    main_frame,
    textvariable=url_var,
    font=("Segoe UI", 12),
    width=65,
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief="flat"
)
url_entry.pack(ipady=8, padx=30)

#  FOLDER SECTION 

folder_title = tk.Label(
    main_frame,
    text="Select Download Folder",
    font=("Segoe UI", 12, "bold"),
    bg="#1E293B",
    fg="white"
)
folder_title.pack(anchor="w", padx=30, pady=(25, 8))

folder_frame = tk.Frame(main_frame, bg="#1E293B")
folder_frame.pack(padx=30, fill="x")

folder_entry = tk.Entry(
    folder_frame,
    textvariable=path_var,
    font=("Segoe UI", 11),
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief="flat",
    width=48
)
folder_entry.pack(side="left", ipady=8)

browse_btn = tk.Button(
    folder_frame,
    text="Browse",
    command=browse_folder,
    font=("Segoe UI", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=7,
    cursor="hand2"
)
browse_btn.pack(side="left", padx=10)

#  DOWNLOAD BUTTON 

download_btn = tk.Button(
    main_frame,
    text="⬇ Download Video",
    command=download_video,
    font=("Segoe UI", 13, "bold"),
    bg="#10B981",
    fg="white",
    activebackground="#059669",
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2"
)
download_btn.pack(pady=35)

#  PROGRESS BAR 

style = ttk.Style()
style.theme_use('clam')

style.configure(
    "Custom.Horizontal.TProgressbar",
    troughcolor="#334155",
    background="#38BDF8",
    bordercolor="#334155",
    lightcolor="#38BDF8",
    darkcolor="#38BDF8"
)

progress_bar = ttk.Progressbar(
    main_frame,
    style="Custom.Horizontal.TProgressbar",
    mode='indeterminate',
    length=500
)
progress_bar.pack(pady=10)

#  STATUS LABEL 

status_label = tk.Label(
    main_frame,
    text="Ready to download",
    font=("Segoe UI", 11),
    bg="#1E293B",
    fg="#94A3B8"
)
status_label.pack(pady=10)

#  FOOTER 

footer_label = tk.Label(
    root,
    text="Powered by Avnish Ojha © 2026",
    font=("Segoe UI", 9),
    bg="#0F172A",
    fg="#64748B"
)
footer_label.pack(pady=10)

#  RUN APP 

root.mainloop()