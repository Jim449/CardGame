from tkinter import PhotoImage
from typing import Self
from typing import Any


class Card:
    """Represents a card of any kind.
    Initially, a card has no owner. It can be copied into a players collection
    using the method 'give_to'. A card has a face and a back.
    Card visibility and observer identity determines if a player can look at the card face.
    A card may be equipped with other cards.
    A card has a target list, representing cards which the card is played against."""
    FLEXIBLE: int = 3
    FACE_UP: int = 2
    FACE_DOWN: int = 1
    HIDDEN: int = 0
    ALL_SEEING: int = 0

    back_image: PhotoImage = None
    back_miniature: PhotoImage = None

    def __init__(self, id: int, name: str, image: PhotoImage, miniature: PhotoImage,
                 properties: dict[str, Any] = None) -> None:
        """Instantiates an ownerless card"""
        self.id = id
        self.name: str = name
        self.image: PhotoImage = image
        self.miniature: PhotoImage = miniature
        self.owner: int = 0
        self.visibility: int = 0
        self.amount: int = 1
        self.target_list: list[Card] = []
        self.targeted_by: list[Card] = []
        self.equip_list: list[Card] = []
        self.equipped_by: Card = None

        if properties is None:
            self.properties: dict[str, Any] = {"name": self.name}
        else:
            self.properties: dict[str, Any] = properties

    def give_to(self, player: int) -> Self:
        """Returns a copy of this card, with ownership set to player"""
        copy: Card = Card(self.name, self.image,
                          self.miniature, self.properties)
        copy.owner = player
        copy.amount = 1
        return copy

    def set_visibility(self, visibility: int) -> None:
        """Sets card visibility out of FACE-UP: visible to anyone.
        FACE-DOWN: visible to owner. HIDDEN: invisible to all"""
        self.visibility = visibility

    def is_facedown(self):
        return self.visibility == Card.FACE_DOWN or self.visibility == Card.HIDDEN

    def can_view(self, observer: int, hide_face_down: bool = False) -> bool:
        """Returns true if the observer is authorized to view card front"""
        if self.visibility == Card.FACE_DOWN and hide_face_down:
            return False
        elif self.visibility == Card.FACE_UP or observer == Card.ALL_SEEING:
            return True
        elif self.visibility == Card.FACE_DOWN and observer == self.owner:
            return True
        else:
            return False

    def get_name(self, observer: int) -> str:
        """Returns card name if observer has sufficient permissions.
        Otherwise, returns 'Unknown card'."""
        if self.can_view(observer):
            return self.name
        else:
            return "Unknown card"

    def get_image(self, observer: int, hide_face_down: bool = False) -> PhotoImage:
        """Returns card front if observer has sufficient permissions.
        Otherwise, returns card back."""
        if self.can_view(observer, hide_face_down):
            return self.image
        else:
            return self.back_image

    def get_miniature(self, observer: int, hide_face_down: bool = False) -> PhotoImage:
        """Returns miniature card front if observer has sufficient permissions.
        Otherwise, returns miniature card back."""
        if self.can_view(observer, hide_face_down):
            return self.miniature
        else:
            return self.back_miniature

    def play_against(self, targets: list) -> None:
        """Sets the target list of this card"""
        self.target_list = targets.copy()
        for target in targets:
            target.targeted_by.append(self)

    def add_target(self, target: Self) -> None:
        """Adds a target to the target list"""
        self.target_list.append(target)
        target.targeted_by.append(self)

    def get_equips(self) -> list[Self]:
        """Returns equipped cards"""
        return self.equip_list

    def get_equip(self, index: int) -> Self:
        """Returns an equipped card"""
        return self.equip_list[index]

    def get_equip_count(self) -> int:
        """Returns amount of cards equipped"""
        return len(self.equip_list)

    def equip_with(self, card: Self) -> None:
        """Equips another card to this card"""
        self.equip_list.append(card)
        card.equipped_by = self

    def unequip(self) -> Self:
        """Unequips this card from the card it is equipped to"""
        self.equipped_by.equip_list.remove(self)
        self.equipped_by = None
        return self

    def unequip_all(self) -> list[Self]:
        """Unequips all cards equipped to this card.

        Returns:
        the equipped cards"""
        for card in self.equip_list:
            card.equipped_by = None
            card.leave_field()
        equips = self.equip_list
        self.equip_list = []
        return equips

    def leave_field(self) -> None:
        """Empties this cards target list. Removes this card
        from the target list of any other card."""
        for card in self.targeted_by:
            card.targetList.remove(self)
        for card in self.target_list:
            self.targetList.remove(card)
        self.targeted_by = []
        self.target_list = []

    def has_property(self, property: str) -> bool:
        """Returns true if this card has the given property"""
        return property in self.properties

    def get_property(self, property: str) -> Any:
        """Returns the value of a property"""
        return self.properties[property]

    def add_property(self, property: str, value: Any) -> None:
        """Adds a property to this card"""
        self.properties[property] = value

    def remove_property(self, property: str) -> None:
        """Removes a property from this card, if it has it"""
        try:
            self.properties.remove(property)
        except ValueError:
            pass

    def get_amount(self) -> int:
        """Returns the amount of copies"""
        return self.amount

    def set_amount(self, value: int) -> None:
        """Sets the amount of copies"""
        self.amount = value

    def add_amount(self, value: int) -> None:
        """Adds copies"""
        self.amount += value
