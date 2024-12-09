from tkinter import *
from tkinter import ttk
import subprocess
import os

def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

root = Tk()
root.title("Home Page")
window_width = 800
window_height = 500
center_window(window_width, window_height)

def open_gifshuff_tool():
    # Close the current window
    root.destroy()
    # Run the gifshuff.py script
    subprocess.Popen(['python', 'gifshuff.py'], cwd=os.path.dirname(os.path.abspath(__file__)))

btn = ttk.Button(root, text="Go To Gifshuff", command=open_gifshuff_tool)
btn.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()