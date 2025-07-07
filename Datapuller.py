import tkinter as tk
import proxmoxer 

# Box to enter your user and pswd
root = tk.Tk()
root.title("Select Node and VM")

Username_label = tk.Label(root, text="Username")
Username_label.pack()

Username_entry = tk.Entry(root, width=50, )
Username_entry.pack()

pswd_label = tk.Label(root, text="Password")
pswd_label.pack()

pswd_entry = tk.Entry(root, width=50, show="*")
pswd_entry.pack()

tk.mainloop()
