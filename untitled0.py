from random import randrange as rd

commands_Qexit = ['exit', 'quit', 'qexit']
commands_attack = ["attack", "strike", "swing"]
commands_rest = ['rest', 'wait', 'heal']
commands_control = ['heel+', 'heel-', 'rotationR', 'rotationL', 'speed+', 'speed-']

locations = []
positions = []

def attack(attacker, defender):
    if attacker.loc == defender.loc and defender.alive and attacker.alive == True:
        dmg = rd(attacker.attack, attacker.attack + 5)
        print(attacker.name, "deal", dmg, "points of damage to", defender.name, "!")
        defender.hp -= dmg
        if defender.hp <= 0:
            death(defender)
            defender.hp = 0
        return True

def death(defender):
    if defender == player:
        player.alive = False
    else:
        print(defender.name, "is dead")
        defender.alive = False

def control(command):
    if command == "heel+":
            player.alt_agl += 10
    elif command == 'heel-':
            player.alt_agl -= 10
    elif command == 'rotationR':
            player.rot += 10
    elif command == 'rotationL':
            player.rot -= 10
    elif command == 'speed+':
            player.speed -= 1
    elif command == 'speed-':
            player.speed -= 1
            
def move(Plane):
    if Plane.speed > 0:
        Plane.alt += Plane.alt_agl * Plane.speed
        Plane.pos += Plane.rot * Plane.speed + Plane.speed
        Plane.speed -= int(Plane.alt_agl / 10)
    else:
        Plane.speed = 0 # no negative number
        Plane.alt_agl -= 10
        Plane.speed -= int(Plane.alt_agl / 10)

class Plane:
    def __init__(self, name, Engine, alt, pos, rot, alt_agl, speed, alive = True):
        self.name = name
        self.alt = alt
        self.pos = pos
        self.rot = rot
        self.alt_agl = alt_agl
        self.speed = speed
        self.alive = True

class Engine:
    def __init__(self, name, power, fuel):
        self.name = name
        self.power = power
        self.fuel = fuel
        self.name = name

class Location:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        locations.append(self)
        positions.append(self.position)
        
Altitude = [0, 10, 20, 30, 40, 50]

arena = Location("Arena", 11)
far = Location("Far away place", 0)
forest = Location("Forest", 12)
town = Location("Town", 21)
dessert = Location("dessert", 22)

player = Plane("Player", Engine('Type1', 100, 100), 10, 11, 0, 0, 1)

def game():
    command = ""
    input("Welcome, pilot!")
    while player.alive:
        command = input("What do you do? ")
        if command in commands_control:
            control(command)
        elif command == 'look':
            print('Your speed is ' + str(player.speed))
            print('Your altitude is ' + str(player.alt))
            print('Your coordinates is ' + str(player.pos))
        elif command in commands_rest:
            move(player)
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
