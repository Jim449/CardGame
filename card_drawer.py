from PIL import Image, ImageDraw, ImageFont


class CardDrawer():
    def __init__(self):
        self.header_font = ImageFont.truetype("Fonts/MANASPC.TTF", 24)
        self.ability_font = ImageFont.truetype("Fonts/MANASPC.TTF", 12)
        self.attributes_font = ImageFont.truetype(
            "Fonts/MERCUTIONBPSMALLCAPS-V2AA.TTF", 16)
        self.details_font = ImageFont.truetype("Fonts/RETGANON.TTF", 16)
        self.flavour_font = ImageFont.truetype("Fonts/ZELDADXT.TTF", 11)

        self.color = (0, 0, 0)

        self.header_y = 23
        self.long_header_y = 9
        self.header_spacing = 9

        self.ability_x = 11
        self.ability_y = 128
        self.line_y = 141
        self.line_start = 12
        self.line_end = 219
        self.value_x = 221
        self.ability_attr_x = 12
        self.ability_attr_y = 140
        self.details_x = 12
        self.details_y = 159
        self.details_spacing = 5
        self.details_height = 17
        self.ability_height = 40

        self.flavour_x = 12
        self.flavour_y = 308
        self.flavour_spacing = 2

        self.attributes_pos = (12, 315)
        self.elements_y = 335

    def draw_header(self, image: ImageDraw, header: str):
        length = image.textlength(header, font=self.header_font)
        x = 116 - length // 2
        image.text((x, self.header_y), header, fill=self.color,
                   font=self.header_font)

    def draw_long_header(self, image: ImageDraw, header: str):
        box = image.multiline_textbbox((0, 0), header, font=self.header_font,
                                       spacing=self.header_spacing)
        # Box[2] = right side, equals length in this case
        x = 116 - box[2] // 2
        image.multiline_text((x, self.long_header_y), header, fill=self.color,
                             font=self.header_font, spacing=self.header_spacing)

    def draw_footer(self, image: ImageDraw, attributes: str, elements: str, health: str):
        length = image.textlength(health, font=self.ability_font)
        x = self.value_x - length
        image.text(self.attributes_pos, attributes,
                   fill=self.color, font=self.attributes_font)
        image.text((self.ability_x, self.elements_y), elements,
                   fill=self.color, font=self.ability_font)
        image.text((x, self.elements_y), health, fill=self.color,
                   font=self.ability_font)

    def draw_ability(self, image: ImageDraw, ability: str, ability_attr: str,
                     ability_details: str = "", ability_value: str = "", spacing: int = 0):
        if spacing > 0:
            pushdown = self.ability_height + spacing * self.details_height
        else:
            pushdown = 0

        length = image.textlength(ability_value, font=self.ability_font)
        x = self.value_x - length

        image.text((self.ability_x, self.ability_y + pushdown), ability,
                   fill=self.color, font=self.ability_font)
        image.text((x, self.ability_y + pushdown), ability_value, fill=self.color,
                   font=self.ability_font)
        image.text((self.ability_attr_x, self.ability_attr_y + pushdown), ability_attr,
                   fill=self.color, font=self.attributes_font)
        image.multiline_text((self.details_x, self.details_y + pushdown), ability_details,
                             fill=self.color, font=self.details_font,
                             spacing=self.details_spacing)
        image.line([self.line_start, self.line_y + pushdown, self.line_end, self.line_y + pushdown],
                   fill=self.color)

    def add_flavour(self, image: ImageDraw, text: str):
        box = image.multiline_textbbox((0, 0), text, font=self.flavour_font,
                                       spacing=self.flavour_spacing)
        # box[3] = bottom side of text box, equal to height in this case
        image.multiline_text((self.flavour_x, self.flavour_y - box[3]), text,
                             fill=self.color, font=self.flavour_font,
                             spacing=self.flavour_spacing)

    def create_images(self):
        with Image.open("Template empty.png") as image:
            new_image = image.copy()
            draw = ImageDraw.Draw(new_image)
            self.draw_long_header(draw, "DEATH\nKNIGHT")
            self.draw_ability(draw, "EXCECUTION", "infused ghost technique",
                              ability_details="Inflicts instant death", ability_value="8")
            self.draw_ability(draw, "WEAKNESS", "ghost spell",
                              ability_details="Decreases attack by 1",
                              ability_value="", spacing=1)
            self.draw_footer(draw, "undead",
                             "GHOST", "8 HP")
            self.add_flavour(draw, "The incarnation\nof death")
            new_image.save("Card images/Death knight.png")

            new_image = image.copy()
            draw = ImageDraw.Draw(new_image)
            self.draw_header(draw, "DEMON")
            self.draw_ability(draw, "FIRE BLADE", "infused fire technique",
                              ability_details="Strikes with a fiery sword", ability_value="4")
            self.draw_ability(draw, "DEMON PORTAL", "void spell",
                              ability_details="Switches this unit\nin or out",
                              ability_value="", spacing=1)
            self.draw_footer(
                draw, "demonic", "VOID, FIRE", "8 HP")
            self.add_flavour(
                draw, "A powerful force\nof evil")
            new_image.save("Card images/Demon.png")


if __name__ == "__main__":
    card_drawer = CardDrawer()
    card_drawer.create_images()
