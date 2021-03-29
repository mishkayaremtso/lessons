class hero():
    def __init__(self, name, lvl, race):
        self.name = name
        self.lvl = lvl
        self.race = race
        self.health = 100

    def showHero(self):
        message = (self.name + " level is: " + str(self.lvl) + " Race is: "  + self.race + " health lvl: " + str(self.health))
        print(message)

    def upgraeLvl(self):
        self.lvl += 1

    def move(self):
        print("Hero " + self.name + " start moving...")


class SuperHero(hero):
    """super hero class"""
    def __init__(self, name, lvl, race, magiclvl):
        super().__init__(name, lvl, race)
        self.magiclvl = magiclvl
        self.magic = 100

    def make_magic(self):
        self.magic -= 10

    def showHero(self):
        message = (self.name + " level is: " + str(self.lvl) + " Race is: " + self.race + " health lvl: " + str(
            self.health) + " Magic is: " + str(self.magic).title())
        print(message)

