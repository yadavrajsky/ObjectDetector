from tkinter import *
from PIL import ImageTk, Image
from CaptureVideo import Capturevideo

root = Tk()
root.title("Fabric Identification And Fabric Defect Detection")
root.minsize(width=300, height=300)
root.maxsize(height=800, width=700)
root.geometry("700x600")


def clear():
   print("Bye !")
   shutdown = 'q'
   root.quit()
def display_num():
   print("Hey !")

same = True
n = 0.85

# Adding a background image
background_image = Image.open("CoverPhoto1.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=2)  # yellow background frame
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="  Fabric Identification \n And \n Fabric Defect Detection", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Capture Video", bg='black', fg='white', command=Capturevideo)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Close", bg='black', fg='white', command=clear)
btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

from GreyScale import greyImage
from CreateImage import imagesCreate
 
root.mainloop()
