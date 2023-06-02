from tkinter import *
from tkinter import ttk
import random

#Create an instance of Tkinter frame
root = Tk()
root.title("Fabric Identification And Fabric Defect Detection")
root.resizable(False, False)
root.geometry("750x350")

def clear():
   print("Bye !")
def display_num():
   print("Hey !")

frame = Frame(root ,bd=5)
frame.place(width= 600 ,height=200)
frame.pack()


#Define an Entry widget
heading = Label(frame, text="Fabric Identification \n And \n Fabric Defect Detection" , font=('Courier',15))
heading.pack()

#Create Buttons with proper position
button1= ttk.Button(frame, text= "Capture", command=display_num)
button1.place( relx=0.28, rely=2.5, relwidth=0.55, relheight=0.25)

button2= ttk.Button(frame, text= "Close",  command= clear)
button2.place(relx=0.28, rely=2.7, relwidth=0.55, relheight=0.25)

root.mainloop()