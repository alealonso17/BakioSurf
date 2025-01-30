import os # Para interactuar con el sistema y los archivos 
import cv2 # Para trabajar con videos 
import tkinter as tk # Para la app
from tkinter import filedialog, messagebox #Para abrir dialogogs y mostrar mensajes
from tkinter import PhotoImage #Para cargar una imagen de fondo de pantalla 

def select_folder(): # Simple function that asks for choosing a media directory 
    folder_path = filedialog.askdirectory()  # For choosing a directory 
    print(f"Directory selected correctly✅ --->  {folder_path}")
    if folder_path: # if directory chosen 
        delete_short_videos(folder_path) # Calls the function delete short videos with that path as a paramenter  

def delete_short_videos(folder_path): #Function in which you give it a directory and deletes the sort videos of that directory 
    for filename in os.listdir(folder_path):# for each file ....
        print(f"📂 Analizando archivo: {filename}") #Print for checking if works until this point 
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv','.MP4', '.AVI', '.MOV', '.MKV')): #If file is a video .... 
            file_path = os.path.join(folder_path, filename) #gets the full path of the file 
            try: # tries open the  video and extract ... 
                video = cv2.VideoCapture(file_path) #Almacenar el video en 'video'
                #See if video is oppened 
                if not video.isOpened():
                    print(f"🚫 No se pudo abrir el archivo: {file_path}")
                    continue
                else:
                    print(f"✅ Archivo abierto correctamente: {file_path}") 


                #Extract fps and frame count 
                fps = video.get(cv2.CAP_PROP_FPS) # Extracts The fps count of the video 
                frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) # The frame count
                print(f"📏 FPS: {fps}, Frame Count: {frame_count} for {filename}") #Print for debbuging 


                
                
                if fps > 0:  # Only calculate duration if FPS is valid
                    duration = frame_count / fps
                    print(f"⏱️ Duración de {filename}: {duration:.2f} segundos")
                else:
                    print(f"⚠️ FPS inválido para {filename}, no se puede calcular la duración.")
                    video.release()
                    continue


                
                video.release()
                if duration < 4: # If the duration is < 3 ;
                    os.remove(file_path) #remove the fil 
                    print(f"Deleted: {file_path}") #Show that u removed the file 
            except Exception as e: #An error in case something bad happens 
                print(f"Error processing {file_path}: {e}") #Print the error for data
        else : print(f"🚫 El archivo {filename} no es un video ! ")
    messagebox.showinfo("Done", "Short videos deleted successfully.") #once for loop finishes , print message that was done correctly 


# App interface ---------------------------------------------------------------------------------------------------------------------------

app = tk.Tk()#Create the window
app.title("BAKIO SURF CLEANER")#Tittle of the window 

#Background configuration -------------------> 

current_directory = os.path.dirname(os.path.abspath(__file__)) #load the curreent directory of the script 
Background_image_path = os.path.join(current_directory, 'Background.png')#Say that the background image is always going to be with the script , so incase the folder moves for expample from desktop to documents , the file is still findable 


Background_image = tk.PhotoImage(file=Background_image_path)#Storage the image for the background 
Background_label = tk.Label(app, image = Background_image) #Create a label with the image 
Background_label.place(relwidth=1, relheight=1) # This makes that the background is full screen 


#Load Company logo 
logo_image_path = os.path.join(current_directory, 'Logo.png')#Say that the background image is always going to be with the script , so incase the folder moves for expample from desktop to documents , the file is still findable 
logo_image = tk.PhotoImage(file=logo_image_path)#Load image 
logo_label = tk.Label(app, image = logo_image)#Make it into a label 
logo_label.pack(padx=10, pady=10)#print the label in that position  (x,y) 


title_label = tk.Label(app, text="🌊 Bakio Surf Cleaner 🌊", font=("Times New Roman", 50), fg="yellow") #Tittle Showed on screen
title_label.pack(pady=10)#Where is the title 

sub_label = tk.Label(app, text="Selecciona la carpeta que quieres limpiar de clips cortos", font=("Times New Roman",20 ),fg='white') #INtructions 
sub_label.pack(pady=30, padx=10 )#Print instructions 

select_button = tk.Button(app, text="Select Folder", command=select_folder) # In the button we call the function for selecting the file 
select_button.pack(pady=200)#Position of the button 

app.geometry("900x900")#window dimension
app.mainloop()  # to start the app 




