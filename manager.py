import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

window = Tk()

odoo_s = tk.StringVar()
postgre_s = tk.StringVar()
nginx_s = tk.StringVar()

def openFile(fName):
	os.system("xdg-open " + fName)

def startService(sName):
	os.system("systemctl start " + sName)
	checkService()

def stopService(sName):
	os.system("systemctl stop " + sName)
	checkService()

def checkService():
	if os.system("systemctl is-active --quiet odoo") == 0:
		odoo_s.set("Running")
	else:
		odoo_s.set("Not Running")

	if os.system("systemctl is-active --quiet postgresql") == 0:
		postgre_s.set("Running")
	else:
		postgre_s.set("Not Running")

	if os.system("systemctl is-active --quiet nginx") == 0:
		nginx_s.set("Running")
	else:
		nginx_s.set("Not Running")




window.title("Server Manager v0.0.1")
window.geometry('400x280')
window.minsize(400, 280)
window.maxsize(400, 280)
window['bg'] = "#333333"

s = ttk.Style()
s.configure("My.TLabel", background='#333', foreground="#fff")
s.configure('My.TFrame', background='#333')

frm = ttk.Frame(window, padding=10, style='My.TFrame')
frm.grid(row=0, column=0, sticky="NESW")
frm.grid_rowconfigure(0, weight=1)
frm.grid_columnconfigure(0, weight=1)

checkService()

ttk.Label(frm, text="Service", style="My.TLabel").grid(column=0, row=0)
ttk.Label(frm, text="Status", style="My.TLabel").grid(column=1, row=0)
ttk.Label(frm, text="Control", style="My.TLabel").grid(column=2, row=0)

ttk.Label(frm, text="Odoo v15", style="My.TLabel").grid(column=0, row=1)
ttk.Label(frm, textvariable=odoo_s, style="My.TLabel").grid(column=1, row=1)
tk.Button(frm, text="Start", bg='#222', fg='#fff', relief='flat', width=9, command=lambda:startService('odoo')).grid(column=2, row=1)
tk.Button(frm, text="Stop", bg='#222', fg='#fff', relief='flat', width=9, command=lambda:stopService('odoo')).grid(column=3, row=1)

ttk.Label(frm, text="Postgres", style="My.TLabel").grid(column=0, row=2)
ttk.Label(frm, textvariable=postgre_s, style="My.TLabel").grid(column=1, row=2)
tk.Button(frm, text="Start", bg='#222', fg='#fff', relief='flat', width=9, command=lambda:startService('postgresql')).grid(column=2, row=2)
tk.Button(frm, text="Stop", bg='#222', fg='#fff', relief='flat', width=9, command=lambda:stopService('postgresql')).grid(column=3, row=2)

ttk.Label(frm, text="Nginx", style="My.TLabel").grid(column=0, row=3)
ttk.Label(frm, textvariable=nginx_s, style="My.TLabel").grid(column=1, row=3)
tk.Button(frm, text="Start", bg='#222', fg='#fff', relief='flat', width=9, command=lambda:startService('nginx')).grid(column=2, row=3)
tk.Button(frm, text="Stop", bg='#222', fg='#fff', relief='flat', width=9, command=lambda:stopService('nginx')).grid(column=3, row=3)

ttk.Label(frm, text="   ", style="My.TLabel").grid(column=0, row=4)
ttk.Label(frm, text="Conf Files", style="My.TLabel").grid(column=0, row=5)

tk.Button(frm, text="pg_hba.conf", bg='#222', fg='#fff', relief='flat', width=12, command=lambda:openFile('/var/lib/pgsql/data/pg_hba.conf')).grid(column=0, row=6)
tk.Button(frm, text="postgresql.conf", bg='#222', fg='#fff', relief='flat', width=12, command=lambda:openFile('/var/lib/pgsql/data/postgresql.conf')).grid(column=2, row=6)
tk.Button(frm, text="nginx.conf", bg='#222', fg='#fff', relief='flat', width=12, command=lambda:openFile('/etc/nginx/nginx.conf')).grid(column=0, row=7)
tk.Button(frm, text="nginx odoo.conf", bg='#222', fg='#fff', relief='flat', width=12, command=lambda:openFile('/etc/nginx/conf.d/odoo.conf')).grid(column=2, row=7)
tk.Button(frm, text="odoo.conf", bg='#222', fg='#fff', relief='flat', width=12, command=lambda:openFile('/etc/odoo.conf')).grid(column=0, row=8)

tk.Label(frm, text="github.com/utkuhalis", background="#333", foreground="#fff").place(x=0,y=215)

ttk.Label(frm, text="   ", style="My.TLabel").grid(column=16, row=16)
window.mainloop()

#0=working
#768=not working