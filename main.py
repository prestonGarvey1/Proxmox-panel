import tkinter  as tk
from tkinter import ttk 
import webview as web
import os

cwd = os.getcwd()
def load_page():
    url = f"http://{url_entry.get()}:{port_entry.get()}/{dir_entry.get()}"
    web.create_window("Webpage", url)
    web.start()

def load_dataview():
    root.destroy()
    os.system(f"python3 {cwd}\\Datapuller.py")
    
    

root = tk.Tk()
root.title("Enter your URL")

#Inputs for web url and port
url_label = tk.Label(root, text="URL or IP:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.insert(tk.END, "192.168.1.30")
url_entry.pack()

port_label = tk.Label(root, text="(Optional) Port:")
port_label.pack()

port_entry = tk.Entry(root, width=50) #if a port is needed, this option supplies it
port_entry.insert(tk.END, "80")
port_entry.pack()

dir_label = tk.Label(root, text="(Optional) Directory:")
dir_label.pack()

dir_entry = tk.Entry(root, width=50)
dir_entry.pack()


# Proxmox data viewer button
data_button = tk.Button(root, text="Data View", command=load_dataview)
data_button.pack()
# Load webview
load_button = tk.Button(root, text="Load Page", command=load_page)
load_button.pack()

root.mainloop() 




   

