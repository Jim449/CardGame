import tkinter
from tkinter import ttk
from Hand import Hand
from Field import Field


class Main():
    def __init__(self):
        self.root: tkinter.Tk = tkinter.Tk()
        self.root.geometry("980x640+160+0")
        self.root.resizable(False, False)
        self.back_image: tkinter.PhotoImage = tkinter.PhotoImage(
            file="Large card back.png")

        style = ttk.Style()
        style.configure("TFrame", background="black")
        style.configure("TButton", background="black")

        self.hand_2_frame = self.create_frame(0, 0)
        self.field_2_frame = self.create_frame(1, 0)
        self.field_1_frame = self.create_frame(2, 0)
        self.hand_1_frame = self.create_frame(3, 0)

        self.hand_1 = Hand(self, self.hand_1_frame, player=1, size=6)
        self.hand_2 = Hand(self, self.hand_2_frame, player=2, size=6)
        self.field_1 = Field(self, self.field_1_frame, player=1, size=6)
        self.field_2 = Field(self, self.field_2_frame, player=2, size=6)

        self.selected_card = ttk.Frame(self.root, width=290, height=440)
        self.selected_card.grid(row=0, column=1, rowspan=3)
        self.card_label = ttk.Label(self.selected_card, image=self.back_image)
        self.card_label.grid()

        self.option_frame = ttk.Frame(
            self.root, width=290, height=160, style="TFrame")
        self.option_frame.grid_propagate(False)
        self.option_frame.grid(row=3, column=1)
        self.end_turn = ttk.Button(self.option_frame, text="End turn")
        self.end_turn.grid()

        # Seems like no code ran after the mainloop started
        # Let's draw some cards here
        # With no cards in hand, layout didn't care about adding space between deck and discard
        self.hand_1.draw_card(1)
        self.hand_1.draw_card(1)
        self.hand_1.draw_card(1)
        self.hand_2.draw_card(1)
        self.hand_2.draw_card(1)
        # Kind of works. Except for the layout
        # What if I change the player?
        self.hand_1.set_observer(2)
        self.hand_2.set_observer(2)
        # Yeah, that works fine.
        # Still, I want to do this while the game is ongoing
        # Try adding a command to the end turn button next

        self.root.mainloop()

    def create_frame(self, row: int, column: int, style="TFrame") -> ttk.Frame:
        frame = ttk.Frame(self.root, width=670, height=160,
                          style=style)
        frame.grid_propagate(False)
        frame.grid(row=row, column=column)
        return frame

    def get_root(self) -> tkinter.Tk:
        return self.root

    def view_card(self, card: tkinter.PhotoImage) -> None:
        self.card_label.config(image=card)


if __name__ == "__main__":
    main = Main()
