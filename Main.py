import tkinter
from game import Game


class Main():
    def __init__(self):
        self.root: tkinter.Tk = tkinter.Tk()
        self.root.geometry("960x640+160+0")
        self.root.resizable(False, False)

    def start_test_game(self):
        game = Game(self.root, 1, 1)
        game.test_setup()


if __name__ == "__main__":
    main = Main()
    main.start_test_game()
    main.root.mainloop()
