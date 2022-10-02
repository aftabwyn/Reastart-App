from struct import pack
from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
    
def restartTime():
    os.system("shutdown /r /t 5")
    
def shutdown():
    os.system("shutdown /s /t 1")
    
st = Tk()
st.title("Shutdown App")
st.geometry("550x400")
st.config(bg="#B5EAAA")

r_button = Button(st,text="Restart",bg="black",fg="white",activebackground="blue",
                  font=("Time New Roman",15,"bold"),relief=RIDGE,command=restart)

rt_button = Button(st,text="Restart Time",bg="black",fg="white",activebackground="blue",
                   font=("Time New Roman",15,"bold"),relief=RIDGE,command=restartTime)

s_button = Button(st,text="Shutdown",bg="black",fg="white",activebackground="blue",
                  font=("Time New Roman",15,"bold"),relief=RIDGE,command=shutdown)

s_button.place(x=200,y=180,height=35,width=150)
r_button.place(x=200,y=60,height=35,width=150)
rt_button.place(x=200,y=120,height=35,width=150)

st.mainloop()
