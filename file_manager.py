import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    return path

def save_file(content):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename()
    with open(file_path, 'w') as file:
        file.write(content)
    return content