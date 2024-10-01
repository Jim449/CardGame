from tkinter import ttk
import tkinter
from deck import Deck


class HandGUI():
    def __init__(self, main, frame: ttk.Frame, empty_card: tkinter.PhotoImage,
                 player: int, hand: Deck, size: int = 6):

        self.player: int = player
        self.cards: list[ttk.Button] = []
        self.empty_card = empty_card
        self.hand = hand

        for i in range(size):
            button = ttk.Button(
                frame, image=empty_card,
                command=lambda player=player, index=i: main.select_in_hand(player, index))
            button.grid(column=i+1, row=0)
            button["state"] = tkinter.DISABLED
            self.cards.append(button)

    def update(self, observer: int) -> None:
        cards = self.hand.get_card_list()

        for index in range(len(self.cards)):
            if index < len(cards):
                self.cards[index].config(
                    image=cards[index].get_miniature(observer))
                self.cards[index]["state"] = tkinter.NORMAL
            else:
                self.cards[index].config(image=self.empty_card)
                self.cards[index]["state"] = tkinter.DISABLED
