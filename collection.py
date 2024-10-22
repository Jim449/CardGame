from card import Card

# Note that it should be possible to filter a collection
# The filter class works on Decks, which are based on lists
# It may not work on a collection
# The filter class is used when moving cards between decks
# A filter on collection shouldn't move cards, it only has to filter
# I may not need to write a new module for the collection filter, since it should only be used here


class Collection():
    """Represents a collection of cards. Based on a dictionary,
    a collection is considered unordered and each card has only one entry.
    The entry may represent multiple copies, as indicated by card.get_amount()"""

    def __init__(self):
        """Creates a new, empty collection"""
        self.content: dict[Card] = {}
        self.filter_view: list[Card] = []

    def add_card(self, card: Card, copies: int = 1) -> None:
        """Adds copies a card"""
        if card.id in self.content:
            self.content[card.id].add_amount(copies)
        else:
            self.content[card.id] = card
            card.set_amount(copies)

    def get_card(self, id: int, owner: int) -> Card:
        """Returns a copy of a card in the collection
        and sets the owner of the copy"""
        return self.content[id].give_to(owner)

    def get_size(self) -> int:
        """Returns the amount of unique cards in this collection"""
        return len(self.content)

    def clear_filter(self) -> None:
        """Clears the filter"""
        self.filter_view.clear()

    def apply_filter(self, properties: list[str]) -> None:
        """Includes cards which have all of the given properties."""
        for card in self.content:
            success = True
            for property in properties:
                if not card.has_property(property):
                    success = False
                    break
            if success:
                self.filter_view.append(card)
