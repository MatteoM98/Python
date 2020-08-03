import tkinter as tk
from tkinter import messagebox
import application
import os


class Root(tk.Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("YT Downloader")
        self.configure(background = "#4D4D4D")
        self.minsize(700, 100)
        self.maxsize(700,100);
        self.createwidget()

    def buttonevent(self,txu,txf,txp):
        if not os.path.exists("/usr/bin/youtube-dl"):
            print("Necessario installare youtube-dl")
            print("Installazione yotube-dl")
            os.system("sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o "
                      "/usr/local/bin/youtube-dl")
            os.system("sudo chmod a+rx /usr/local/bin/youtube-dl")
        if not os.path.exists("/usr/bin/ffmpeg"):
            print("Necessario installare ffmpeg")
            print("Installazione ffmpeg")
            os.system("sudo apt-get install ffmpeg")
        tu = txu.get()
        tf = txf.get()
        tp = txp.get()
        command = "youtube-dl --extract-audio --audio-format \"" + str(tf) + "\" " + str(tu)
        os.system(command)
        os.system("mv *." + str(tf) + " " + str(tp))
        print("mv *." + str(tf) + " " + str(tp))
        messagebox.showinfo("Completato", "Download completato")

    def createwidget(self):
        url = tk.Label(self, text="Inserire URL video YT: ")
        url.configure(background = "#4D4D4D", foreground = "white")
        url.grid(column=0, row=0)
        texturl = tk.Entry(self, width = 50)
        texturl.grid(row=0, column=100)

        form = tk.Label(self, text=" Inserire formato audio: ")
        form.configure(background="#4D4D4D", foreground="white")
        form.grid(column = 0, row = 300)
        textform = tk.Entry(self, width=50)
        textform.grid(row=300, column=100)

        path = tk.Label(self, text="Inserire path di salvataggio: ")
        path.configure(background="#4D4D4D", foreground="white")
        path.grid(column=0, row=600)
        textpath = tk.Entry(self, width=50)
        textpath.grid(row=600, column=100)

        button = tk.Button(self, text="Scarica", command=lambda: self.buttonevent(texturl,textform,textpath))
        button.grid(row=800, column=100)




root = Root()
root.mainloop()


