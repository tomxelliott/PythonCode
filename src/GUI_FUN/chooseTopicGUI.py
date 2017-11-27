from tkinter import Frame, Tk, BOTH, Text, Menu, END, Label, Radiobutton
from tkinter import filedialog, IntVar


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text

v = IntVar()
v.set(1)  # initializing the choice, i.e. Anatomy

topics = [
    ("Anatomy", 1),
    ("Anesthesiology", 2),
    ("Biochemisty", 3),
    ("Cell Biology", 4),
    ("Embryology", 5),
    ("Genetics", 6),
    ("Human Behavior", 7),
    ("Immunology", 8),
    ("Neuroscience", 9),
    ("Physiology", 10)
    ]

def ShowChoice():
    print(v.get())

    Label(root,
          text="""Choose your Revision Topic:""",
          justify=LEFT,
          padx=20).pack()

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

    B = Button(root, text="Go", command=option1)
    B.pack()
    B.place(x=160, y=270)

    C = Button(root, text="Close", command=root.destroy)
    C.pack()
    C.place(x=320, y=270)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
