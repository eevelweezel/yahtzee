#!/usr/bin/python

import sys

class Rules:
    
    def __init__(self, list, text, s=0):
        self.rule = text
        self.roll = list
        self.score = 0
        self.score += self.rolldice()+int(s)
                
    def rolldice(self):
        if self.rule == '1' or self.rule == '2' or self.rule == '3' or self.rule == '4' or self.rule == '5' or self.rule == '6':
            self.n = int(self.rule)
            self.num()
        elif self.rule == '3x':
            self.n = int(3)
            self.nx()
        elif self.rule == '4x':
            self.n = int(4)
            self.nx()
        elif self.rule == 'full_house':
            self.full_house()
        elif self.rule == 'small_straight':
            self.n = int(4)
            self.straight()
        elif self.rule == 'large_straight':
            self.n = int(5)
            self.straight()        
        elif self.rule == 'chance':
            self.chance()
        else:
            self.yahtzee()        
        return self.score

        
    def num(self):
        self.score += self.n*self.roll.count(self.n)
        return self.score
            
    def nx(self):
        for r in self.roll:
            e = self.roll.count(r)
            if e >= self.n:
                self.score += r*self.n
                break
            else:
                self.score += 0
        return self.score        
                    
    def full_house(self):
        check = 0
        for r in self.roll:
            if self.roll.count(r) == 3 or self.roll.count(r) == 2:
                check += 0
            else:
                check += 1
        if check == 0:
            for r in self.roll:
                self.score += r
        else:
            self.score += 0
        return self.score
            
    def straight(self):
        check = 0
        for i in self.roll:
            if self.roll.count(i+1) == 1:
                check += 1
            else: 
                check += 0
        if check >= (self.n - 1):
            if self.n == 4:
                self.score += 15
            else: 
               self.score += 20
        else:
            self.score += 0
        return self.score
        
    def chance(self):
        for r in self.roll:
            self.score += r
        return self.score
        
    def yahtzee(self):
        for r in self.roll:
            if self.roll.count(r) == 5:
                self.score = 50
                break
            else: 
                self.score = 0
                break
        return self.score
        
