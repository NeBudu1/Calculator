class Hero:
    def __init__(self, name, race, health, damage, speed, magicPower, magicList):
        self.Name = name
        self.Race = race
        self.Health = health
        self.Damage = damage
        self.Speed = speed
        self.MagicPower = magicPower
        self.MagicList = magicList
    def heroInfo(self):
        print(f"Информация о герое: Имя: {self.Name}, раса: {self.Race}, жизни: {self.Health}, урон: {self.Damage}, скорость: {self.Speed}, магическая сила: {self.MagicPower}, список магии: {self.MagicList}")
    def healthInfo(self):
        print(f"{self.Name} Осталось столько здоровья: {self.Health}")
    def die(self):
        if (self.Health <= 0):
            return True
hero1 = Hero("Bober", "Ork", 200, 30, 10, 70, [])
hero2 = Hero("Bober222222222", "Elf", 150, 40, 20, 50, [])

def punch(hero1, hero2):
    hero2.Health -= hero1.Damage
    hero2.healthInfo()
    if (hero2.die() == True):
        print(f"{hero2.Name} проиграл")
        return
    input()
    punch(hero2, hero1)
punch(hero1, hero2)
