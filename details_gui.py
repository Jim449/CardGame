import tkinter
from tkinter import ttk
from card import Card


class DetailsGUI():
    def __init__(self, main, frame: ttk.Frame, empty_card: tkinter.PhotoImage,
                 empty_miniature: tkinter.PhotoImage, size: int = 3):
        self.empty_card = empty_card
        self.empty_miniature = empty_miniature
        self.size = size
        self.card_label: ttk.Label = ttk.Label(frame, image=empty_card)
        self.card_label.grid(row=0, column=0, rowspan=size, columnspan=size)
        self.equips: list[ttk.Button] = []

        for i in range(size):
            button = ttk.Button(
                frame, image=empty_miniature,
                command=lambda index=i: main.select_equip(index))
            button.grid(column=i, row=size)
            button["state"] = tkinter.DISABLED
            self.equips.append(button)

    def view_card(self, card: Card, observer: int):
        if card is None:
            self.card_label.config(image=self.empty_card)

            for equip in equips:
                equip.config(image=self.empty_miniature)
                equip["state"] = tkinter.NORMAL
        else:
            self.card_label.config(image=card.get_image(observer))
            equip_list = card.get_equips()

            for i in range(self.size):
                if i < len(equip_list):
                    self.equips[i].config(
                        image=equip_list[i].get_miniature(observer))
                    self.equips[i]["state"] = tkinter.NORMAL
                else:
                    self.equips[i].config(image=self.empty_miniature)
                    self.equips[i]["state"] = tkinter.DISABLED
