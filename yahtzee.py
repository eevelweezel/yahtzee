#!/usr/bin/python

import sys
import rules


def main(list, text, s_score=0):
    d6 = {1,2,3,4,5,6}
    roll = [int(x) for x in list]
    rule = text
    valid = {'1','2','3','4','5','6','3x','4x','full_house', 'small_straight', 'large_straight', 'chance', 'yahtzee'} 
    check_d = 0
    
    for i in roll: 
        if i in d6:
            check_d += 1
        else:
            check_d += 0
    if (check_d != 5) or (rule not in valid):
        print('Quit cheating and play nice.')       
    else:
        scr = rules.Rules(roll,rule,s_score)
        print(scr.score)
        return scr
    

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])