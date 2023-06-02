from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Fabric Identification And Fabric Defect Detection")
root.minsize(width=300, height=300)
root.maxsize(height=800, width=700)
root.geometry("700x600")

# Initialize global variable to store the PhotoImage object
background_photo = None



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

background_image = background_image.resize(
    (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)

# Convert the PIL Image object to a Tkinter PhotoImage object
background_photo = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

# Use the PhotoImage object for the canvas image
Canvas1.create_image(300, 340, image=background_photo)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=2)  # yellow background frame
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="  Fabric Identification \n And \n Fabric Defect Detection",
                     bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Fabric Identification", bg='black',
              fg='white', command=root.destroy)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Fabric Defect Detection", bg='black', fg='white', command=root.destroy)
btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

root.mainloop()
