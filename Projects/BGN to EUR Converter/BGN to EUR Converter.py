import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.label = tk.Label(text="Value Converter")
        self.number_entry = tk.Entry()
        self.convert_button = tk.Button(text="Convert", command=self.convert)
        self.output = tk.Label()
        self.label.pack(side="left")
        self.number_entry.pack(side="left")
        self.convert_button.pack(side="left")
        self.output.pack(side="left")

    def convert(self):
        entry = self.number_entry.get()
        try:
            value = float(entry)
            result = round(value * 1.95583, 2)
            self.output.config(
                text=str(value) + ' BGN = ' + str(result) + ' EUR',
                bg="green", fg="white")
        except ValueError:
            self.output.config(
                text="That's not a number!",
                bg="red", fg="black")

app = Application()
app.master.title("BGN to EUR converter")
app.mainloop()

