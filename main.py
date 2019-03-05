#!/usr/bin/python3
from Character import Character
import random
def isDead(entities):
    return [x.pv[0] <= 0 for x in entities]

players = [Character("Zheng Xiulan", 18, 14, 14, 10, 15, True),
        Character("Miao Lin", 22, 10, 16, 11, 18, True),
        Character("Tao Jiang", 26, 6, 18, 13, 13, True),
        Character("Liu Jingsheng", 20, 8, 14, 10, 14, True),
        Character("Jiang Xun", 23, 10, 16, 12, 17, True),
        Character("Guan Long", 25, 9, 17, 14, 12, True)]
enemies = [Character("Jueyuan", 15, 0, 14, 9, 20, False),
        Character("Jueyuan", 15, 0, 14, 9, 20, False),
        Character("Jueyuan", 15, 0, 14, 9, 20, False)]

entities = [x for x in players] + [x for x in enemies]

op = "0"
battleOver = False
while(not battleOver):
    print("Enemies:")
    for e in enemies:
        print(e)
    print("\nHeroes:")
    for p in players:
        print(p)

    # op = input("What is your choice? 9 - Quit")
    # if(all(isDead(enemies))):
    #     battleOver = True

    for e in entities:
        e.progress += e.ag[0] + 1
    for e in entities:
        if e.progress > 1000:
            e.act()
