#!/usr/bin/python

#Class structure for class objects in the coursePlanner module

import itertools

class Node:
    def __init__(self, dept='', cc='',everyTerm=True,  tail=None, tail2=None):
        self.dept = dept
        self.cc = cc
        self.everyTerm = everyTerm
        self.tail = tail
        self.tail2 = tail2
    
    def str(self):
        name = str(self.dept) + ' ' +  str(self.cc)
        if self.everyTerm == False:
            name += '*'
        return name

    def countnodes(self):
        i=1
        if self.tail != None:
            cn = self
            while cn.tail:
                i+=1
                if cn.tail2 != None:
                    i+=1
                cn= cn.tail
        return i
