#!/bin/python3
import datetime
import tkinter as tk


# function to save quick note
def save_note(event=None):
    """Capture the note and save in the file.
    Add 'event=None' to handle direct function call and key binding"""

    note = text_entry.get("1.0", tk.END).strip()
    with open(note_file, "a") as file:
        file.write(f"{note_time}: {note}\n")

    root.destroy()


# build the note name
date = datetime.datetime.now()
week_day = date.strftime("%A")
year = date.strftime("%x")
hour = date.strftime("%X")
note_time = f"**{week_day} - {year} - {hour}**"

# set the file location
full_path = "/home/mateus/Documentos/quick_note/"
note_file = full_path + "notes.md"

# create an instance of tkinter frame
root = tk.Tk()
root.title("Quick Notes")
root.geometry("400x200")

# text box
text_entry = tk.Text(
    root, wrap=tk.WORD, height=10, bg="#2b2b2b", fg="white", insertbackground="white"
)
text_entry.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
text_entry.focus_set()  # set the focus on the text entry widget


# adjust row and column weights to allow the text entry to expand vertically
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# bind the 'Return' key press event to the save_note function
text_entry.bind("<Return>", save_note)

# run the application
root.mainloop()
