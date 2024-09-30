from deck import Deck
from card import Card


class Field(Deck):
    """Represents a collection of cards.
    A field has a constant size and may include empty spaces.
    A field has a visibility setting, which will be applied
    to all cards added to the field."""

    def __init__(self, visibility: int, size: int) -> None:
        """Creats a new field. Sets visibility as FACE_UP, FACE_DOWN, HIDDEN or FLEXIBLE,
        whereas FLEXIBLE means added card can have individual visibility settings."""
        self.content: list = [None for x in range(size)]
        self.visibility: int = visibility
        self.size: int = size

    def add_card(self, card: Card, visibility: int = Card.FACE_UP) -> bool:
        """Adds a card to the first unoccupied spot in the field.
        Returns true if successful. Added card inherits visibility
        settings from this field."""
        for i, spot in enumerate(self.content):
            if spot is None:
                self.content[i] = card
                if self.visibility == Card.FLEXIBLE:
                    card.set_visibility(visibility)
                else:
                    card.set_visibility(self.visibility)
                return True
        return False

    def insert_card(self, card: Card, index: int) -> bool:
        """Refrains from inserting a card and returns false"""
        return False

    def shuffle(self) -> bool:
        """Refrains from shuffling cards and returns false"""
        return False

    def remove_card(self, index: int) -> Card:
        """Removes a card at index and returns it."""
        try:
            card: Card = self.content[index]
            card.leave_field()
            self.content[index] = None
            return card
        except IndexError:
            return None

    def view_all(self, observer: int) -> str:
        """Views all cards on this field."""
        text = ""
        for card in self.content:
            if card is not None:
                text += f"{card.view(observer)
                           } ({card.view_equips(observer)})\n"
            else:
                text += "-\n"
        return text

    def has_space(self) -> bool:
        """Returns true if this field has space for another card"""
        if None in self.content:
            return True
        else:
            return False
