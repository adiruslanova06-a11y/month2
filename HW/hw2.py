import random

class Hero:
    def __init__(self, name, lv, hp, strength):
        self.name = name
        self.lv = lv
        self.hp = hp
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}")

    def attack(self):
        print(f"{self.name} герой наносит удар!")

class Warrior(Hero):
    def __init__(self, name, lv, hp, strength, stamina):
        super().__init__(name, lv, hp, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def __init__(self, name, lv, hp, strength, mana):
        super().__init__(name, lv, hp, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, lv, hp, strength, stealth):
        super().__init__(name, lv, hp, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} атакует из-под тишка!")


warrior = Warrior("Воин", 5, 100, 20, 50)
mage = Mage("Маг", 5, 80, 15, 100)
assassin = Assassin("Ассасин", 5, 90, 18, 80)

heroes = {
    'воин': warrior,
    'маг': mage,
    'ассасин': assassin
}


beats = {
    'воин': 'ассасин',
    'ассасин': 'маг',
    'маг': 'воин'
}


player_input = input('Введите героя (воин/маг/ассасин): ').lower()

if player_input not in heroes:
    print("Такого героя нет!")
else:
    player_hero = heroes[player_input]
    bot_hero = random.choice(list(heroes.values()))

    print(f"Вы выбрали: {player_hero.name}")
    print(f"Противник: {bot_hero.name}")

    player_name = player_hero.name.lower()
    bot_name = bot_hero.name.lower()
    print(f"----Бьёт: {player_name}")
    print(f"----Противник: {bot_name}")
    if player_name == bot_name:
        print("Ничья!")
    elif beats[player_name] == bot_name:
        print(f"Победил {player_hero.name}!")
    else:
        print(f"Победил {bot_hero.name}!")