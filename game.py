import sys
from time import sleep
import location
import go
from colorama import init
from colorama import Fore, Back, Style
init()

class Weapon:
    def __init__(self, name):
        self.name = name

sword = Weapon("Sword")
knife = Weapon("Knife")
shield = Weapon("Shield")
goldensword = Weapon("Golden Sword")

equipment = [sword.name, knife.name]
assortment = [shield.name, goldensword.name]

class Place:
    def __init__(self, name, description, way):
        self.name = name
        self.description = description
        self.way = way

mnse = Place("\nMain Square\n", location.mainsq, go.g3)

def mainsquare():
    print(Fore.YELLOW + mnse.name)
    print(Fore.WHITE + mnse.description)
    print(Fore.CYAN + mnse.way + Style.RESET_ALL)
    # equipment["Apple"] = 10 - adding new items to dictionary (don't ask)

    def choice():
        where = input()
        if where == "n":
            townhall()
        if where == "s":
            industrialdistrict()
        if where == "e":
            residentdistrict()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice()
    choice()

rtdt = Place("\nResident District\n", location.resdist, go.g7)

def residentdistrict():
    print(Fore.YELLOW + rtdt.name)
    print(Fore.WHITE + rtdt.description)
    print(Fore.CYAN + rtdt.way + Style.RESET_ALL)

    def choice():
        where = input()
        if where == "w":
            mainsquare()
        if where == "e":
            market()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice()
    choice()

mt = Place("\nMarket\n", location.markt, go.g8)

def market():
    print(Fore.YELLOW + mt.name)
    print(Fore.WHITE + mt.description)
    print(Fore.CYAN + mt.way + Style.RESET_ALL)

    def choice():
        where = input()
        if where == "w":
            residentdistrict()
        if where == "n":
            thievesguild()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice()
    choice()

tsgd = Place("\nThieves Guild\n", location.thguild, go.g14)

def thievesguild():
    print(Fore.YELLOW + tsgd.name)
    print(Fore.WHITE + tsgd.description)
    print(Fore.CYAN + tsgd.way + Style.RESET_ALL)

    def choice():
        where = input()
        if where == "s":
            market()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice()
    choice()

ildt = Place("\nIndustrial District\n", location.indist, go.g1)

def industrialdistrict():
    print(Fore.YELLOW + ildt.name)
    print(Fore.WHITE + ildt.description)
    print(Fore.CYAN + ildt.way + Style.RESET_ALL)

    def choice():
        where = input()
        if where == "n":
            mainsquare()
        if where == "s":
            arena()
        if where == "w":
            uresidentdistrict()
        if where == "e":
            tunnel()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()
    
tl = Place("\nTunnel\n", location.tunl,go.g5)

def tunnel():
    print(Fore.YELLOW + tl.name)
    print(Fore.WHITE + tl.description)
    print(Fore.CYAN + tl.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "s":
            tunnel1()
        if where == "w":
            industrialdistrict()
        if where == "e":
            smithy()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()

tl1 = Place("\nTunnel\n", location.tunl1, go.g9)
    
def tunnel1():
    print(Fore.YELLOW + tl1.name)
    print(Fore.WHITE + tl1.description)
    print(Fore.CYAN + tl1.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "n":
            tunnel()
        if where == "e":
            dorm()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()
 
sy = Place("\nSmithy\n", location.smth, go.g15)
    
def smithy():
    print(Fore.YELLOW + sy.name)
    print(Fore.WHITE + sy.description)
    print(Fore.BLUE + "If you want to buy anything from smith, type: stock")
    print(Fore.CYAN + sy.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "w":
            tunnel()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        if where == "stock":
            print(Fore.YELLOW + "Smith stock:" + Style.RESET_ALL)
            for thing in assortment:
                print(thing)
            print(Fore.BLUE + "If you want to buy anything from smith, type: buy item name")
            print("e.g. buy shield" + Style.RESET_ALL)
            choice()
        if where == "buy shield":
            equipment.append(shield.name)
            assortment.remove(shield.name)
            print("You bought {}!".format(shield.name))
            choice()
        if where == "buy golden sword":
            equipment.append(goldensword.name)
            assortment.remove(goldensword.name)
            print("You bought {}!".format(goldensword.name))
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()
 
dm = Place("\nDorm\n", location.drm, go.g15)
    
def dorm():
    print(Fore.YELLOW + dm.name)
    print(Fore.WHITE + dm.description)
    print(Fore.CYAN + dm.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "w":
            tunnel1()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()
 
aa = Place("\nArena\n", location.arn, go.g8)
    
def arena():
    print(Fore.YELLOW + aa.name)
    print(Fore.WHITE + aa.description)
    print(Fore.BLUE + "If you want to fight someone, type: fight opponent's name.\nFor example: fight gladiator")
    print(Fore.RED + "Next to you is a gladiator. I think he is waiting for his opponent.")
    print(Fore.CYAN + aa.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "n":
            industrialdistrict()
        if where == "w":
            trainingground()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()
 
tggd = Place("\nTraining ground\n", location.traingd, go.g16)
    
def trainingground():
    print(Fore.YELLOW + tggd.name)
    print(Fore.WHITE + tggd.description)
    print(Fore.BLUE + "If you want to practice, type: practice weapon name.\nFor example: practice sword")
    print(Fore.RED + "Next to you is training dummy.")
    print(Fore.CYAN + tggd.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "e":
            arena()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()
    
udrtdt = Place("\nUnderground Resident District\n", location.uresdist, go.g9)
    
def uresidentdistrict():
    print(Fore.YELLOW + udrtdt.name)
    print(Fore.WHITE + udrtdt.description)
    print(Fore.BLUE + "You see a hole in the north.")
    print(Fore.CYAN + udrtdt.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "n":
            cave()
        if where == "e":
            industrialdistrict()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()
    
ce = Place("\nCave\n", location.cav, go.g6)
    
def cave():
    print(Fore.YELLOW + ce.name)
    print(Fore.WHITE + ce.description)
    print(Fore.CYAN + ce.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "n":
            cave1()
        if where == "s":
            uresidentdistrict()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()

ce1 = Place("\nCave\n", location.cav1, go.g14)
    
def cave1():
    print(Fore.YELLOW + ce1.name)
    print(Fore.WHITE + ce1.description)
    print(Fore.CYAN + ce1.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "s":
            cave()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()

tnhl = Place("\nTown Hall\n", location.twnhall, go.g12)
    
def townhall():
    print(Fore.YELLOW + tnhl.name)
    print(Fore.WHITE + tnhl.description)
    print(Fore.CYAN + tnhl.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "s":
            mainsquare()
        if where == "e":
            bank()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()

bk = Place("\nBank\n", location.bnk, go.g15)
    
def bank():
    print(Fore.YELLOW + bk.name)
    print(Fore.WHITE + bk.description)
    print(Fore.RED + "The banker looks at you friendly.")
    print(Fore.CYAN + bk.way + Style.RESET_ALL)
    
    def choice():
        where = input()
        if where == "w":
            townhall()
        if where == "eq":
            print(Fore.YELLOW + "Equipment:" + Style.RESET_ALL)
            for item in equipment:
                print(item)
            choice()
        else:
            print(Fore.RED + "You cannot go there or no such command exists." + Style.RESET_ALL)
            choice() 
    choice()

mainsquare()

