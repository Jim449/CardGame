from tkinter import ttk
import tkinter


class Hand():
    def __init__(self, main, frame: ttk.Frame, player: int = 1, size: int = 6):

        self.main = main
        self.root: tkinter.Tk = main.get_root()
        self.player: int = player
        self.observer: int = 1
        self.cards: list[ttk.Button] = []
        self.hand_size: int = 0
        self.back_image: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Card back.png")
        self.large_back_image: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Large card back.png")
        # TODO Replace with custom card front later
        self.sample_card: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Sample card.png")
        self.large_sample_card: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Large sample card.png")

        self.deck: ttk.Button = ttk.Button(
            frame, image=self.back_image, command=self.click_deck)
        self.discard: ttk.Button = ttk.Button(
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

    def create_buttons(self, frame: ttk.Frame, side: str, size: int = 6) -> None:
        for i in range(size):
            button = ttk.Button(
                frame, image=self.back_image, command=lambda index=i: self.select(index))
            button.grid(column=i+1, row=0)
            button.grid_remove()
            self.cards.append(button)

    def draw_card(self, observer: int) -> None:
        # TODO: this should draw a specific card.
        # The card object should have an image.
        # The cards visibility settings, along with the observer,
        # should determine if the card is displayed face-up or not.
        # Reuse code in CardBase module.
        # If hand size of 6 is exceeded, I need to decide what to do.
        # Don't draw? Or add arrows to traverse hand?
        self.cards[self.hand_size].grid()

        if observer == self.player:
            self.cards[self.hand_size].config(image=self.sample_card)
        else:
            self.cards[self.hand_size].config(image=self.back_image)
        self.hand_size += 1

    def set_observer(self, observer: int) -> None:
        self.observer = observer

        for i in range(self.hand_size):
            # TODO again, replace with something better, using card class
            if observer == self.player:
                self.cards[i].config(image=self.sample_card)
            else:
                self.cards[i].config(image=self.back_image)

    def select(self, index: int) -> None:
        print(f"Selected card {index} in hand!")
        # TODO replace with something better after I add the card class
        if self.player == self.observer:
            self.main.view_card(self.large_sample_card)
        else:
            self.main.view_card(self.large_back_image)
        self.popup.tk_popup(self.root.winfo_pointerx(),
                            self.root.winfo_pointery())

    def play(self):
        print("Play the card!")

    def click_deck(self):
        print("Deck clicked!")

    def click_discard(self):
        print("Discard clicked!")
