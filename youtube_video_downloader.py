import time
import tkinter as tk
import tkinter.font as tkfont
from PIL import Image, ImageTk
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog
import os

class Ytubedownload:
    def __init__(self, root):
        self.root = root
        self.path_name = ""
        self.root.resizable(width=0, height=0)
        def get_path():

            self.path_name = filedialog.askdirectory()
            abc = self.enter_path_entry.get()
            self.enter_path_entry.delete(0,'end')
            self.enter_path_entry.insert(0, self.path_name)

        self.root.title("Youtube Video Downloader")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight() -60

        self.root.geometry("%dx%d+0+0"%(width,height))

        self.bg = ImageTk.PhotoImage(file="bg_image.jpg")  #if you are reading this code in github so download this image from this repository only or https://github.com/NitinSingh8/N-Programmer/blob/main/bg_image.jpg
        self.tk_bg = tk.Label(self.root, image=self.bg)
        self.tk_bg.place(x=700, y=0, relwidth=1, relheight=1)

        self.fontstyle = tkfont.Font(family="Lucida Grande", size=15)
        self.heading = tk.Label(self.root, text="Youtube Video Downloader", font=("oblique",30),bg='black',fg="white", padx="50").place(x=500,y=0)
        self.heading = tk.Label(self.root, text="~    Nitin Singh", font=("oblique", 30), fg='black',padx="50").place(x=1000, y=50)

        self.enter_link_label = tk.Label(self.root, text="Enter the link here  ", font=self.fontstyle, padx="50").grid(row=0, column=0, padx=50, pady=(70, 0))
        self.enter_link_entry = tk.Entry(self.root, width=30, borderwidth=5)
        self.enter_link_entry.grid(row=0, column=1, padx=25, pady=(70, 0))

        self.enter_path_label1 = tk.Label(self.root, text="Choose the path ", font=self.fontstyle, padx="50").grid(
            row=1, column=0, padx=50, pady=(50, 0))
        self.enter_path_button = tk.Button(self.root, text="Browse", width=20, borderwidth=5, command=get_path)
        self.enter_path_button.grid(row=1, column=1, padx=25, pady=(50, 0))

        self.enter_path_label2 = tk.Label(self.root, text="Enter the path ", font=self.fontstyle, padx="50").grid(row=2,column=0,padx=50,pady=(50,0))
        self.enter_path_entry = tk.Entry(self.root, text="hello", width=30, borderwidth=5)
        self.enter_path_entry.grid(row=2, column=1, padx=25, pady=(50, 0))

        self.quality_list = tk.LabelFrame(self.root)
        self.quality_list.place(x=50, y=310)

        self.quality_val = tk.IntVar()

        self.main_frame = tk.LabelFrame(self.root)
        self.main_frame.place(x=100, y=620)


        choose_cateogry_label = tk.Label(self.quality_list, text="Choose the category  ", font=self.fontstyle,padx="50").grid(row=1, column=0, padx=50, pady=(30, 40))

        self.quality_1 = tk.Radiobutton(self.quality_list, text="360", variable=self.quality_val, value=1, bd=2,
                                        font=self.fontstyle)
        self.quality_1.grid(row=1, column=1, padx=40, pady=(0, 10))
        self.quality_2 = tk.Radiobutton(self.quality_list, text="720", variable=self.quality_val, value=2, bd=2,
                                        font=self.fontstyle)
        self.quality_2.grid(row=2, column=1, padx=40, pady=(5, 10))

        tk.Button(self.root, text='Proceed', width=15, height=3, bg="black", fg="white",
                  command=lambda: selecting_video(self,self.quality_val.get())).place(x=500, y=470)

        def selecting_video(self, inp):

            if self.enter_link_entry.get() == "":
                messagebox.showerror("Invalid", "You haven't enter the link")
                return

            elif self.enter_path_entry.get()=="":
                messagebox.showerror("Invalid", "You haven't select the path either browse or enter the path")
                return
            elif inp == 0:
                messagebox.showerror("Invalid", "You haven't select any of the option")
                return
            show(self)
            global status
            download(self, self.enter_link_entry.get(), inp)

        def show(self):
            status = "Downloading..........."
            self.status_label = tk.Label(self.main_frame, text=f"Status ={status}", font=self.fontstyle)
            self.status_label.grid(row=0, column=0, padx=(40, 40), pady=(35, 10))

        def download(self, link, inp):
            try:

                yt_obj = YouTube(link)
                filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

                if inp == 1:
                    downld = filters[0]
                else:
                    downld = filters[1]

                main_part(self, downld,self.path_name)

                time.sleep(0)

            except Exception as excep:
                status = f"Link is not valid ..........."
                self.status_label = tk.Label(self.main_frame, text=f"Status ={status}", font=self.fontstyle)
                self.status_label.grid(row=0, column=0, padx=(40, 40), pady=(35, 10))
                messagebox.showerror("Error", f"{excep}")
                messagebox.showerror("Error", "Opps Please reload the page for downloading again")
        status = "None"

        def main_part(self, downld,path):
            if path=="":
                path = self.enter_path_entry.get()
            if downld.download(path):
                status = "Download Completed"
                self.status_label = tk.Label(self.main_frame, text=f"Status ={status}", font=self.fontstyle)
                self.status_label.grid(row=0, column=0, padx=(40, 40), pady=(35, 10))
                messagebox.showinfo("Status", "Downloaded Completed")
                flag =1

            else:
                status = "Error while downloading"
                self.status_label = tk.Label(self.main_frame, text=f"Status ={status}", font=self.fontstyle)
                self.status_label.grid(row=0, column=0, padx=(40, 40), pady=(35, 10))
                messagebox.showerror("Status", "Error while downloading")
                flag =0
            if flag:
                messagebox.showinfo("Info", "Please reload this page for downloading other video")
            else:
                messagebox.showerror("Error","Opps Please reload the page for downloading again")

root = tk.Tk()
interface = Ytubedownload(root)
root.mainloop()
