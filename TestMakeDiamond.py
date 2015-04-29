#!/usr/bin/env python


import unittest
from MakeDiamond import MakeDiamond

class TestMakeDiamond(unittest.TestCase):
    def test_width_3_offset_0(self):
        expected = [" * ", "***", " * "]
        diamond = MakeDiamond(3,0)
        actual = diamond.construct()
        print "Testing with width 3, offset 0 - should print a diamond"
        diamond.printit()
        print "" 
        self.assertTrue(actual == expected)

    def test_width_7_offset_4(self):
        expected = ["       *   ", "      ***  ", "     ***** ", "    *******",
                    "     ***** ", "      ***  ", "       *   "]
        diamond = MakeDiamond(7,4)
        actual = diamond.construct()
        print "Testing with width 7, offset 4 - should print a diamond"
        diamond.printit() 
        print ""
        self.assertTrue(actual == expected)

    def test_invalid_width(self):
        diamond = MakeDiamond(0,4)
        print "Testing with width 0 - should print an error"
        actual = diamond.construct()
        self.assertTrue(actual == None)


    def test_invalid_offset(self):
        print "Testing with width 7, offset -4 - should print an error"
        diamond = MakeDiamond(7,-4)
        actual = diamond.construct()
        self.assertTrue(actual == None)

if __name__ == '__main__':
    unittest.main()