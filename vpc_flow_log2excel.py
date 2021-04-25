import pandas as pd
import openpyxl
from tkinter import Tk, filedialog, Label

def File_path_open():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "C:/",title = "Select AWS VPC Flow Log file",filetypes =[("log files","*.log"),("csv files","*.csv")])

    return root.filename

def File_path_save():
    root = Tk()
    root.filename = filedialog.asksaveasfilename(initialdir = "C:/",title = "Select Save Directory",filetypes =[("Excel files","*.xlsx")], defaultextension=".xlsx")

    return root.filename
initial = Tk()
lbl = Label(initial, text="Excel Processing")
lbl.pack()

open_file_path = File_path_open()
flow_file = pd.read_csv(open_file_path, sep=" ", index_col=0)

save_file_path = File_path_save()
flow_file.to_excel(save_file_path)

initial.destory()