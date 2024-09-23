from tkinter import ttk
import tkinter


class Field():
    def __init__(self, root: tkinter.Tk, frame: ttk.Frame, player: int = 1, size: int = 6):

        self.root = root
        self.player = player
        self.cards = []
        self.back_image = tkinter.PhotoImage(file="Card back.png")

        for i in range(size):
            button = ttk.Button(
                frame, image=self.back_image, command=lambda index=i: self.select(index))
            button.grid(column=i, row=0)
            self.cards.append(button)

        self.popup = tkinter.Menu(frame)
        self.popup.add_command(label="Advance", command=self.advance)

    def select(self, index: int):
        print(f"Selected card {index} in field!")
        self.popup.tk_popup(self.root.winfo_pointerx(),
                            self.root.winfo_pointery())

    def advance(self):
        print("Advance!")
