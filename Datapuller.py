import tkinter as tk
import tkinter.messagebox as messagebox
import proxmoxer 
from proxmoxer import ProxmoxAPI
import requests
import paramiko
import json
import sys



# Box to enter your user and pswd
root = tk.Tk()
root.title("Select Node and VM")

host_label = tk.Label(root, text="Host:")
host_label.pack()

host_entry = tk.Entry(width=50)
host_entry.pack()

Username_label = tk.Label(root, text="Username:")
Username_label.pack()

Username_entry = tk.Entry(root, width=50 )
Username_entry.pack()


pass_label = tk.Label(root, text="Password:")
pass_label.pack()

pass_entry = tk.Entry(root, width=50, show="*")
pass_entry.pack()


def ProxAPI():
    Hostname = host_entry.get()
    User = Username_entry.get()
    Password = pass_entry.get()
    try:
        API = ProxmoxAPI(f'{Hostname}', user=f'{User}', password=f'{Password}', backend='ssh_paramiko', service='PVE')
        
    except:
        messagebox.showerror("Error", "Auth failed, check spelling and try again.")
   

def getusers():
    Hostname = host_entry.get()
    User = Username_entry.get()
    Password = pass_entry.get()
    API = ProxmoxAPI(f'{Hostname}', user=f'{User}', password=f'{Password}', backend='ssh_paramiko', service='PVE')
        
    with open('users.json', 'w',) as f:
        sys.stdout = f
        print(API.access.users.get())
    print('dumped file')
    


apiauth_button = tk.Button(root, text="Check Authentication", command=ProxAPI)
apiauth_button.pack()

getusers_button = tk.Button(root, text='Dump users file', command=getusers)
getusers_button.pack()
tk.mainloop()


