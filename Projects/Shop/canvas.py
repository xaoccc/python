from tkinter import Tk, Canvas


def create_window():
    window = Tk()
    window.geometry(f"800x600")
    window.title("Tashev's Shop for Everything")
    window.resizable(False, False)
    window.iconbitmap("icon.ico")
    return window


def create_frame():
    frame = Canvas(window, width=700, height=600)
    frame.grid(row=0, column=0)
    return frame


window = create_window()
frame = create_frame()
