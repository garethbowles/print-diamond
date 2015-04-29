#!/usr/bin/env python

import string

__version__ = '0.0.1'

"""
Given values w and o, print a diamond of asterisks with width w,
indented by o spaces.

w must be an odd number.
"""


class MakeDiamond(object):

    def __init__(self, width, offset):
        self.width = width
        self.offset = offset
        self.diamond = []

    def construct(self):
        width = self.width
        offset = self.offset

        # Validate parameters
        if (width % 2 == 0 or width <= 0):
            print "Width must be a positive odd number."
            return
        if offset < 0:
            print "Offset must be zero or more."
            return

        # Make a triangle with width self.width
        for i in range(1, width + 1, 2):
            self.diamond.append("%s%s" % (" " * offset, ("*" * i).center(width)))
        # To finish the diamond, make an inverted triangle with width self.width-2
        for i in range(width - 2, 0, -2):
            self.diamond.append("%s%s" % (" " * offset, ("*" * i).center(width)))
        return self.diamond

    def printit(self):
        # Make sure diamond hasn't already been constructed
        if not self.diamond:
            self.construct()
        for i in range(len(self.diamond)):
            print self.diamond[i]

if __name__ == "__main__":
    diamond = MakeDiamond(0, -4)
    diamond.printit()
