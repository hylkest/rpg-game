import random

class Player:
    def __init__(self, role, leven=100, level=1):
        self.leven = leven
        self.level = level
        self.role = role

    def Attack(self):
        damage = random.randint(1, 10)
        self.leven -= damage
        self.level += random.randint(1, 5)
        print(f"Je hebt iemand aangevallen. Jouw leven is nu: {self.leven}% !")

    def info(self):
        print(f"Leven: {self.leven} Level: {self.level} Rol: {self.role}")

speler1 = Player("test")

speler1.Attack()
speler1.info()
