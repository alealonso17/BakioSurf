import os
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        delete_short_videos(folder_path)

def delete_short_videos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            file_path = os.path.join(folder_path, filename)
            try:
                video = cv2.VideoCapture(file_path)
                fps = video.get(cv2.CAP_PROP_FPS)
                frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
                duration = frame_count / fps
                video.release()
                if duration < 3:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    messagebox.showinfo("Done", "Short videos deleted successfully.")

app = tk.Tk()
app.title("BAKIO SURF ")

select_button = tk.Button(app, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

title_label = tk.Label(app, text="Bakio Surf", font=("Helvetica", 24), fg="yellow")
title_label.pack(pady=10)

app.geometry("400x300")
app.mainloop()