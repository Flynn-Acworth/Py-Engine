# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:42:42 2015

@author: Research
"""


class GameObject(object):
    position_x = 0
    position_y = 0
    solid = False

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
