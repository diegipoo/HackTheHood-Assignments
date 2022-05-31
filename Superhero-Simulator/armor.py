import random


class Armor:

    def __init__(self, name, max_block):

        self.name = name

        self.max_block = max_block

    def block(self):
        block_value = random.randrange(0, self.max_block)
        return block_value

armor1 = Armor("Iron Armor", 70)
armor2 = Armor("Diamond Armor", 90)

print(armor1.block())
