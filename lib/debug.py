#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ben = Player('Ben')
    tanner = Player('tanner')
    game1 = Game('solitaire')
    game2 = Game('monopoly')
    result3 = Result(ben, game2, 500)
    result2 = Result(ben, game2, 1500)
    result1 = Result(ben, game1, 550)

    

    ipdb.set_trace()
