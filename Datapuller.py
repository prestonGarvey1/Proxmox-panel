import customtkinter
import tkinter.messagebox as messagebox
import proxmoxer 
from proxmoxer import ProxmoxAPI
import requests
import paramiko
import json
import sys



# Box to enter your user and pswd
root = customtkinter.CTk()
root.title("Select Node and VM")
root.geometry("400x400")

host_label = customtkinter.CTkLabel(root, text="Host:")
host_label.pack()

host_Entry = customtkinter.CTkEntry(root, width=50)
host_Entry.pack()

Username_label = customtkinter.CTkLabel(root, text="Username:")
Username_label.pack()

Username_Entry = customtkinter.CTkEntry(root, width=50 )
Username_Entry.pack()


pass_label = customtkinter.CTkLabel(root, text="Password:")
pass_label.pack()

pass_CTkEntry = customtkinter.CTkEntry(root, width=50, show="*")
pass_CTkEntry.pack()


def ProxAPI():
    Hostname = host_Entry.get()
    User = Username_Entry.get()
    Password = pass_CTkEntry.get()
    try:
        API = ProxmoxAPI(f'{Hostname}', user=f'{User}', password=f'{Password}', backend='ssh_paramiko', service='PVE')
        
    except:
        messagebox.showerror("Error", "Auth failed, check spelling and try again.")
   

def getusers():
    Hostname = host_Entry.get()
    User = Username_Entry.get()
    Password = pass_CTkEntry.get()
    API = ProxmoxAPI(f'{Hostname}', user=f'{User}', password=f'{Password}', backend='ssh_paramiko', service='PVE')
        
    with open('users.json', 'w',) as f:
        sys.stdout = f
        print(API.access.users.get())
    print('dumped file')
    


apiauth_button = customtkinter.CTkButton(root, text="Check Authentication", command=ProxAPI)
apiauth_button.pack(padx=10, pady=10)

getusers_button = customtkinter.CTkButton(root, text='Dump users file', command=getusers)
getusers_button.pack(padx=10, pady=10)
root.mainloop()


