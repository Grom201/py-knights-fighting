from equipment import armour, weapon, potion
class Knight:
    def __init__(self, name, power, hp, armour: armour, weapon: weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self):
        # apply armour
        self.armour.protection = 0
        for a in self.armour:
            self.armour["protectiom"] += a["protection"]

    def apply_weapon(self):
        # apply weapon
        self.power += self.weapon["power"]

    def apply_potion(self):
        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]

            if "protection" in self.potion.effect:
                self.armour.protection += self.potion.effect["protection"]

            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
