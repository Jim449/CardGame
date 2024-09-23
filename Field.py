from tkinter import ttk
import tkinter


class Field():
    def __init__(self, main, frame: ttk.Frame, player: int = 1, size: int = 6):

        self.main = main
        self.root: tkinter.Tk = main.get_root()
        self.player: int = player
        self.cards: list[ttk.Button] = []
        self.back_image: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Card back.png")

        for i in range(size):
            button = ttk.Button(
                frame, image=self.back_image, command=lambda index=i: self.select(index))
            button.grid(column=i, row=0)
            button.grid_forget()
            self.cards.append(button)

        self.popup = tkinter.Menu(frame)
        self.popup.add_command(label="Advance", command=self.advance)

    def select(self, index: int):
        print(f"Selected card {index} in field!")
        self.popup.tk_popup(self.root.winfo_pointerx(),
                            self.root.winfo_pointery())

    def advance(self):
        print("Advance!")
