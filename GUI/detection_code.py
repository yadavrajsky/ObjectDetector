from tkinter import *
from PIL import ImageTk, Image

from view_defects import *;
from CaptureVideo import *;

root = Tk()
root.title("Fabric Defect Detection")
root.minsize(width=300, height=300)
root.maxsize(height=800, width=700)
root.geometry("700x600")

#dummy_functions 

def codeDetection():
    Capturevideo()
    View()
    print("fabric defect identified ")

def detection(): 
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#9370DB")  # maroon
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=2)  # yellow background frame
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Fabric Defect Detection",
                        bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #labelFrame = Frame(root, bg='white')
    #labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    btn1 = Button(root, text="Capture Video", bg='black',
                fg='white', command=codeDetection)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Close", bg='black', fg='white', command=root.destroy)
    btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    root.mainloop()
detection()
