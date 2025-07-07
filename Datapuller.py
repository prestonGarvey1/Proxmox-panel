import tkinter as tk
import proxmoxer 
from proxmoxer import ProxmoxAPI
import requests

# Box to enter your user and pswd
root = tk.Tk()
root.title("Select Node and VM")

host_label = tk.Label(root, text="Host:")
host_label.pack()

host_entry = tk.Entry(width=50)
host_entry.pack()

Username_label = tk.Label(root, text="Username")
Username_label.pack()

Username_entry = tk.Entry(root, width=50, )
Username_entry.pack()

tokenid_label = tk.Label(root, text="Password")
tokenid_label.pack()

tokenid_entry = tk.Entry(root, width=50, show="*")
tokenid_entry.pack()

tokensecret_label = tk.Label(root, text="Token ID")
tokensecret_label.pack()

tokensecret_entry = tk.Entry(width=50, show="*")
tokensecret_entry.pack()

def ProxAPI():
    Try_API = ProxmoxAPI(host_entry, user=Username_entry, verify_ssl=False )

apiauth_button = tk.Button(root, text="Authenticate API", command=ProxAPI)
apiauth_button.pack()
tk.mainloop()


