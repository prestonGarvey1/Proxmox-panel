import customtkinter
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
    
    

root = customtkinter.CTk()
root.title("Enter your URL")
root.geometry("400x400")
#Inputs for web url and port
url_label = customtkinter.CTkLabel(root, text="URL or IP:")
url_label.pack()

url_entry = customtkinter.CTkEntry(root, width=100)
url_entry.pack()

port_label = customtkinter.CTkLabel(root, text="(Optional) Port:")
port_label.pack()

port_entry = customtkinter.CTkEntry(root, width=100) #if a port is needed, this option supplies it
port_entry.insert(customtkinter.END, "80")
port_entry.pack()

dir_label = customtkinter.CTkLabel(root, text="(Optional) Directory:")
dir_label.pack()

dir_entry = customtkinter.CTkEntry(root, width=100)
dir_entry.pack()


# Proxmox data viewer button
data_button = customtkinter.CTkButton(root, text="Data View", command=load_dataview)
data_button.pack(padx=10, pady=10)
# Load webview
load_button = customtkinter.CTkButton(root, text="Load Page", command=load_page)
load_button.pack(padx=10, pady=10)

root.mainloop() 




   

