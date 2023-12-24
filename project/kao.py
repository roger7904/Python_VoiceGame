#! /usr/bin/env python3
# coding: utf-8
import change
import time
import sys, pygame
from xpinyin import Pinyin
from pygame.locals import *
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("kkk.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
x = Pinyin()

def print_board():
    for i in range(0, 4):
        for j in range(0, 4):
            print(map[3-i][j], end=" ")
            if j != 3:
                print("|", end=" ")
        print()

def check_done():
    for i in range(0, 4):
        if map[i][0] == map[i][1] == map[i][2] == map[i][3] != " " \
           or map[0][i] == map[1][i] == map[2][i] == map[3][i] != " ":
            print(turn, "WINNNNNNN!!!")
            return True
        
    if map[0][0] == map[1][1] == map[2][2] == map[3][3] != " " \
       or map[0][3] == map[1][2] == map[2][1] == map[3][0] != " ":
        print(turn, "WINNNNNNN!!!")
        return True

    if all(" " not in row for row in map):
        print("Drawwwwww")
        return True
    return False

# 主遊戲循環
turn = "A"
map = [[" "]*4 for _ in range(4)]
done = False

print()
print("  | * | * | * | * |")
print("  | * | * | * | * |")
print("  | * | * | * | * |")
print("  | * | * | * | * |")
print()

while not done:
    moved = False
    while not moved:
        print()
        print(turn, "'s turn")
        print()
        print_board()
        time.sleep(3)
        try:
            pos = change.sound()
            test = x.get_pinyin(pos, '').lower()
            print(test)
            if test == 'foguangshan':
                num = 13
            elif test == 'mengshidai':
                num = 14
            elif test == 'yidashijie':
                num = 15
            elif test == 'zhonglieci':
                num = 16
            elif test == 'hamaxing':
                num = 9
            elif test == 'xiziwan':
                num = 10
            elif test == 'lianchitan':
                num = 11
            elif test == 'dagangshan':
                num = 12
            elif test == 'dagoulingshiguan':
                num = 5
            elif test == 'aihe':
                num = 6
            elif test == 'gaoxionggang':
                num = 7
            elif test == 'qijin':
                num = 8
            elif test == 'ruifengyeshi':
                num = 1
            elif test == 'xinjuejiang':
                num = 2
            elif test == 'caoyadao':
                num = 3
            elif test == 'qishanlaojie':
                num = 4

            if 1 <= num <= 16:
                Y, X = divmod(num - 1, 4)
                if map[Y][X] == " ":
                    map[Y][X] = turn
                    moved = True
                    done = check_done()
                turn = "B" if turn == "A" else "A"
        except Exception as e:
            print("recording fail", e)
            turn = "B" if turn == "A" else "A"

