from tkinter import *
from PIL import ImageTk, Image

from tkinter import filedialog

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Test button")
    button.pack()

def option1():
    filewin = Toplevel(root)
    button = Button(filewin, text="Options")
    button.pack()

def onOpen(self):
    ftypes = [('Python files', '*.py'), ('All files', '*')]
    dlg = filedialog.Open(self, filetypes=ftypes)
    fl = dlg.show()

    if fl != '':
        text = self.readFile(fl)
        self.txt.insert(END, text)

def readFile(self, filename):
    f = open(filename, "r")
    text = f.read()
    return text


root = Tk()
root.title("MedicApp - New Session")
root.minsize(500, 300)
root.maxsize(500, 300)
root.configure(background='white')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


'''
def sel():
   selection = "You selected the Option " + str(var.get()) + "\nSelect Go to Proceed..."
   label.config(text = selection)

var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)
'''

v = IntVar()
v.set(1)  # initializing the choice, i.e. Anatomy

topics = [
    ("Anatomy",1),
    ("Anesthesiology",2),
    ("Biochemisty",3),
    ("Cell Biology",4),
    ("Embryology",5),
    ("Genetics",6),
    ("Human Behavior",7),
    ("Immunology",8),
    ("Neuroscience",9),
    ("Physiology",10)
]

def ShowChoice():
    print (v.get())

Label(root,
      text="""Choose your Revision Topic:""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in topics:
    Radiobutton(root,
                text=txt,
                indicatoron=0,
                width=20,
                padx=20,
                selectcolor="blue",
                variable=v,
                command=ShowChoice,
                value=val).pack(anchor=CENTER)

label = Label(root)
label.pack()

B = Button(root, text ="Go", command=option1)
B.pack()
B.place(x=160, y=270)

C = Button(root, text ="Close", command=root.destroy)
C.pack()
C.place(x=320, y=270)

root.config(menu=menubar)
root.mainloop()
