import tkinter
from tkinter import ttk
from deck import Deck


class DeckGUI():
    def __init__(self, main, frame: ttk.Frame, name: str,
                 column: int, player: int, empty_card: tkinter.PhotoImage):

        self.name = name
        self.player = player
        self.empty_card = empty_card
        self.deck: ttk.Button = ttk.Button(
            frame,
            command=lambda name=name, player=player: main.click_deck(name, player))
        self.deck.grid(column=column, row=0, padx=20)
        self.deck.config(image=empty_card)
        self.deck["state"] = tkinter.DISABLED

    def update(self, deck: Deck, observer: int) -> None:
        card = deck.get_card(-1)
        if card is not None:
            self.deck.config(image=card.get_miniature(observer))
            self.deck["state"] = tkinter.NORMAL
