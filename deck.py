from card import Card


class Deck:
    """Represents a collection of cards.
    A deck has no max size and no empty spots.
    A deck has a visibility setting, which will be applied
    to all cards added to the deck."""

    def __init__(self, visibility: int, max_size: int | None = None) -> None:
        """Creats a new deck. Sets visibility as FACE_UP, FACE_DOWN, HIDDEN or FLEXIBLE,
        whereas FLEXIBLE means added card can have individual visibility settings."""
        self.content: list[Card] = list()
        self.visibility: int = visibility
        self.max_size = max_size

    def add_card(self, card: Card, visibility: int = Card.FACE_UP) -> bool:
        """Adds a card to this deck. The card will inherit visibility settings
        from this deck, unless deck has FLEXIBLE visibility."""
        if self.has_space():
            self.content.append(card)
        else:
            return False
        
        if self.visibility == Card.FLEXIBLE:
            card.set_visibility(visibility)
        else:
            card.set_visibility(self.visibility)
        return True

    def get_card(self, index: int) -> Card | None:
        """Returns the card at index, or None"""
        try:
            return self.content[index]
        except IndexError:
            return None

    def unequip_all(self, index: int) -> list[Card]:
        """Unequips all cards from the card at index"""
        try:
            card: Card = self.content[index]
            equips = card.unequip_all()
            return equips
        except IndexError:
            return []

    def remove_card(self, index: int = -1) -> Card | None:
        """Removes a card and returns it"""
        try:
            return self.content.pop(index)
        except IndexError:
            return None

    def get_size(self) -> int:
        """Returns deck size"""
        return len(self.content)

    def get_card_list(self) -> list[Card]:
        return self.content

    def has_space(self) -> bool:
        """Returns true if there is space for one more card in this deck"""
        if self.max_size is None:
            return True
        elif len(self.content) < self.max_size:
            return True
        else:
            return False
