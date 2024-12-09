import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import subprocess


def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

root = Tk()
root.title("GifShuff Tool")
root.config()
window_width = 800
window_height = 500
center_window(window_width, window_height)

def gifshuff(message,password,carrier,outimg):
    subprocess.Popen(["Tools/hide in images/GIFShuff-Tool/GIFSHUF.EXE"
                      ,"-CS"
                      ,"-m"
                      ,message
                      ,"-p"
                      ,password
                      ,carrier
                      ,outimg
                      ])

def gifshuff_extract(password,stegoimg):
        message= subprocess.getoutput(["Tools/hide in images/GIFShuff-Tool/GIFSHUF.EXE"
                      ,"-C"
                      ,"-p"
                      ,password
                      ,stegoimg
                      ])
        extract.insert(0,message)

title= ttk.Label(root , text="GiFShuff tool GUI",font="Ubuntu 20 bold")
title.grid(row=0 ,column=0, columnspan=6 ,padx=20 ,pady=10)


title= ttk.Label(root , text="GiFShuff hide",font="Ubuntu 20 bold")
title.grid(row=1 ,column=0, columnspan=6 ,padx=10 ,pady=10)

#message it self
message_label = ttk.Label(root,text="Enter message to hide")  
message_label.grid(row=2 , column=1,padx=10, pady=10)

message = ttk.Entry(root,width=30)
message.grid(row=2 ,column=2) 


#password
pass_label = ttk.Label(root,text="Enter password ")  
pass_label.grid(row=3 , column=3,padx=10, pady=10)

password = ttk.Entry(root,width=20)
password.grid(row=3 ,column=4) 

#name of out img
out_img_name_label = ttk.Label(root,text="Enetr the stego image name")
out_img_name_label.grid(row=3 ,column=1,padx=10,pady=10)

out_img_name = ttk.Entry(root,width=30)
out_img_name.grid(row=3 ,column=2,padx=10,pady=10)


path_carrier_img_label= ttk.Label(root ,text = "path of the carrier img")
path_carrier_img_label.grid(row=4 , column=1 ,padx=10 ,pady=10)
    
path_carrier_img = ttk.Entry(root,width=30)
path_carrier_img.grid(row=4, column=2,padx=10,pady=10)
    
#select button 
def upload_img():
    name = filedialog.askopenfilename(title="select the carrie image")
    path_carrier_img.insert(0,name)

btn_select = ttk.Button(root, text="upload",command = upload_img) 
btn_select.grid(row=5 , column=1 ,padx=10 ,pady=10 )

#hide button
def hidebutton():
    carrier_img = path_carrier_img.get()
    passw= password.get()
    hidden_message = message.get()
    name_stego_img = out_img_name.get()

    gifshuff(hidden_message,passw,carrier_img,name_stego_img)

btn_hide = ttk.Button(root, text="hide",command = hidebutton) 
btn_hide.grid(row=5 , column=3 ,padx=10 ,pady=10 )



title= ttk.Label(root , text="GiFShuff extract",font="Ubuntu 20 bold")
title.grid(row=6 ,column=0, columnspan=6 ,padx=10 ,pady=10)

#btn extract 


extract_label= ttk.Label(root, text="the hidde data")
extract_label.grid(row=7 ,column=1 , padx=10 ,pady=10)

extract=  ttk.Entry(root, width=50)
extract.grid(row=7 ,column=2 ,padx=10,pady=10)


def extract_hidden_message():
     path = stego_img_path.get()
     passw= password.get()
     gifshuff_extract(passw,path)


btn_extract = ttk.Button(root, text="extract", command=extract_hidden_message)
btn_extract.grid(row=7 , column=3 ,padx=10 ,pady=10)


def upload_stego_img():
    name = filedialog.askopenfilename(title="select stego image path")
    stego_img_path.insert(0, name)
    
     
btn_upload = ttk.Button(root, text="upload",command=upload_stego_img)
btn_upload.grid(row=7 , column=4 ,padx=10 ,pady=10)

stego_img_label =  ttk.Label(root, text="stego image path")
stego_img_label.grid(row=8,column=1)

stego_img_path = ttk.Entry(root,width=50)
stego_img_path.grid(row=8 ,column=2) 


def Back():
    root.destroy()
    subprocess.Popen(['python', "hide_in_image_page.py"], cwd=os.path.dirname(os.path.abspath(__file__)))

btn_back=ttk.Button(root,text="back",command=Back )
btn_back.grid(row=9,column=1,padx=10,pady=30)


root.mainloop()