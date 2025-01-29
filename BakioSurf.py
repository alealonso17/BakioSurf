import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        delete_short_videos(folder_path)

def delete_short_videos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            file_path = os.path.join(folder_path, filename)
            try:
                video = VideoFileClip(file_path)
                if video.duration < 3:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    messagebox.showinfo("Done", "Short videos deleted successfully.")

app = tk.Tk()
app.title("Delete Short Videos")

select_button = tk.Button(app, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

app.mainloop()