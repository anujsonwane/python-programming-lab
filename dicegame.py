Name:-ANUJ SONWANE 
Division:-M Batch:-3
Roll no.:-59. Gr no.:-11810837

import random
from random import randint as rt
def game(dice,faces):
    result=0
    for roll in range(0,dice):
        result+=rt(1,faces)
    return result
dice=int(input())
faces=int(input())
result=game(dice,faces)
print(result)
