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
        self.warning = tk.Label(text="Please delete old input values(if any) before calculating.")
        self.warning.pack(side="top")

        self.label = tk.Label(text="Length, Width & Height to Volume")
        self.length = tk.Entry()
        self.height = tk.Entry()
        self.width = tk.Entry()

        self.convert_button = tk.Button(text="Calculate", command=self.calculate)
        self.output = tk.Label()

        self.label.place(x=10, y=30)
        self.length.place(x=10, y=60)
        self.height.place(x=100, y=60)
        self.width.place(x=200, y=60)
        self.convert_button.place(x=300, y=60)


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


root.geometry('600x150')

app = Application()
app.master.title("Multicalculator")
app.mainloop()

