import tkinter
from tkinter import ttk
from Hand import Hand
from Field import Field


class Main():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("980x640+160+0")
        self.root.resizable(False, False)
        self.back_image = tkinter.PhotoImage(file="Large card back.png")

        style = ttk.Style()
        style.configure("TFrame", background="black")
        style.configure("TButton", background="black")

        self.hand_2_frame = self.create_frame(0, 0)
        self.field_2_frame = self.create_frame(1, 0)
        self.field_1_frame = self.create_frame(2, 0)
        self.hand_1_frame = self.create_frame(3, 0)

        self.hand_1 = Hand(self.root, self.hand_1_frame, player=1, size=6)
        self.hand_2 = Hand(self.root, self.hand_2_frame, player=2, size=6)
        self.field_1 = Field(self.root, self.field_1_frame, player=1, size=6)
        self.field_2 = Field(self.root, self.field_2_frame, player=2, size=6)

        self.selected_card = ttk.Frame(self.root, width=290, height=440)
        self.selected_card.grid(row=0, column=1, rowspan=4)
        self.card_label = ttk.Label(self.selected_card, image=self.back_image)
        self.card_label.grid()

        self.root.mainloop()

    def create_frame(self, row: int, column: int, style="TFrame") -> ttk.Frame:
        frame = ttk.Frame(self.root, width=670, height=160,
                          style=style)
        frame.grid_propagate(False)
        frame.grid(row=row, column=column)
        return frame


if __name__ == "__main__":
    main = Main()
