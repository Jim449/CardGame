import tkinter
from tkinter import ttk
from deck import Deck


class DeckGUI():
    def __init__(self, main, frame: ttk.Frame, name: str,
                 column: int, player: int, empty_card: tkinter.PhotoImage,
                 deck: Deck):

        self.name = name
        self.player = player
        self.empty_card = empty_card
        self.deck = deck
        self.button: ttk.Button = ttk.Button(
            frame,
            command=lambda name=name, player=player: main.click_deck(name, player))
        self.button.grid(column=column, row=0, padx=20)
        self.button.config(image=empty_card)
        self.button["state"] = tkinter.DISABLED

    def update(self, observer: int) -> None:
        card = self.deck.get_card(-1)
        if card is not None:
            self.button.config(image=card.get_miniature(observer))
            self.button["state"] = tkinter.NORMAL
