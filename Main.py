import tkinter
from tkinter import ttk
from card import Card
from deck import Deck
from field import Field
from hand_gui import HandGUI
from deck_gui import DeckGUI
from field_gui import FieldGUI
import transitions


class Main():
    def __init__(self, player: int = 1, observer: int = 1):
        self.player: int = player
        self.observer: int = observer
        self.root: tkinter.Tk = tkinter.Tk()
        self.root.geometry("980x640+160+0")
        self.root.resizable(False, False)

        self.selected_location: Deck = None
        self.selected_index: int = None
        self.selected_card: Card = None
        self.selected_gui = None

        self.empty_card: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Large empty card.png")
        self.empty_miniature: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Empty card.png")

        Card.back_image = tkinter.PhotoImage(file="Large card back.png")
        Card.back_miniature = tkinter.PhotoImage(file="Card back.png")

        style = ttk.Style()
        style.configure("TFrame", background="black")
        style.configure("TButton", background="black")

        self.hand_2_frame: ttk.Frame = self.create_frame(0, 0)
        self.field_2_frame: ttk.Frame = self.create_frame(1, 0)
        self.field_1_frame: ttk.Frame = self.create_frame(2, 0)
        self.hand_1_frame: ttk.Frame = self.create_frame(3, 0)

        self.hand_1: Deck = Deck(Card.FACE_DOWN, 6)
        self.hand_2: Deck = Deck(Card.FACE_DOWN, 6)
        self.field_1: Field = Field(Card.FLEXIBLE, 6)
        self.field_2: Field = Field(Card.FLEXIBLE, 6)
        self.deck_1: Deck = Deck(Card.HIDDEN)
        self.deck_2: Deck = Deck(Card.HIDDEN)
        self.discard_1: Deck = Deck(Card.FACE_UP)
        self.discard_2: Deck = Deck(Card.FACE_UP)

        self.hand_gui_1: HandGUI = HandGUI(
            self, self.hand_1_frame, player=1, size=6, empty_card=self.empty_miniature)
        self.hand_gui_2: HandGUI = HandGUI(
            self, self.hand_2_frame, player=2, size=6, empty_card=self.empty_miniature)
        self.field_gui_1: FieldGUI = FieldGUI(
            self, self.field_1_frame, player=1, size=6, empty_card=self.empty_miniature)
        self.field_gui_2: FieldGUI = FieldGUI(
            self, self.field_2_frame, player=2, size=6, empty_card=self.empty_miniature)
        self.deck_gui_1: DeckGUI = DeckGUI(self, self.hand_1_frame, name="Deck",
                                           column=7, player=1, empty_card=self.empty_miniature)
        self.deck_gui_2: DeckGUI = DeckGUI(self, self.hand_2_frame, name="Deck",
                                           column=0, player=2, empty_card=self.empty_miniature)
        self.discard_gui_1: DeckGUI = DeckGUI(
            self, self.hand_1_frame, name="Discard", column=0, player=1, empty_card=self.empty_miniature)
        self.discard_gui_2: DeckGUI = DeckGUI(
            self, self.hand_2_frame, name="Discard", column=7, player=2, empty_card=self.empty_miniature)

        self.selected_card: ttk.Frame = ttk.Frame(
            self.root, width=290, height=440)
        self.selected_card.grid(row=0, column=1, rowspan=3)
        self.card_label: ttk.Label = ttk.Label(
            self.selected_card, image=Card.back_image)
        self.card_label.grid()

        self.option_frame: ttk.Frame = ttk.Frame(
            self.root, width=290, height=160, style="TFrame")
        self.option_frame.grid_propagate(False)
        self.option_frame.grid(row=3, column=1)
        self.end_turn_button: ttk.Button = ttk.Button(
            self.option_frame, text="End turn", command=self.end_turn)
        self.end_turn_button.grid()

        self.hand_menu = tkinter.Menu(
            self.root, background="black", foreground="white")
        self.hand_menu.add_command(label="Play",
                                   command=lambda visibility=Card.FACE_UP: self.play_card(visibility))
        self.hand_menu.add_command(label="Set",
                                   command=lambda visibility=Card.FACE_DOWN: self.play_card(visibility))
        self.hand_menu.add_command(label="Discard",
                                   command=lambda: self.move_card("Discard"))
        # self.hand_menu.add_command(label="Equip", command=self.equip_card)

        self.field_menu = tkinter.Menu(
            self.root, background="black", foreground="white")
        self.field_menu.add_command(label="Destroy",
                                    command=lambda: self.move_card("Discard"))
        self.field_menu.add_command(label="Return to hand",
                                    command=lambda: self.move_card("Hand"))
        # self.field_menu.add_command(label="Activate equip 1", command=lambda equip=1: self.activate_equip(equip))
        # self.field_menu.add_command(label="Activate equip 2", command=lambda equip=2: self.activate_equip(equip))
        # self.field_menu.add_command(label="Activate equip 3", command=lambda equip=3: self.activate_equip(equip))

        self.deck_menu = tkinter.Menu(
            self.root, background="black", foreground="white")
        self.deck_menu.add_command(label="Draw", command=self.draw_card)

        self.discard_menu = tkinter.Menu(
            self.root, background="black", foreground="white")
        self.discard_menu.add_command(
            label="Check", command=self.check_discard)

    def create_frame(self, row: int, column: int, style="TFrame") -> ttk.Frame:
        """Creates a frame to hold a player hand or field"""
        frame = ttk.Frame(self.root, width=670, height=160,
                          style=style)
        frame.grid_propagate(False)
        frame.grid(row=row, column=column)
        return frame

    def test_setup(self) -> None:
        """Adds sample cards to both decks and draws starting hands"""
        sample_card = Card("Sample card", tkinter.PhotoImage(file="Large sample card.png"),
                           tkinter.PhotoImage(file="Sample card.png"))
        for i in range(30):
            self.deck_1.add_card(sample_card.give_to(1))
            self.deck_2.add_card(sample_card.give_to(2))

        self.deck_gui_1.update(self.deck_1, self.observer)
        self.deck_gui_2.update(self.deck_2, self.observer)

        transitions.draw(origin=self.deck_1, destination=self.hand_1, amount=6)
        transitions.draw(origin=self.deck_2, destination=self.hand_2, amount=5)
        self.hand_gui_1.update(self.hand_1, self.observer)
        self.hand_gui_2.update(self.hand_2, self.observer)

    def end_turn(self) -> None:
        """Ends the turn by switching player. The turn player draws a card. Updates gui."""
        if self.player == 1:
            self.player = 2
            if self.observer == 1:
                self.observer = 2
            transitions.draw(origin=self.deck_2, destination=self.hand_2)
            self.deck_gui_2.update(self.deck_2, self.observer)
        elif self.player == 2:
            self.player = 1
            if self.observer == 2:
                self.observer = 1
            transitions.draw(origin=self.deck_1, destination=self.hand_1)
            self.deck_gui_1.update(self.deck_1, self.observer)

        self.hand_gui_1.update(self.hand_1, self.observer)
        self.hand_gui_2.update(self.hand_2, self.observer)
        self.field_gui_1.update(self.field_1, self.observer)
        self.field_gui_2.update(self.field_2, self.observer)

    def get_deck(self, name: str, player: int) -> Deck:
        """Returns a deck or field associated with name and player.

        Args:
            name:
                'Deck', 'Discard', 'Hand' or 'Field'"""
        if name == "Deck":
            if player == 1:
                return self.deck_1
            elif player == 2:
                return self.deck_2
        elif name == "Discard":
            if player == 1:
                return self.discard_1
            elif player == 2:
                return self.discard_2
        elif name == "Hand":
            if player == 1:
                return self.hand_1
            elif player == 2:
                return self.hand_2
        elif name == "Field":
            if player == 1:
                return self.field_1
            elif player == 2:
                return self.field_2

    def get_gui(self, name: str, player: int) -> FieldGUI | DeckGUI | HandGUI:
        """Returns a gui associated with name and player.

        Args:
            name:
                'Deck', 'Discard', 'Hand' or 'Field'"""
        if name == "Deck":
            if player == 1:
                return self.deck_gui_1
            elif player == 2:
                return self.deck_gui_2
        elif name == "Discard":
            if player == 1:
                return self.discard_gui_1
            elif player == 2:
                return self.discard_gui_2
        elif name == "Hand":
            if player == 1:
                return self.hand_gui_1
            elif player == 2:
                return self.hand_gui_2
        elif name == "Field":
            if player == 1:
                return self.field_gui_1
            elif player == 2:
                return self.field_gui_2

    def view_card(self, card: Card, observer: int) -> None:
        """Views the full size image of a card. Depending on visibility and observer,
        views the card back. If card is none, views the empty card image."""
        if card is None:
            self.card_label.config(image=self.empty_card)
        else:
            self.card_label.config(image=card.get_image(observer))

    def show_hand_menu(self) -> None:
        self.hand_menu.tk_popup(
            self.root.winfo_pointerx(), self.root.winfo_pointery())

    def show_field_menu(self) -> None:
        self.field_menu.tk_popup(
            self.root.winfo_pointerx(), self.root.winfo_pointery())

    def show_deck_menu(self) -> None:
        self.deck_menu.tk_popup(
            self.root.winfo_pointerx(), self.root.winfo_pointery())

    def show_discard_menu(self):
        self.discard_menu.tk_popup(
            self.root.winfo_pointerx(), self.root.winfo_pointery())

    def click_deck(self, name: str, player: int) -> None:
        """Views the top card of a deck and shows options for that deck."""
        self.selected_location = self.get_deck(name, player)
        self.selected_card = self.selected_location.get_card(-1)
        self.view_card(self.selected_card, self.observer)
        self.selected_gui = self.get_gui("Deck", player)

        if name == "Deck":
            self.show_deck_menu()
        elif name == "Discard":
            self.show_discard_menu()

    def select_in_hand(self, player: int, index: int) -> None:
        self.selected_location = self.get_deck("Hand", player)
        self.selected_index = index
        self.selected_card = self.selected_location.get_card(index)
        self.selected_gui = self.get_gui("Hand", player)
        self.view_card(self.selected_card, self.observer)
        self.show_hand_menu()

    def select_in_field(self, player: int, index: int) -> None:
        self.selected_location = self.get_deck("Field", player)
        self.selected_index = index
        self.selected_card = self.selected_location.get_card(index)
        self.selected_gui = self.get_gui("Field", player)
        self.view_card(self.selected_card, self.observer)
        self.show_field_menu()

    def check_discard(self) -> None:
        print("Dreadfully sorry! Discard pile checking hasn't been implemented yet!")

    def play_card(self, visibility: int) -> None:
        destination = self.get_deck("Field", self.selected_card.owner)
        if transitions.move_card(origin=self.selected_location, index=self.selected_index,
                                 destination=destination, visibility=visibility):
            self.selected_gui.update(
                self.selected_location, self.observer)
            self.get_gui("Field", self.selected_card.owner).update(
                destination, self.observer)

    def move_card(self, location: str) -> None:
        destination = self.get_deck(location, self.selected_card.owner)
        if transitions.move_card(origin=self.selected_location, index=self.selected_index,
                                 destination=destination):
            self.selected_gui.update(
                self.selected_location, self.observer)
            self.get_gui(location, self.selected_card.owner).update(
                destination, self.observer)

    def draw_card(self) -> None:
        destination = self.get_deck("Hand", self.selected_card.owner)
        if transitions.draw(origin=self.selected_location, destination=destination):
            self.selected_gui.update(
                self.selected_location, self.observer)
            self.get_gui("Hand", self.selected_card.owner).update(
                destination, self.observer)


if __name__ == "__main__":
    main = Main()
    main.test_setup()
    main.root.mainloop()
