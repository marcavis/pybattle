#!/usr/bin/python3
from Character import Character
players = [Character("Zheng Xiulan", 18, 14, 14, 10, 15),
        Character("Miao Lin", 22, 10, 16, 11, 18),
        Character("Tao Jiang", 26, 6, 18, 13, 13),
        Character("Liu Jingsheng", 20, 8, 14, 10, 14),
        Character("Jiang Xun", 23, 10, 16, 12, 17),
        Character("Guan Long", 25, 9, 17, 14, 12)]
for p in players:
    print(p)
