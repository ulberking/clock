from threading import currentThread
from tkinter import *
import tkinter
from tkinter.tix import COLUMN
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Clock')
current_hour = Label(root,font=('ds-digital',80),background='black',foreground='blue', )
current_hour.grid(row=0,column=0)
current_1 = Label(root,font=('ds-digital',80),background='black',foreground='white',text=':')
current_1.grid(row=0,column=1)
current_minute = Label(root,font=('ds-digital',80),background='black',foreground='red')
current_minute.grid(row=0,column=2)
current_2 = Label(root,font=('ds-digital',80),background='black',foreground='white',text=':')
current_2.grid(row=0,column=3)
current_second = Label(root,font=('ds-digital',80),background='black',foreground='green')
current_second.grid(row=0,column=4)
current_3 = Label(root,font=('ds-digital',80),background='black',foreground='white',text=':')
current_3.grid(row=0,column=5)
current_PA = Label(root,font=('ds-digital',80),background='black',foreground='yellow')
current_PA.grid(row=0,column=6)
def fetch_time():
    # th = strftime('%H')
    # tm = strftime('%M')
    # ts = strftime('%S')
    # tp = strftime('%p')
    t= strftime("%H:%M:%S:%p")
    th=t[0:2]
    tm=t[3:5]
    ts=t[6:8]
    tp=t[9:]
    current_hour.config(text=th)
    current_minute.config(text=tm)
    current_second.config(text=ts)
    current_PA.config(text=tp)
    current_second.after(1000,fetch_time)
fetch_time()
root.mainloop()