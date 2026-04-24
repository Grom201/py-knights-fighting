from knight import Knight
from knight_tournir import KnightTournir


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knightsConfig["lancelot"]
    lancelot = Knight("Lancelot",
                      35,
                      100,
                      [],
                      {
                                "name": "Metal Sword",
                                "power": 50,
                              },
                    None,
                      0)
    arthur = Knight("Arthur",
                     45,
                     75,
                     [
                         {
                "part": "helmet",
                "protection": 15,
                         },
                         {
                "part": "breastplate",
                "protection": 20,
                         },
                         {
                "part": "boots",
                "protection": 10,
                         }
                     ],
                     {
            "name": "Two-handed Sword",
            "power": 55,
                     },
                     None,
                     0
                     )
    mordred = Knight("Mordred",
                     30,
                     90,
                     [
                         {
                             "part": "breastplate",
                             "protection": 15,
                         },
                         {
                             "part": "boots",
                             "protection": 10,
                         }
                     ],
                     {
                         "name": "Poisoned Sword",
                         "power": 60,
                     },
                     {
                         "name": "Berserk",
                         "effect":
                             {
                             "power": +15,
                                 "hp": -5,
                                 "protection": +10,
                             }
                     },
                     0
                     )
    red_knight = Knight("Red Knight",
                        40,
                        70,
                        [
                            {
                                "part": "breastplate",
                                "protection": 25,
                            }
                        ],
                        {
                            "name": "Sword",
                            "power": 45
                        },
                        {
                            "name": "Blessing",
                            "effect": {
                                "hp": +10,
                                "power": +5,
                            }
                        },
                        0)
    # apply armour
    lancelot.apply_armour()
    arthur.apply_armour()
    mordred.apply_armour()
    red_knight.apply_armour()

    # apply weapon
    lancelot.apply_weapon()
    arthur.apply_weapon()
    mordred.apply_weapon()
    red_knight.apply_weapon()

    # apply potion if exist
    lancelot.apply_potion()
    arthur.apply_potion()
    mordred.apply_potion()
    red_knight.apply_potion()

    # -------------------------------------------------------------------------------
    # BATTLE:
    KnightTournir.duel(lancelot, mordred)
    KnightTournir.duel(arthur, red_knight)
    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
