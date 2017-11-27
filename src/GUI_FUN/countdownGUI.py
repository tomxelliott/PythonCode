import tkinter as tk

counter = 10


def counter_label(label):
    def count():
        global counter
        counter -= 1
        label.config(text=str(counter))
        label.after(1000, count)
        if counter == 0:
            root.destroy()

    count()


root = tk.Tk()
root.title("Counting Seconds")
root.minsize(150, 100)
root.maxsize(150, 100)
label = tk.Label(root, fg="black")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
