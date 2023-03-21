import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.warning = tk.Label(text="Currency converter. Please delete old input values(if any) before converting.")
        self.label = tk.Label(text="BGN to EUR", bg="#123456", fg="white")
        self.bgn_eur_entry = tk.Entry()
        self.convert_button = tk.Button(text="Convert", command=self.convert)
        self.output = tk.Label()

        self.warning.pack(side="top")

        self.label.place(x=10, y=30)
        self.bgn_eur_entry.place(x=100, y=30)
        self.convert_button.place(x=250, y=30)


        self.label1 = tk.Label(text="BGN to USD", bg="#123456", fg="white")
        self.bgn_usd_entry = tk.Entry()
        self.convert_button1 = tk.Button(text="Convert", command=self.convert)

        self.label1.place(x=10, y=60)
        self.bgn_usd_entry.place(x=100, y=60)
        self.convert_button1.place(x=250, y=60)

        self.output.place(x=100, y=110)

    def convert(self):
        bgn_eur = self.bgn_eur_entry.get()
        bgn_usd = self.bgn_usd_entry.get()
        if bgn_eur.isdigit():
            bgn_eur_value = float(bgn_eur)
            bgn_eur_result = round(bgn_eur_value * 1.95583, 2)
            self.output.config(
                text=str(bgn_eur_value) + ' BGN = ' + str(bgn_eur_result) + ' EUR',
                bg="green", fg="white")
        elif bgn_usd.isdigit():
            bgn_usd_value = float(bgn_usd)
            bgn_usd_result = round(bgn_usd_value * 1.67, 2)
            self.output.config(
                text=str(bgn_usd_value) + ' BGN = ' + str(bgn_usd_result) + ' USD',
                bg="green", fg="white")
        else:
            self.output.config(
                text="That's not a number!",
                bg="red", fg="black")
from tkinter import *
root = Tk()

root.geometry('500x150')

app = Application()
app.master.title("Currency converter")
app.mainloop()

