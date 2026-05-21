import time
import os
import keyboard
import random

class Enemy:
    def __init__(self,type,ehealth,edmg):
        self.type = type
        self.ehealth = ehealth
        self.edmg = edmg

class Player:
    def __init__(self,name,phealth,pdmg):
        self.name = name
        self.phealth = phealth
        self.pdmg = pdmg

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
        Damage: {player.pdmg}""")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#heals
Potion_of_Minor_Healing = Heal(5,1,"Potion of Minor Healing +5")
Potion_of_Healing = Heal(10,2,"Potion of Healing +5")
Potion_of_Major_Healing = Heal(5,1,"Potion of Major Healing +5")
#goblin
wooden_spear = Wepon(3,"Wooden Spear +3")
stone_spear = Wepon(5,"Stone Spear +5")
stick = Wepon(1,"Stick +1")
#skeleton
bone = Wepon(2,"Bone +2")
simple_bow = Wepon(5,"Simple Bow +5")
advanced_bow = Wepon(8,"Advanced Bow +8")
#zombie
wooden_sword = Wepon(5,"Wooden Sword +5")
stone_sword = Wepon(7,"Stone Sword +7")
metal_sword = Wepon(15, "Metal sword +15")

inventory = [] #keep this empty so it auto puts stuff in
gobdrops = [Potion_of_Minor_Healing, Potion_of_Healing, wooden_spear, stone_spear, stick]
skeledrops = [Potion_of_Healing, simple_bow, advanced_bow, bone]
zombdrops = [Potion_of_Healing, Potion_of_Major_Healing, wooden_sword, stone_sword, metal_sword]


player_name = input("What is your name?: ")
clear
player = Player(player_name,50,5)

zombie = Enemy("Zombie",35,5)
skeleton = Enemy("Sekeleton",20,5)
goblin = Enemy("goblin",10,1)

mobs = [zombie,skeleton,goblin]

def showinventory():
    displayinventory = [x.name for x in inventory]
    print(displayinventory)

def apear(type):
    print(f"""{type.type} has apeared
        Health: {type.ehealth}
        Damage: {type.edmg}""")
    input()
    while type.ehealth > 0:
        type.ehealth = type.ehealth - player.pdmg
        print(f"You hit {type.type}. {type.type} health {type.ehealth}")
        time.sleep(1)
        if type.ehealth == 0:
            print(f"You defeated {type.type}")
            if type == goblin:
                dropnum = random.randint(0, 4)
                print(f"{type.type} has dropped {gobdrops[dropnum].name}")
                inventory.append(gobdrops[dropnum])
                goblin.ehealth = 10
                break
            elif type == skeleton:
                dropnum = random.randint(0, 4)
                print(f"{type.type} has dropped {skeledrops[dropnum].name}")
                inventory.append(skeledrops[dropnum])
                skeleton.ehealth = 20
                break
            elif type == zombie:
                dropnum = random.randint(0, 4)
                print(f"{type.type} has dropped {zombdrops[dropnum].name}")
                inventory.append(zombdrops[dropnum])
                zombie.ehealth = 35
                break
            else:
                print("something broke idk what but its not my fault cus I say so")
        player.phealth = player.phealth - type.edmg
        print(f"{type.type} hit you. Your Health is {player.phealth}")
        

def prompt(enemy):
    while True:
        choice = input("Would  you like to view your stats, inventory or continue?: ").strip().lower()
        if choice == "stats":
            stats()
        elif choice == "continue":
            clear()
            apear(enemy)
            break  
        elif choice == "inventory":
            clear()
            showinventory()
        elif choice == "debug":
            debug_choice = input("Health or Damage: ").strip().lower()
            if debug_choice == "health":
                player.phealth = int(input("What would you like to set health to?: "))
            elif debug_choice == "damage":
                player.pdmg = int(input("What would you like to set damage to?: "))
            else:
                print("pretty sure you spelt that wrong pall")
        else:
            print("Please select stats or continue")

prompt(goblin)
input()

while True:
    rng = random.randint(0,2)
    prompt(mobs[rng])
