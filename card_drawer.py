from PIL import Image, ImageDraw, ImageFont


class CardDrawer():
    def __init__(self):
        # 26 pt
        # 24 is good!
        self.header_font = ImageFont.truetype("Fonts/MANASPC.TTF", 24)
        # 13 pt
        # 12 is good!
        self.ability_font = ImageFont.truetype("Fonts/MANASPC.TTF", 12)
        # 16pt
        # 16 is good!
        self.attributes_font = ImageFont.truetype(
            "Fonts/MERCUTIONBPSMALLCAPS-V2AA.TTF", 16)
        # 18pt
        # 16 is good!
        self.details_font = ImageFont.truetype("Fonts/RETGANON.TTF", 16)
        # 10pt
        # 12 is good! It actually has some light grey in it
        # I'm not sure if I can get rid of it
        self.flavour_font = ImageFont.truetype("Fonts/ZELDADXT.TTF", 12)

        self.color = (0, 0, 0)

        # Centered
        self.header_y = 23
        self.long_header_y = 8
        # 12 was a bit far to the right. Same for all letters?
        self.ability_pos = (11, 128)
        # Right
        self.ability_value_pos = (219, 128)
        self.ability_attr_pos = (12, 140)
        self.details_pos = (12, 159)
        self.details_spacing = 5

        self.flavor_pos = (12, 301)
        self.flavor_spacing = 11

        self.attributes_pos = (12, 315)
        self.elements_pos = (11, 335)
        # Right
        self.health_pos = (219, 335)

    def draw_header(self, image: ImageDraw, header: str):
        length = image.textlength(header, font=self.header_font)
        x = 116 - length // 2
        image.text((x, self.header_y), header, fill=self.color,
                   font=self.header_font, align="center")

    def draw_long_header(self, image: ImageDraw, header: str):
        length = image.textlength(header, font=self.header_font)
        x = 116 - length // 2
        image.multiline_text((x, self.long_header_y),
                             header, fill=self.color,
                             font=self.header_font, align="center")

    def draw_card_text(self, image: ImageDraw, ability: str, ability_value: str, ability_attr: str,
                       ability_details: str, attributes: str, elements: str, health: str):
        image.text(self.ability_pos, ability,
                   fill=self.color, font=self.ability_font)
        image.text(self.ability_value_pos, ability_value, fill=self.color,
                   font=self.ability_font, align="right")
        image.text(self.ability_attr_pos, ability_attr,
                   fill=self.color, font=self.attributes_font)
        image.multiline_text(self.details_pos, ability_details, fill=self.color,
                             font=self.details_font, spacing=self.details_spacing)
        image.text(self.attributes_pos, attributes,
                   fill=self.color, font=self.attributes_font)
        image.text(self.elements_pos, elements,
                   fill=self.color, font=self.ability_font)
        image.text(self.health_pos, health, fill=self.color,
                   font=self.ability_font, align="right")

    def add_ability(self, image: ImageDraw, space: int, ability: str, ability_value: str, ability_attr: str,
                    ability_details: str):
        pass

    def add_passive(self, image: ImageDraw, space: int, ability: str, ability_value: str, ability_details: str):
        pass

    def add_flavour(self, image: ImageDraw, spaces: int, text: str):
        position = (
            self.flavor_pos[0], self.flavor_pos[1] - self.flavor_spacing * spaces)
        image.multiline_text(
            position, text, fill=self.color, font=self.flavour_font)

    def create_images(self):
        with Image.open("Template empty.png") as image:
            new_image = image.copy()

        draw = ImageDraw.Draw(new_image)
        # Single line header looks fine
        # Cannot measure length of multiline text!
        self.draw_header(draw, "MUFFIN MAN")
        self.draw_card_text(draw, "AN ABILITY", "1", "physical technique",
                            "Does something?\nMaybe not", "muffin", "NORMAL", "5 HP")
        self.add_flavour(draw, 1, "You thought it was a man")
        new_image.show()
        new_image.save("Card images/Muffin man.png")


if __name__ == "__main__":
    card_drawer = CardDrawer()
    card_drawer.create_images()
