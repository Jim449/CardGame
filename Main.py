import tkinter
from tkinter import ttk
from card import Card
from deck import Deck
from field import Field
from hand_gui import HandGUI
from deck_gui import DeckGUI
from field_gui import FieldGUI
from transitions import *


class Main():
    def __init__(self, observer: int = 1):
        self.observer = observer
        self.root: tkinter.Tk = tkinter.Tk()
        self.root.geometry("980x640+160+0")
        self.root.resizable(False, False)
        
        self.empty_card = tkinter.PhotoImage(file="Large empty card.png")
        self.empty_miniature = tkinter.PhotoImage(file="Empty card.png")
        
        Card.back_image = tkinter.PhotoImage(file="Large card back.png")
        Card.back_miniature = tkinter.PhotoImage(file="Card back.png")

        style = ttk.Style()
        style.configure("TFrame", background="black")
        style.configure("TButton", background="black")

        self.hand_2_frame = self.create_frame(0, 0)
        self.field_2_frame = self.create_frame(1, 0)
        self.field_1_frame = self.create_frame(2, 0)
        self.hand_1_frame = self.create_frame(3, 0)

        self.hand_1 = Deck(Card.FACE_DOWN, 6)
        self.hand_2 = Deck(Card.FACE_DOWN, 6)
        self.field_1 = Field(Card.FLEXIBLE, 6)
        self.field_2 = Field(Card.FLEXIBLE, 6)
        self.deck_1 = Deck(Card.HIDDEN)
        self.deck_2 = Deck(Card.HIDDEN)
        self.discard_1 = Deck(Card.FACE_UP)
        self.discard_2 = Deck(Card.FACE_UP)

        self.hand_gui_1 = HandGUI(self, self.hand_1_frame, player=1, size=6, empty_card=self.empty_miniature)
        self.hand_gui_2 = HandGUI(self, self.hand_2_frame, player=2, size=6, empty_card=self.empty_miniature)
        self.field_gui_1 = FieldGUI(self, self.field_1_frame, player=1, size=6, empty_card=self.empty_miniature)
        self.field_gui_2 = FieldGUI(self, self.field_2_frame, player=2, size=6, empty_card=self.empty_miniature)
        self.deck_gui_1 = DeckGUI(self, self.hand_1_frame, name="Deck", image=Card.back_miniature, column=7, player=1, empty_card=self.empty_miniature)
        self.deck_gui_2 = DeckGUI(self, self.hand_2_frame, name="Deck", image=Card.back_miniature, column=0, player=2, empty_card=self.empty_miniature)
        self.discard_gui_1 = DeckGUI(self, self.hand_1_frame, name="Discard", column=0, player=1, empty_card=self.empty_miniature)
        self.discard_gui_2 = DeckGUI(self, self.hand_2_frame, name="Discard", column=7, player=2, empty_card=self.empty_miniature)

        self.selected_card = ttk.Frame(self.root, width=290, height=440)
        self.selected_card.grid(row=0, column=1, rowspan=3)
        self.card_label = ttk.Label(self.selected_card, image=Card.back_image)
        self.card_label.grid()

        self.option_frame = ttk.Frame(
            self.root, width=290, height=160, style="TFrame")
        self.option_frame.grid_propagate(False)
        self.option_frame.grid(row=3, column=1)
        self.end_turn_button = ttk.Button(
            self.option_frame, text="End turn", command=self.end_turn)
        self.end_turn_button.grid()

        self.root.mainloop()

    def create_frame(self, row: int, column: int, style="TFrame") -> ttk.Frame:
        frame = ttk.Frame(self.root, width=670, height=160,
                          style=style)
        frame.grid_propagate(False)
        frame.grid(row=row, column=column)
        return frame

    def end_turn(self) -> None:
        if self.observer == 1:
            self.observer = 2
            self.hand_2.draw_card(self.observer)
        else:
            self.observer = 1
            self.hand_1.draw_card(self.observer)
        self.hand_1.set_observer(self.observer)
        self.hand_2.set_observer(self.observer)

    def get_root(self) -> tkinter.Tk:
        return self.root

    def view_card(self, card: Card, observer: int) -> None:
        self.card_label.config(image=card.get_image(observer))

    def click_deck(self, name: str, player: int) -> None:
        print(f"Clicked deck {name} of player {player}!")
    
    def select_in_hand(self, player: int, index: int) -> None:
        print(f"Clicked card {index} in the hand of player {player}!")

        # self.popup = tkinter.Menu(frame)
        # self.popup.add_command(label="Play", command=self.play)
        # self.popup.tk_popup(self.root.winfo_pointerx(), self.root.winfo_pointery())

    def select_in_field(self, player: int, index: int) -> None:
        print(f"Clicked card {index} in the field of player {player}!")

if __name__ == "__main__":
    main = Main()
