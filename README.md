# 🌊 Bakio Surf Cleaner  
_A simple but powerful desktop tool for surf schools to automatically clean short video clips._  

![Bakio Surf Cleaner Banner](data/Background.png)

## 🧠 Overview  
**Bakio Surf Cleaner** is a small Python desktop application built with **Tkinter** and **OpenCV**, designed to help surf schools efficiently manage their training footage.  
The app scans a selected folder and **automatically deletes all videos shorter than a chosen duration (in seconds)** — saving time, storage space, and keeping only useful recordings.  

Built originally for the **Bakio Surf School**, this project demonstrates how a lightweight and functional Python app can solve real-world problems in sports training environments.  

---

## ⚙️ Features  
- 🗂️ **Folder selection** — choose any folder containing videos  
- ⏱️ **Automatic filtering** — detects and deletes clips under X seconds  
- 🧹 **Supports multiple formats** — `.mp4`, `.avi`, `.mov`, `.mkv` (case-insensitive)  
- 💬 **User-friendly interface** with buttons, labels, and confirmation messages  
- 🖼️ **Custom branding** — includes school logo and background image  
- 💻 **Cross-platform** — works on Windows, macOS, and Linux  

---

## 🧩 Technologies Used  
| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **Tkinter** | Used for the graphical user interface |
| **OpenCV** | Handles video file processing |
| **OS module** | Interacts with files and directories |
| **FileDialog & MessageBox** | Manages folder selection and alerts |

---

## 🚀 How It Works  
1. Launch the app (`python main.py`)  
2. Enter the **minimum duration** (in seconds) for your videos  
3. Click **“Add Seconds”**  
4. Select the folder you want to clean  
5. The program automatically scans and removes short clips  

✅ When the process finishes, a popup will confirm how many videos were deleted.  

---

## 🧱 Folder Structure  

BakioSurfCleaner/
│
├── data/
│   ├── Background.png
│   └── Logo.png
│
├── main.py
└── README.md

---

## 🏄 About the Project  
Created for **Bakio Surf School** to help organize their surf session videos.  
This small tool was developed in a few hours but has become a daily time-saver for instructors managing hundreds of short clips every week.  

---

## 👨‍💻 Author  
**Alejandro Alonso López**  
Software Developer | Computer Science Student | Surf Enthusiast 🌊  
📍 Aberdeen, Scotland  
🔗 [LinkedIn]([https://www.linkedin.com/in/alejandroalonsolopez](https://www.linkedin.com/in/alejandro-alonso-lopez-b9145b353/)) · [GitHub](https://github.com/alealonso17)

---
