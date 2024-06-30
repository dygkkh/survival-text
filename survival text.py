import os
from random import *
from time import *

x = 0
y = 0
ccc = False
basex : int
basey : int
materials = 0

while True:
    print("pos:")
    print(f"({x}; {y})\n")
    print("materials:")
    print(materials)
    print("options: ")
    print("1: move")
    print("2: create base")
    print("3: save data")
    option = input("select option: ")
    if option == "1":
        movto = input("n,s,e,w: ")
        if movto == "n":
            y += 1
        elif movto == "s":
            y -= 1
        elif movto == "e":
            x += 1
        elif movto == "w":
            x -= 1
        guannnudf = randint(0,10)
        if guannnudf == 5:
            print("you founded a forest, +10 of material")
            materials += 10
    elif option == "2":
        if materials >= 30:
            basex = x
            basey = y
            x += 1
            materials -= 30
            ccc = True
        else:
            try:
                print("you don´t have sufficient materials")
            except NameError:
                print("you don´t have sufficient materials")
                
    if ccc == True:
        if x == basex and y == basey:
            print("options:")
            print("sleep")
            print("continue")
            ffff =  input("what do you want in your base?: ")
            if ffff == "sleep":
                print("sleeping 8 hours (8 secons in real life)")
                counter = 0
                print(counter)
                sleep(1)
                counter += 1
                print(counter)
                sleep(1)
                counter += 1
                print(counter) 
                sleep(1)
                counter += 1
                print(counter)
                sleep(1)
                counter += 1
                print(counter)
                sleep(1)
                counter += 1
                print(counter)
                sleep(1)
                counter += 1
                print(counter)
                sleep(1)
                counter += 1
                print(counter)
                sleep(1)
                counter += 1
                print(counter)
                sleep(1)
                counter += 1
            if ffff == "continue":
                continue
    
                  
                
    os.system("cls")
