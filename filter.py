from deck import Deck
from card import Card


class Filter(Deck):
    """A filter view. Cards can be selected using their properties.
    Use the include-methods to add cards to the filter.
    Then, use exclude-methods to remove cards from the filter.
    Use get_deck and get_index to retrieve the position of a filtered card.
    Then, use 'next' to go to the next entry.
    """

    def __init__(self):
        """Creates a new, empty filter."""
        self.content: list[Card] = []
        self.decks: list[Deck] = []
        self.indices: list[int] = []

    def include_card(self, card: Card, location: Deck, index: int) -> None:
        """Includes a single card in the filter."""
        # Sort in ascending order
        # Items will be returned starting from the last item
        # This should prevent index troubles when removing cards from location decks
        for i, existing in enumerate(self.indices):
            if index < existing:
                self.content.insert(i, card)
                self.decks.insert(i, location)
                self.indices.insert(i, index)
                return
        self.content.append(card)
        self.decks.append(location)
        self.indices.append(index)

    def include_any_property(self, location: Deck, properties: list[str]) -> None:
        """Includes cards which have any of the given properties."""
        for index, card in enumerate(location.get_card_list()):
            if card is None:
                continue
            for property in properties:
                if card.has_property(property):
                    self.include_card(card, location, index)
                    break

    def include_all_properties(self, location: Deck, properties: list[str]) -> None:
        """Includes cards which have all of the given properties."""

        for index, card in enumerate(location.get_card_list()):
            success = True
            if card is None:
                continue
            for property in properties:
                if not card.has_property(property):
                    success = False
                    break
            if success:
                self.include_card(card, location, index)

    def include_location(self, location: Deck) -> None:
        """Includes all cards in a location."""
        for index, card in enumerate(location.get_card_list()):
            if card is not None:
                self.include_card(card, location, index)

    def exclude_property(self, properties: list[str]) -> None:
        """Exclude filtered cards which have any of the given properties."""
        for i in range(len(self.content - 1), -1, -1):
            for property in properties:
                if self.content[i].has_property(property):
                    del self.content[i]
                    del self.decks[i]
                    del self.indices[i]
                    break

    def select(self, selection: list[int]) -> None:
        """Saves a selection of cards and removes the rest.

        Args:
            selection:
                indices of cards in filter"""
        for i in range(len(self.content - 1), -1, -1):
            if i not in selection:
                del self.content[i]
                del self.decks[i]
                del self.indices[i]

    def add_card(self, card: Card, visibility: int = 1) -> bool:
        """Does nothing and returns false."""
        return False

    def shuffle(self) -> bool:
        """Does nothing and returns false."""
        return False

    def remove_card(self, index: int = -1) -> Card | None:
        """Excludes a card from this filter and returns it."""
        try:
            card = self.content.pop(index)
            self.decks.pop(index)
            self.indices.pop(index)
            return card
        except:
            return None

    def get_card(self) -> Card:
        """Returns a filtered card."""
        return self.content[-1]

    def get_deck(self) -> Deck:
        """Returns the deck of a filtered card."""
        return self.decks[-1]

    def get_index(self) -> int:
        """Returns the index of a filtered card."""
        return self.indices[-1]

    def next(self) -> None:
        """Removes the last items in the filter so that previous items can be accessed."""
        del self.content[-1]
        del self.decks[-1]
        del self.indices[-1]
