import tkinter as tk
from tkinter import *
root = Tk()


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.input_variable_length = StringVar(value="Enter length")
        self.input_variable_height = StringVar(value="Enter height")
        self.input_variable_width = StringVar(value="Enter width")

        self.label = tk.Label(text="Calculate Volume")
        self.length = Entry(root, textvariable=self.input_variable_length)
        self.height = Entry(root, textvariable=self.input_variable_height)
        self.width = Entry(root, textvariable=self.input_variable_width)

        self.convert_button = tk.Button(text="Calculate", command=self.calculate)
        self.output = tk.Label()

        self.label1 = tk.Label(text="Calculate Area")
        self.length1 = Entry(root, textvariable=self.input_variable_length)
        self.height1 = Entry(root, textvariable=self.input_variable_height)

        self.label.place(x=10, y=30)
        self.length.place(x=10, y=60)
        self.height.place(x=100, y=60)
        self.width.place(x=200, y=60)
        self.convert_button.place(x=300, y=60)
        self.label1.place(x=10, y=100)
        self.length1.place(x=10, y=130)
        self.height1.place(x=100, y=130)

        self.output.place(x=100, y=110)

    def calculate(self):
        if (isfloat(self.length.get()) or self.length.get().isdigit()) and (isfloat(self.height.get()) or self.height.get().isdigit()) and (isfloat(self.height.get()) or self.width.get().isdigit()):
            length = float(self.length.get())
            height = float(self.height.get())
            width = float(self.width.get())
            volume_result = round(length * height * width, 2)
            self.output.config(text=str(volume_result) + ' m3', bg="green", fg="white")

        else:
            self.output.config(
                text="That's not a number!",
                bg="red", fg="black")


root.geometry('600x300')

app = Application()
app.master.title("Multicalculator")
app.mainloop()

