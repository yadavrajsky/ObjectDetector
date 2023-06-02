from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

from ClickImageNew import *;

root = Tk()
root.title("Fabric Identification")
root.minsize(width=300, height=300)
root.maxsize(height=800, width=700)
root.geometry("700x600")

#dummy_functions 

def code_identification():
    capture_image()
    messagebox.showinfo('Success', "Fabric Identified Successfully")
    print("Fabric Identified - fabric Name ")


def identification():
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")  # maroon
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=2)  # yellow background frame
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="  Fabric Identification ",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #labelFrame = Frame(root, bg='black')
    #labelFrame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.4)

    lb1 = Label(root, text="Fabric name: ", bg='white', fg='black')
    lb1.place(relx=0.2, rely=0.8,  relheight=0.05)

    bookInfo1 = Label(root, text="Cotton", bg='white', fg='black')
    bookInfo1.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.05)

    btn1 = Button(root, text="Capture Video", bg='black',
                fg='white', command=code_identification)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Close", bg='black', fg='white', command=root.destroy)
    btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    root.mainloop()
identification()
'''
    CaptureBtn = Button(root, text="Camera", bg='#d1ccc0',
                        fg='black', command=code_identification)
    CaptureBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Close", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
'''
    


