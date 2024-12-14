from tkinter import *
from tkinter import ttk
import subprocess
import os
import win32com.client


def center_window(root, width, height):
    """Centers the window on the screen."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

def open_tool(script_name):
    """Opens the specified script, executable, or shortcut file."""
        # Assume it's a Python script
    root.destroy()
    subprocess.Popen(['python', script_name], cwd=os.path.dirname(os.path.abspath(__file__)))


# Main window setup
root = Tk()
root.title("hide in image tools")
window_width = 900
window_height = 600
center_window(root, window_width, window_height)

# Title label
title = ttk.Label(
    root, 
    text="hide in image tools", 
    font=("Ubuntu", 24, "bold"), 
)
title.grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky="n")

# Subheading
subheading = ttk.Label(
    root, 
    text="Choose a tool to hide data:", 
    font=("Ubuntu", 14), 
)
subheading.grid(row=1, column=0, columnspan=3, pady=(0, 20), sticky="n")

# Button styles
style = ttk.Style()
style.configure(
    "TButton", 
    font=("Ubuntu", 12), 
    padding=10, 
    foreground="black"
)
style.map(
    "TButton", 
    background=[("active", "#0056b3")], 
    foreground=[("active", "white")]
)

# Buttons for each category
categories = [
    ("Steghide tool", "steghide.py"),
    ("Back", "home.py"),
]

for i, (label, script) in enumerate(categories):
    button = ttk.Button(
        root, 
        text=label, 
        command=lambda script=script: open_tool(script)
    )
    button.grid(row=i + 2, column=1, pady=10, padx=20, sticky="ew")

# Make the layout centered
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
