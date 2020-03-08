#! /usr/bin/env python
# -*- coding:utf-8 -*-
import change
import time
import sys,pygame
from xpinyin import Pinyin
from pygame.locals import *
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("kkk.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
x=Pinyin()

def print_board():
    for i in range(0,4):
        for j in range(0,4):
            print map[3-i][j],
            if j != 3:
                print "|",
        print ""

def check_done():
    for i in range(0,4):
        if map[i][0] == map[i][1] == map[i][2] ==map[i][3] != " " \
        or map[0][i] == map[1][i] == map[2][i] ==map[3][i] != " ":
            print turn, "WINNNNNNN!!!"
            return True
        
    if map[0][0] == map[1][1] == map[2][2] ==map[3][3] != " " \
    or map[0][3] == map[1][2] == map[2][1] ==map[3][0] != " ":
        print turn, "WINNNNNNN!!!"
        return True
    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Drawwwwww"
        return True
    return False


turn = "A"
map = [[" "," "," "," "],
       [" "," "," "," "],
       [" "," "," "," "],
       [" "," "," "," "],
       [" "," "," "," "]]
done = False

print
print "  | * | * | * | * |"
print "  | * | * | * | * |"
print "  | * | * | * | * |"
print "  | * | * | * | * |"
print


while done != True:

    moved = False
    while moved != True:
        print 
        print turn, "'s turn"
        print
        print_board()
        time.sleep(3)
        try:
            pos=change.sound()
            test=x.get_pinyin(pos, u'').lower()
            print (test)
            if test == 'foguangshan':
                num = 13
            elif test == 'mengshidai' :
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
            
            if num <=16 and num >=1:
                Y = num/4
                X = num%4
                if X != 0:
                    X -=1
                else:
                     X = 3
                     Y -=1
                    
                if map[Y][X] == " ":
                    map[Y][X] = turn
                    moved = True
                    done = check_done()
                if turn == "A":
                    turn = "B"
                else:
                    turn = "A"

        except:
            if turn == "A":
                turn = "B"
            else:
                turn = "A"
            print "recording fail"