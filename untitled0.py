from random import randrange as rd

commands_Qexit = ['exit', 'quit', 'qexit']
commands_attack = ["attack", "strike", "swing"]
commands_spell = ["cast", 'spell', 'magic']
commands_rest = ['rest', 'stand', 'heal']
commands_move = ['south', 'north', 'east', 'west']

locations = []
positions = []

def attack(attacker, defender):
    if attacker.loc == defender.loc and defender.alive and attacker.alive == True:
        print(attacker.name, "deal", rd(attacker.attack, attacker.attack + 5), "points of damage to", defender.name, "!")
        defender.hp -= attacker.attack
        if defender.hp <= 0:
            death(defender)
        return True
    else:
        return False



def summon():
    monster.loc = player.loc
    monster.alive = True
    monster.hp += 10

def death(defender):
    if defender == player:
        player.alive = False
    else:
        print(defender.name, "is dead")
        defender.alive = False

def move(command):
    if command == "south":
        if player.pos + 10 not in positions:
            print('You are trying to cross the edge of the world')
        else:
            player.pos += 10
    elif command == 'north':
        if player.pos - 10 not in positions:
            print('You are trying to cross the edge of the world')
        else:
            player.pos -= 10
    elif command == 'east':
        if player.pos + 1 not in positions:
            print('You are trying to cross the edge of the world')
        else:
            player.pos += 1
    elif command == 'west':
        if player.pos - 1 not in positions:
            print('You are trying to cross the edge of the world')
        else:
            player.pos -= 1
    for i in locations:
        if i.position == player.pos:
            player.loc = i
            print('You are in the', player.loc.name)

class Character:
    def __init__(self, name, alive, loc, pos, hp, attack):
        self.hp = hp
        self.alive = alive
        self.loc = loc
        self.name = name
        self.attack = attack
        self.pos = pos

class Location:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        locations.append(self)
        positions.append(self.position)

arena = Location("Arena", 11)
far = Location("Far away place", 0)
forest = Location("Forest", 12)
town = Location("Town", 21)
dessert = Location("dessert", 22)

player = Character("Player", True, arena, 11, 10, 5)
monster = Character("Monster", True, arena, 11, 10, 5)

def game():
    command = ""
    input("Welcome, traveller!")
    while player.alive == True:
        command = input("What do you do? ")
        if command in commands_attack:
            if attack(player, monster) == True:
                attack(monster, player)
            else:
                print("No one to attack")
        elif command in commands_spell:
            print("You teleported the monster!")
            monster.loc = far
        elif command in commands_rest:
            if attack(monster, player) == False:
                print("Get some rest")
                player.hp += 2
            else:
                print('No time to rest')
        elif command in commands_move:
            move(command)
        elif command == "look":
            print("Your health is", player.hp, "and Monster health is", monster.hp)
            print("You are in", player.loc.name)
        elif command == "summon":
            summon()
            print("You have summoned a monster")
        elif command in commands_Qexit:
            print("Your journey ends here.")
            return False
        else:
            print("Try another command")
    else:
        print("You have perished.")
        print("Your journey ends here.")
        return False

game()
