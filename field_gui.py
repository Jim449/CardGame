from tkinter import ttk
import tkinter
from field import Field


class FieldGUI():
    def __init__(self, main, frame: ttk.Frame, empty_card: tkinter.PhotoImage,
                 name: str, player: int, field: Field, size: int = 6,
                 padding: int = 0, grid_start: int = 1):

        self.name = name
        self.player: int = player
        self.cards: list[ttk.Button] = []
        self.empty_card = empty_card
        self.field = field

        for i in range(size):
            button = ttk.Button(
                frame, image=empty_card, compound=tkinter.TOP, text="",
                command=lambda name=name, player=player, index=i: main.select_in_field(name, player, index))
            button.grid(column=grid_start + i, row=0, padx=padding)
            button["state"] = tkinter.DISABLED
            self.cards.append(button)

    def update(self, observer: int) -> None:
        for index, card in enumerate(self.field.get_card_list()):
            if card is not None:
                self.cards[index].config(
                    image=card.get_miniature(observer, hide_face_down=True))
                self.cards[index]["state"] = tkinter.NORMAL
                if card.get_equip_count() > 0:
                    self.cards[index].config(
                        text=f"{card.get_equip_count()} equips")
                else:
                    self.cards[index].config(text="")
            else:
                self.cards[index].config(image=self.empty_card, text="")
                self.cards[index]["state"] = tkinter.DISABLED
