from tkinter import *
from PIL import ImageTk, Image



def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


root = Tk()
root.title("MedicApp - Welcome Screen")
root.minsize(300, 350)
root.maxsize(300, 350)
root.configure(background='white')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


imgFile = "logo.gif"
img = ImageTk.PhotoImage(Image.open(imgFile))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


explanation = """Welcome to MedicApp."""
w2 = Label(root,
           justify=LEFT,
           padx = 10,
           text=explanation).pack(side="top")



B = Button(root, text ="New Session", command=donothing)
B.pack()
B.place(x=40, y=320)

C = Button(root, text ="Close", command=root.destroy)
C.pack()
C.place(x=200, y=320)

root.config(menu=menubar)
root.mainloop()
