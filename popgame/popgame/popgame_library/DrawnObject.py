from GameObject import GameObject
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:38:09 2015

@author: Research
"""


class DrawnObject(GameObject):
    texture = ""

    def __init__(self, position_x, position_y, texture):
        GameObject.__init__(self, position_x, position_y)
        self.texture = texture
