from card import Card
from deck import Deck
from field import Field


def move_card(origin: Deck | Field, index: int, destination: Deck | Field, visibility: int = Card.FACE_UP) -> bool:
    """Moves a card from one Deck to another. The moved card retains its equip cards."""

    if destination.has_space():
        card = origin.remove_card(index)
    else:
        return False

    if card is not None:
        destination.add_card(card, visibility)
        return True
    else:
        return False


def discard_equips(holder: Card, discard_1: Deck, discard_2: Deck) -> None:
    """Discards all equip cards of the holder card to their appropriate discard piles.

    Args:
        holder:
            card holding the equips
        discard_1:
            player 1 discard pile
        discard_2:
            player 2 discard pile"""
    equips = holder.unequip_all()

    for equip in equips:
        if equip.owner == 1:
            discard_1.add_card(equip)
        else:
            discard_2.add_card(equip)

# TODO: I need the Filter class in order to implement this. I need to be careful with equip cards
# def move_filtered_cards(self, filter: Filter, destination: Deck | Field, visibility: int = Card.FACE_UP) -> bool:
#         """Moves all filtered cards from their origin decks to the destination.
#         Returns true if all cards were successfully moved."""
#         for i in range(filter.get_size()):
#             if self.move_card(filter.get_deck(), filter.get_index(), destination, visibility):
#                 filter.next()
#             else:
#                 return False
#         return True


def draw(origin: Deck, destination: Deck, amount: int = 1, visibility: int = Card.FACE_UP) -> bool:
    """Moves any number of cards from the top of one Deck to the top of another Deck.
    Not intended to be used on Fields, though it will still work.
    Returns True if the desired amount of cards were moved."""
    for i in range(amount):
        if destination.has_space():
            card = origin.remove_card()
        else:
            return False

        if card is not None:
            destination.add_card(card, visibility)
        else:
            return False
    return True


def equip_card_to(origin: Deck, index: int, destination: Deck, target_index: int, visibility: int = Card.FACE_UP) -> None:
    """Removes a card from one Deck and equips it to another card."""
    equip = origin.remove_card(index)
    equip.set_visibility(visibility)
    card = destination.get_card(target_index)
    card.equip_with(equip)


def add_target(origin: Deck, index: int, destination: Deck, target_index: int) -> None:
    """Adds a target to the card."""
    card = origin.get_card(index)
    target_card = destination.get_card(target_index)
    card.add_target(target_card)
