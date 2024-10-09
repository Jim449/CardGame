from deck import Deck
import tkinter
from tkinter import ttk


class DeckScrutinizeGUI():
    def __init__(self, main, root: tkinter.Tk, name: str, player: int, empty_card: tkinter.PhotoImage,
                 deck: Deck, rows: int = 4, columns: int = 10):
        self.name = name
        self.player = player
        self.deck = deck
        self.empty_card = empty_card
        self.panel = tkinter.Toplevel(root, background="black")
        self.content: list[ttk.Button] = []

        i = 0
        for row in range(rows):
            for column in range(columns):
                button = ttk.Button(
                    self.panel, image=empty_card,
                    command=lambda index=i, name=name, player=player: main.select_in_scrutinize(name, player, index))
                button["state"] = tkinter.DISABLED
                button.grid(row=row, column=column)
                self.content.append(button)
                i += 1

        self.close: ttk.Button = ttk.Button(
            self.panel, text="Close", command=self.panel.withdraw)
        self.close.grid(row=4, column=4, pady=20)
        self.panel.protocol("WM_DELETE_WINDOW", self.panel.withdraw)
        self.panel.withdraw()

    def update(self, observer: int) -> None:
        for index in range(40):
            card = self.deck.get_card(index)

            if card is not None:
                self.content[index].config(
                    image=card.get_miniature(observer))
                self.content[index]["state"] = tkinter.NORMAL
            else:
                self.content[index].config(image=self.empty_card, text="")
                self.content[index]["state"] = tkinter.DISABLED
        self.panel.deiconify()
