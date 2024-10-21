import tkinter
import json
from game import Game


class Main():
    def __init__(self):
        self.root: tkinter.Tk = tkinter.Tk()
        self.root.geometry("960x640+160+0")
        self.root.resizable(False, False)

    def start_test_game(self):
        game = Game(self.root, 1, 1)
        game.test_setup()

    # Save to json file.
    # Include: name, id, image, miniature, type: bool, secondary type: bool,
    # health: int, spirit: bool, avatar: bool, shrine: bool, spell: bool, area spell: bool
    # Properties of interest when sorting:
    # healing, remove buff, remove debuff, attack up, attack down, defense up, defense down,
    # resistance, incorpereal, immunity, instant death, invisibility, evasion, sure hit,
    # switch, prevent switch, poison, faith, drain faith, psychic, regeneration, counter,
    # prevent healing, self-destruct, unavoidable, ignore invisibility, draw, prevent melee, sleep
    def write_info(self):
        card_list = []
        card_list.append({"name": "Black cat", "id": 1,
                         "image": "Black cat.png", "miniature": "Black cat miniature.png",
                          "normal": True, "void": True, "spirit": True, "ignore defense": True,
                          "evasion": True, "sharp senses": True, "beast": True})
        card_list.append({"name": "Black hound", "id": 2,
                         "image": "Black hound.png", "miniature": "Black hound miniature.png",
                          "normal": True, "void": True, "spirit": True, "instant death": True,
                          "sharp senses": True, "beast": True})
        card_list.append({"name": "Beholder", "id": 3,
                         "image": "Placeholder.png", "miniature": "Beholder miniature.png",
                          "void": True, "spirit": True, "strange mind": True})
        card_list.append({"name": "Slime", "id": 4,
                         "image": "Placeholder.png", "miniature": "Slime miniature.png",
                          "poison": True, "void": True, "spirit": True, "defense down": True,
                          "regeneration": True})
        card_list.append({"name": "Imp", "id": 5,
                          "image": "Placeholder.png", "miniature": "Imp miniature.png",
                          "void": True, "fire": True, "spirit": True, "drain faith": True,
                          "switch": True})
        card_list.append({"name": "Nightmare", "id": 6,
                         "image": "Placeholder.png", "miniature": "Nightmare miniature.png",
                          "fire": True, "ghost": True, "spirit": True})
        card_list.append({"name": "Demonic shrine", "id": 7,
                         "image": "Placeholder.png", "miniature": "Demonic shrine miniature.png",
                          "shrine": True})
        card_list.append({"name": "Demon", "id": 8,
                         "image": "Placeholder.png", "miniature": "Demon miniature.png",
                          "void": True, "fire": True, "avatar": True, "regeneration": True})
        card_list.append({"name": "Burning remains", "id": 9,
                         "image": "Burning remains.png", "miniature": "Burning remains miniature.png",
                          "fire": True, "ghost": True, "spirit": True, "counter": True, "undead": True})
        card_list.append({"name": "Shadow", "id": 10,
                         "image": "Placeholder.png", "miniature": "Shadow miniature.png",
                          "ghost": True, "void": True, "spirit": True, "strange mind": True,
                          "switch": True})
        card_list.append({"name": "Gargoyle", "id": 11,
                         "image": "Placeholder.png", "miniature": "Gargoyle miniature.png",
                          "earth": True, "ghost": True, "spirit": True, "defense up": True,
                          "elemental": True})
        card_list.append({"name": "Dust spirit", "id": 12,
                         "image": "Placeholder.png", "miniature": "Dust spirit miniature.png",
                          "earth": True, "ghost": True, "spirit": True, "prevent healing": True})
        card_list.append({"name": "Earth shrine", "id": 13,
                         "image": "Placeholder.png", "miniature": "Earth shrine miniature.png",
                          "shrine": True})
        card_list.append({"name": "Dust dragon", "id": 14,
                         "image": "Placeholder.png", "miniature": "Dust dragon miniature.png",
                          "earth": True, "avatar": True, "resistance": True})
        card_list.append({"name": "Behemoth", "id": 15,
                         "image": "Placeholder.png", "miniature": "Behemoth miniature.png",
                          "earth": True, "normal": True, "avatar": True})
        card_list.append({"name": "Shrine of death", "id": 16,
                         "image": "Placeholder.png", "miniature": "Shrine of death miniature.png",
                          "shrine": True})
        card_list.append({"name": "Bone dragon", "id": 17,
                         "image": "Placeholder.png", "miniature": "Bone dragon miniature.png",
                          "ghost": True, "divine": True, "avatar": True, "undead": True,
                          "resistance": True})
        card_list.append({"name": "Black knight", "id": 18,
                         "image": "Placeholder.png", "miniature": "Black knight miniature.png",
                          "ghost": True, "avatar": True, "undead": True, "instant death": True})
        card_list.append({"name": "Drowned soul", "id": 19,
                         "image": "Drowned soul.png", "miniature": "Drowned soul miniature.png",
                          "water": True, "ghost": True, "spirit": True, "undead": True,
                          "attack down": True, "prevent switch": True})
        card_list.append({"name": "Spectre", "id": 20,
                         "image": "Placeholder.png", "miniature": "Spectre miniature.png",
                          "ghost": True, "spirit": True, "undead": True, "incorpereal": True,
                          "drain health": True, "drain faith": True})
        card_list.append({"name": "Armadillo", "id": 21,
                         "image": "Placeholder.png", "miniature": "Armadillo miniature.png",
                          "normal": True, "earth": True, "spirit": True, "beast": True,
                          "defense up": True})
        card_list.append({"name": "Golem", "id": 22,
                         "image": "Placeholder.png", "miniature": "Golem miniature.png",
                          "earth": True, "spirit": True, "elemental": True, "resistance": True})
        card_list.append({"name": "Gravity rock", "id": 23,
                         "image": "Placeholder.png", "miniature": "Gravity rock miniature.png",
                          "earth": True, "void": True, "spirit": True, "strange mind": True,
                          "sure hit": True, "self-destruction": True, "instant death": True})
        card_list.append({"name": "Magma golem", "id": 24,
                         "image": "Placeholder.png", "miniature": "Magma golem miniature.png",
                          "fire": True, "earth": True, "spirit": True, "elemental": True,
                          "counter": True})
        card_list.append({"name": "Fire spirit", "id": 25,
                         "image": "Placeholder.png", "miniature": "Fire spirit miniature.png",
                          "fire": True, "spirit": True, "elemental": True, "healing": True,
                          "summoner": True})
        card_list.append({"name": "Salamander", "id": 26,
                         "image": "Placeholder.png", "miniature": "Salamander miniature.png",
                          "fire": True, "spirit": True, "regeneration": True})
        card_list.append({"name": "Shrine of fire", "id": 27,
                         "image": "Placeholder.png", "miniature": "Shrine of fire miniature.png",
                          "shrine": True})
        card_list.append({"name": "Efreet", "id": 28,
                         "image": "Placeholder.png", "miniature": "Efreet miniature.png",
                          "fire": True, "avatar": True, "elemental": True, "counter": True})
        card_list.append({"name": "Phoenix", "id": 29,
                         "image": "Placeholder.png", "miniature": "Phoenix miniature.png",
                          "fire": True, "divine": True, "avatar": True})
        card_list.append({"name": "Dragon shrine", "id": 30,
                         "image": "Placeholder.png", "miniature": "Dragon shrine miniature.png",
                          "shrine": True})
        card_list.append({"name": "Black dragon", "id": 31,
                         "image": "Placeholder.png", "miniature": "Black dragon miniature.png",
                          "fire": True, "divine": True, "avatar": True, "resistance": True})
        card_list.append({"name": "Astral dragon", "id": 32,
                         "image": "Placeholder.png", "miniature": "Astral dragon miniature.png",
                          "ghost": True, "divine": True, "avatar": True, "resistance": True,
                          "psychic": True})
        card_list.append({"name": "Farseer", "id": 33,
                         "image": "Placeholder.png", "miniature": "Farseer miniature.png",
                          "divine": True, "spirit": True, "sure hit": True})
        card_list.append({"name": "Fox spirit", "id": 34,
                         "image": "Placeholder.png", "miniature": "Fox spirit miniature.png",
                          "divine": True, "spirit": True, "beast": True, "add faith": True})
        card_list.append({"name": "Scarab", "id": 35,
                         "image": "Placeholder.png", "miniature": "Scarab miniature.png",
                          "divine": True, "earth": True, "spirit": True, "draw": True})
        card_list.append({"name": "Frost giant", "id": 36,
                         "image": "Placeholder.png", "miniature": "Frost giant miniature.png",
                          "water": True, "spirit": True, "attack down": True})
        card_list.append({"name": "Kappa", "id": 37,
                         "image": "Placeholder.png", "miniature": "Kappa miniature.png",
                          "water": True, "spirit": True, "instant death": True})
        card_list.append({"name": "Shrine of water", "id": 38,
                         "image": "Placeholder.png", "miniature": "Shrine of water miniature.png",
                          "shrine": True})
        card_list.append({"name": "Water serpent", "id": 39,
                         "image": "Placeholder.png", "miniature": "Water serpent miniature.png",
                          "water": True, "divine": True, "avatar": True, "immunity": True})
        card_list.append({"name": "Shen", "id": 40,
                         "image": "Placeholder.png", "miniature": "Shen miniature.png",
                          "water": True, "avatar": True, "sleep": True})
        card_list.append({"name": "Water elemental", "id": 41,
                         "image": "Placeholder.png", "miniature": "Water elemental miniature.png",
                          "water": True, "spirit": True, "elemental": True, "healing": True})
        card_list.append({"name": "White snake", "id": 42,
                         "image": "Placeholder.png", "miniature": "White snake miniature.png",
                          "divine": True, "spirit": True, "drain health": True, "remove debuff": True})
        card_list.append({"name": "Sprite", "id": 43,
                         "image": "Placeholder.png", "miniature": "Sprite miniature.png",
                          "divine": True, "earth": True, "spirit": True, "elemental": True,
                          "healing": True})
        card_list.append({"name": "Giant rat", "id": 44,
                         "image": "Placeholder.png", "miniature": "Giant rat miniature.png",
                          "normal": True, "poison": True, "spirit": True, "beast": True,
                          "sharp senses": True, "poisonous": True})
        card_list.append({"name": "Troll", "id": 45,
                         "image": "Placeholder.png", "miniature": "Troll miniature.png",
                          "normal": True, "spirit": True, "regeneration": True})
        card_list.append({"name": "Mist wolf", "id": 46,
                         "image": "Placeholder.png", "miniature": "Mist wolf miniature.png",
                          "normal": True, "ghost": True, "sharp senses": True})
        card_list.append({"name": "Scorpion", "id": 46,
                         "image": "Placeholder.png", "miniature": "Scorpion miniature.png",
                          "poison": True, "spirit": True, "poisonous": True})
        card_list.append({"name": "Shrine of disaster", "id": 47,
                         "image": "Placeholder.png", "miniature": "Shrine of disaster miniature.png",
                          "shrine": True})
        card_list.append({"name": "Basilisk", "id": 48,
                         "image": "Placeholder.png", "miniature": "Basilisk miniature.png",
                          "poison": True, "avatar": True, "poisonous": True, "instant death": True})
        card_list.append({"name": "Hydra", "id": 49,
                         "image": "Placeholder.png", "miniature": "Hydra miniature.png",
                          "poison": True, "divine": True, "avatar": True, "poisonous": True,
                          "regeneration": True})
        card_list.append({"name": "Plane walker", "id": 50,
                         "image": "Placeholder.png", "miniature": "Plane walker miniature.png",
                          "void": True, "spirit": True, "strange mind": True,
                          "ignore defense": True, "switch": True})
        card_list.append({"name": "Werewolf", "id": 51,
                         "image": "Placeholder.png", "miniature": "Werewolf miniature.png",
                          "normal": True, "spirit": True, "beast": True,
                          "sharp senses": True, "attack up": True})
        card_list.append({"name": "Tengu", "id": 52,
                         "image": "Placeholder.png", "miniature": "Tengu miniature.png",
                          "storm": True, "ghost": True, "spirit": True,
                          "prevent attack": True, "remove buffs": True})
        card_list.append({"name": "Spirit weasel", "id": 53,
                         "image": "Placeholder.png", "miniature": "Spirit weasel miniature.png",
                          "storm": True, "spirit": True, "beast": True, "sharp senses": True,
                          "sure hit": True, "evasion": True})
        card_list.append({"name": "Shrine of storm", "id": 54,
                         "image": "Placeholder.png", "miniature": "Shrine of storm miniature.png",
                          "shrine": True})
        card_list.append({"name": "Thunderbird", "id": 55,
                         "image": "Placeholder.png", "miniature": "Thunderbird miniature.png",
                          "storm": True, "avatar": True, "sure hit": True})
        card_list.append({"name": "Garuda", "id": 56,
                         "image": "Placeholder.png", "miniature": "Garuda miniature.png",
                          "storm": True, "avatar": True, "beast": True, "sharp senses": True,
                          "prevent attack": True})
        card_list.append({"name": "Sand wyrm", "id": 57,
                         "image": "Placeholder.png", "miniature": "Sand wyrm miniature.png",
                          "earth": True, "void": True, "instant death": True, "defense up": True})

        with open("Card info/Card info.json", "w") as file:
            json.dump(card_list, file)


if __name__ == "__main__":
    main = Main()
    main.start_test_game()
    main.root.mainloop()
