import time
import os
import keyboard
import random

class Enemy:
    def __init__(self,type,ehealth,edmg,espeed):
        self.type = type
        self.ehealth = ehealth
        self.edmg = edmg
        self.espeed = espeed

    def attack(self):
        print(f"{self.type} is attacking")
    
    def damage(self):
        print(f"You damaged {self.type}")

class Player:
    def __init__(self,name,phealth,pdmg,pspeed):
        self.name = name
        self.phealth = phealth
        self.pdmg = pdmg
        self.pspeed = pspeed

class Heal:
    def __init__(self,amount,uses,name):
        self.amount = amount
        self.uses = uses
        self.name = name

class Wepon:
    def __init__(self,damage,name):
        self.damage = damage
        self.name = name

def stats():
    print(f"""Stats:
        Name: {player.name}
        Health: {player.phealth}
        Damage: {player.pdmg}
        Speed: {player.pspeed}""")

Potion_of_Minor_Healing = Heal(5,1,"Potion of Minor Healing")
Potion_of_Healing = Heal(10,2,"Potion of Healing")
wooden_spear = Wepon(3,"Wooden Spear")
stone_spear = Wepon(5,"Stone Spear")
stick = Wepon(1,"Stick")

inventory = []
drops = [Potion_of_Minor_Healing, Potion_of_Healing, wooden_spear, stone_spear, stick]


player_name = input("What is your name?: ")
os.system('cls' if os.name == 'nt' else 'clear')
player = Player(player_name,50,5,10)



goblin = Enemy("goblin",10,1,1)

def goblin_apear():
    print(f"""{goblin.type} has apeared
        Health: {goblin.ehealth}
        Damage: {goblin.edmg}
        Speed: {goblin.espeed}""")
    input()
    while goblin.ehealth > 0:
        goblin.ehealth = goblin.ehealth - player.pdmg
        print(f"You hit goblin. goblin health {goblin.ehealth}")
        time.sleep(1)
        if goblin.ehealth == 0:
            print(f"You defeated {goblin.type}")
            dropnum = random.randint(0, 4)
            print(f"Goblin has dropped {drops[dropnum].name}")
            inventory.append(drops[dropnum])
            break
        player.phealth = player.phealth - goblin.edmg
        print(f"Goblin hit you. Your Health is {player.phealth}")
        


while True:
    choice = input("Would  you like to view your stats, inventory or continue?: ").strip().lower()
    if choice == "stats":
        stats()
    elif choice == "continue":
        os.system('cls' if os.name == 'nt' else 'clear')
        goblin_apear()
        break
    elif choice == "inventory":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(inventory)
    else:
        print("Please select stats or continue")

input()
