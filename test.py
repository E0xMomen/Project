import tkinter as tk

def show_start_page():
    clear_window()
    label = tk.Label(root, text="Start Page", font=("Arial", 16))
    label.pack(pady=10)

    button1 = tk.Button(root, text="Go to Page 1", command=show_page_one)
    button1.pack()

    button2 = tk.Button(root, text="Go to Page 2", command=show_page_two)
    button2.pack()

def show_page_one():
    clear_window()
    label = tk.Label(root, text="Page One", font=("Arial", 16))
    label.pack(pady=10)

    button = tk.Button(root, text="Back to Start Page", command=show_start_page)
    button.pack()

def show_page_two():
    clear_window()
    label = tk.Label(root, text="Page Two", font=("Arial", 16))
    label.pack(pady=10)

    button = tk.Button(root, text="Back to Start Page", command=show_start_page)
    button.pack()

def clear_window():
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

# Main application window
root = tk.Tk()
root.title("Page Navigation Example")
root.geometry("400x300")

# Start with the Start Page
show_start_page()

# Run the application
root.mainloop()
