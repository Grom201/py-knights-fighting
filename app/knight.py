from equipment import armour, weapon, potion
class Knight:
    def __init__(self, name, power, hp, armour: armour, weapon: weapon, potion, protection):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_armour(self):
        # apply armour
        self.protection = 0
        for a in self.armour:
            self.protection += a["protection"]

    def apply_weapon(self):
        # apply weapon
        self.power += self.weapon["power"]

    def apply_potion(self):
        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
