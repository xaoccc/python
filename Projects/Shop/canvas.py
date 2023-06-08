from tkinter import Tk, Canvas


def create_window():
    window = Tk()
    window.geometry("800x600")
    window.title("Tashev's Shop for Everything")
    window.resizable(False, False)
    window.iconbitmap('icon.ico')
    window.mainloop()

    return window


def create_frame():
    frame = Canvas(window, width=800, height=800)
    frame.grid(row=0, col=0)


window = create_window()
frame = create_frame()
