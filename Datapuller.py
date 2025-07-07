import tkinter as tk
import tkinter.messagebox as messagebox
import proxmoxer 
from proxmoxer import ProxmoxAPI
import requests
import paramiko




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
        ProxmoxAPI(f'{Hostname}', user=f'{User}', password=f'{Password}', backend='ssh_paramiko', service='PVE')
    except:
        messagebox.showerror("Error", "Auth failed, check spelling and try again.")
apiauth_button = tk.Button(root, text="Authenticate API", command=ProxAPI)
apiauth_button.pack()
tk.mainloop()


