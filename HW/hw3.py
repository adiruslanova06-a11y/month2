from abc import  ABC, abstractmethod

class Hero(ABC):    
    def __init__(self, name, health, strength, level):
        self.name = name
        self.__health= health
        self.strength = strength
        self.level = level

    def greet(self):
        print(f"Привет я, {self.name}! мой уровень {self.level} ")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass 

class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом")

class Mage(Hero):
    def attack(self):
        print(f"{self.name} атакует магией")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из под тишка")


warrior = Warrior("Геракл", 100, 20, 5)
warrior.greet()
warrior.rest()
warrior.attack()

mage = Mage("Мерлин", 80, 30, 7)
mage.greet()
mage.rest()
mage.attack()

assassin = Assassin("Шадоу", 70, 25, 6)
assassin.greet()
assassin.rest() 
assassin.attack()
