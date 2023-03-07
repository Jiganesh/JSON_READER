import tkinter as tk
from tkinter import *
from tkinter import filedialog
from json_extraction import *


def upload_file():
    file = filedialog.askopenfilename(initialdir="C:\\", filetypes=[("JSON files", "*.json")])
    if file : 
        path_selected.set("Received a json file " + file)
        get_json_file_path_and_process(file)
        
    else:
        print("No file Selected")
    

application = tk.Tk()
application.geometry ("1200x400")  # Size of the window
application.title("Application for JSON File")  # Tittle of the application

font1 = ("times" , 18, "bold") # Just creating a font


# Creating a label and positioning it
upload_a_json_file_label = tk.Label(application, text="Upload a JSON File to Read", width=30, font=font1, pady= 20)
upload_a_json_file_label.grid(row=0, column=0)

# Creating a button and positioning it
upload_file_button = tk.Button(application, text="Upload File", width=20, command= lambda: upload_file())
upload_file_button.grid(row= 0, column=1)

path_selected = tk.StringVar()
path_selected.set("Once path is selected, It will be visible here")

# Creating a label to show selected file path  and positioning it
label2 = tk.Label(application, textvariable=path_selected, fg = "green")
label2.grid(row=3, column=0, padx= 10, pady=10)

application.mainloop()