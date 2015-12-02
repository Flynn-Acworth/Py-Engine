import DrawnObject
import Direction
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:23:36 2015

@author: Research
"""


class Creature(DrawnObject):
    health = 0
    direction = Direction.Facing.left
    jumping = False
    
    def __init__(self, position_x, position_y, texture_location, health):
        self.health = health