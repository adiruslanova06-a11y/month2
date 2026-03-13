from abc import ABC, abstractmethod



class Hero(ABC):
    def __init__(self, name,level, health,strengh):
        self.name=name
        self.level=level
        self.__health=100
        self.strength=strengh

    def greet(self):
        print(f"Привет {self.name},{self.level}")

    def rest(self):
        self.__health += 1
        print(self.name,"отдыхает" ,self.__health)

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(self.name," воин атакует мечом")

class Mage(Hero):
    def attack(self):
        print(self.name, "Маг использует магию")

class Assassin(Hero):
    def attack(self):
        print(self.name,"Ассассин атакует из-под тишка")

Warrior = Warrior("Thor", 25, 250, 435)
Mage = Mage("Deep", 34, 23, 435)
Assassin = Assassin("Shadow", 25, 23, 235)


Warrior.greet()
Mage.greet()
Assassin.greet()

Warrior.attack()
Mage.attack()
Assassin.attack()

Warrior.rest()
Mage.rest()
Assassin.rest()




