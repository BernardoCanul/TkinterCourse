import tkinter as tk
from tkinter import ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    outputString.set(km_output)

# Window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

# Title
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left",padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# Output
outputString = tk.StringVar()
output_label = ttk.Label(master=window, text="OUTPUT", font="Calibri 24", textvariable=outputString)
output_label.pack(pady=5)

# Run
window.mainloop()