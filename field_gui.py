from tkinter import ttk
import tkinter
from field import Field


class FieldGUI():
    def __init__(self, main, frame: ttk.Frame, empty_card: tkinter.PhotoImage, player: int, size: int = 6):

        self.player: int = player
        self.cards: list[ttk.Button] = []
        self.empty_card = empty_card

        for i in range(size):
            button = ttk.Button(
                frame, image=empty_card,
                command=lambda player=player, index=i: main.select_in_field(player, index))
            button.grid(column=i, row=0)
            button["state"] = tkinter.DISABLED
            self.cards.append(button)

    def populate(self, field: Field, observer: int) -> None:
        for index, card in enumerate(field.get_card_list()):
            if card is not None:
                self.cards[index].config(card.get_miniature(observer))
                self.cards[index]["state"] = tkinter.NORMAL
