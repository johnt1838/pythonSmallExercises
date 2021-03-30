import tkinter as tk
from tkinter import ttk
from datetime import date
from datetime import datetime

NORM_FONT = ("Helvetica", 10)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=20)
    B1 = ttk.Button(popup, text="Thanks", command=popup.destroy)
    B1.pack()
    popup.mainloop()


now_time = str(datetime.now())

popupmsg(now_time)

