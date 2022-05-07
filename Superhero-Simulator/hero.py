from unicodedata import name


class Hero:

    def __init__(self, name, start_hp = 100):

        self.name = name

        self.hp = start_hp

        self.current_hp = start_hp

if __name__ == "__main__":

    diegos_hero = Hero("Diego Crusher", 100)
    print(diegos_hero.name)
    print(diegos_hero.current_hp)
