import random


class Player:
    def __init__(self, leven=100, level=1):
        self.leven = leven
        self.level = level

    def Attack(self):
        damage = random.randint(1, 10)
        self.leven -= damage
        self.level += random.randint(1,5)
        print(f"Nieuw leven:{self.leven} Nieuw level {self.level}")


speler1 = Player()

speler1.Attack()