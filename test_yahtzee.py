#!/usr/bin/python

import unittest
import yahtzee
import rules

class Test_the_YahtzeeBot(unittest.TestCase):

    def test_yahtzeeBot(self):
        """test that scoring an invalid roll fails"""
        fail = [7,8,9,0,7] 
        c = yahtzee.main(fail,'yahtzee',0)
        self.assertFalse(c)
    
    def test_scores(self):    
        """test that class methods score properly"""
        d6 = [1,1,1,3,4]
        b = yahtzee.main(d6,'full_house',3)
        c = yahtzee.main(d6,'yahtzee',3)
        d = yahtzee.main(d6,'1',3)
        e = yahtzee.main(d6,'small_straight',3)
        f = yahtzee.main(d6,'chance',3)
        g = yahtzee.main(d6,'3x',3)
        self.assertEqual(b.score,3)
        self.assertEqual(c.score,3)
        self.assertEqual(d.score,6)
        self.assertEqual(e.score,3)
        self.assertEqual(f.score,13)
        self.assertEqual(g.score,6)        


if __name__ == '__main__':
    unittest.main()