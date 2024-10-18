import tkinter
from tkinter import tkk
from card import Card
from deck import Deck
from collection import Collection


class DeckBuilder():
    def __init__(self, root, player: int = 1):
        self.player = player
