from tkinter import ttk
import tkinter


class Hand():
    def __init__(self, root: tkinter.Tk, frame: ttk.Frame, player: int = 1, size: int = 6):

        self.root = root
        self.player = player
        self.cards = []
        self.back_image = tkinter.PhotoImage(file="Card back.png")

        self.deck = ttk.Button(
            frame, image=self.back_image, command=self.click_deck)
        self.discard = ttk.Button(
            frame, image=self.back_image, command=self.click_discard)

        if player == 1:
            self.discard.grid(column=0, row=0, padx=20)
            self.deck.grid(column=7, row=0, padx=20)
            self.create_buttons(frame, "right", size)
        else:
            self.deck.grid(column=0, row=0, padx=20)
            self.create_buttons(frame, "left", size)
            self.discard.grid(column=7, row=0, padx=20)

        self.popup = tkinter.Menu(frame)
        self.popup.add_command(label="Play", command=self.play)

    def create_buttons(self, frame: ttk.Frame, side: str, size: int = 6):
        for i in range(size):
            button = ttk.Button(
                frame, image=self.back_image, command=lambda index=i: self.select(index))
            button.grid(column=i+1, row=0)
            self.cards.append(button)

    def select(self, index: int):
        print(f"Selected card {index} in hand!")
        self.popup.tk_popup(self.root.winfo_pointerx(),
                            self.root.winfo_pointery())

    def play(self):
        print("Play the card!")

    def click_deck(self):
        print("Deck clicked!")

    def click_discard(self):
        print("Discard clicked!")
