from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=500, height=500)
    root.maxsize(900, 800)
    root.geometry("700x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")  # blue
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)  # yellow
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Defects",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.3

    Label(labelFrame, text="%-20s%--50s%-30s" % ('No.', 'Title of Defect', 'Probability'), bg='black', fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    Label(labelFrame, text="%-20s%--50s%-30s" % ('1', 'Hole', '0.82'), bg='black', fg='white').place(
        relx=0.07, rely=0.3)
    Label(labelFrame, text="%-20s%--50s%-30s" % ('2', 'Torn', '0.64'), bg='black', fg='white').place(
        relx=0.07, rely=0.4)
    Label(labelFrame, text="%-20s%--50s%-30s" % ('3', 'Laddering', '0.79'), bg='black', fg='white').place(
        relx=0.07, rely=0.5)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

View()
