import customtkinter as ctk
from pytube import YouTube
import os

#gui
app = ctk.CTk()
app.geometry("650x800")
app.title("YT Downloader")
app.resizable(False, False)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


label = ctk.CTkLabel(app, text="YouTube URL:",font = ("Arial",20))
label.place(x=240, y=260)

eingabefeld = ctk.CTkEntry(app )
eingabefeld.place(x=240, y=300)


global percent
def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    downloaded = total_size - bytes_remaining
    percent = downloaded / total_size
    progressbar.set(percent)   
    
start_button = ctk.CTkButton(app, text="Download", command=lambda: get_link())
start_button.place(x=390, y=265)

#progressbar
progressbar = ctk.CTkProgressBar(app, width=300)
progressbar.place(x=232, y=380)
progressbar.set(0)
if progressbar.get() ==1.0:
 download_anzeige = ctk.CTkLabel(app, text="Download finished", text_color="green")
 download_anzeige.place(x=300,y=220, anchor="center")
 download_anzeige.after(3000, download_anzeige.destroy)


def get_link():
    global url
    global value
    url = eingabefeld.get()
    yt = YouTube(url, on_progress_callback=progress_func)
    streams = yt.streams
    video_stream = yt.streams.filter(res= optionmenu_var.get(), progressive=True, file_extension="mp4").first()
    audio_stream = yt.streams.filter(only_audio=True).first()
    video_title = yt.title
    os.makedirs("Downloads", exist_ok=True)
    video_stream.download(output_path="Downloads", filename=f"{video_title}.mp4")
    
 
optionmenu_var = ctk.StringVar(value="720p")  

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

auswahlbox = ctk.CTkOptionMenu(master=app,
                                       values=["mp3","360p", "480p", "720p", "1080p", "1440p", "2160p"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
auswahlbox.place(x=390, y=300)



app.mainloop()