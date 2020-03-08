import tkinter as tk
import pyqrcode
import sys

win = tk.Tk()
win.title("QR Code Creator")

def creator():
    txt = entry.get()
    qr = pyqrcode.create(txt)
    save = qr.svg("myqrcode.svg",scale=5)


label=tk.Label(win,text="Enter URL")
label.grid(row=0,column=0)
entry = tk.Entry(win)
entry.grid(row=1,column=0)

button=tk.Button(win,text="Create",command=creator)
button.grid(row=3,column=0)
win.mainloop()