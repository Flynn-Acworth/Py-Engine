import sys
import pygame
import game_manager
import numpy
from popgame_library.DrawnObject import DrawnObject

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:48:44 2015

@author: Research
"""
def init():
    pygame.init()
    game_manager.block_size = 32
    game_manager.window_height_in_blocks = 8 
    game_manager.window_width_in_blocks = 10
    game_manager.screen = pygame.display.set_mode((
        game_manager.window_width_in_blocks * game_manager.block_size,
        game_manager.window_height_in_blocks * game_manager.block_size))
    game_manager.clock = pygame.time.Clock()
    game_manager.frame_rate = 30
       
 
                        
        
                

def load():
    game_manager.tile["d"] = pygame.image.load("../asset/dirt.png")
    game_manager.tile["s"] = pygame.image.load("../asset/stone.png")
    game_manager.tile["c"] = pygame.image.load("../asset/coin.png")
    game_manager.tile["p"] = pygame.image.load("../asset/player.png")
    game_manager.tile["b"] = pygame.image.load("../asset/brown.png")
    game_manager.tile["z"] = pygame.image.load("../asset/sky.png")
    
    level_structure = (numpy.genfromtxt(open("../level/level_shahinday.txt","r"),
                                        delimiter=",", skiprows=0, dtype=str))

    row_count = 0
    for row in level_structure:
        col_count = 0
        block_row = []
        for column in row:        
            (block_row.append(DrawnObject(col_count * game_manager.block_size,
                     row_count * game_manager.block_size,
                             game_manager.tile[column])))
            col_count += 1
        row_count += 1
                             
        game_manager.level.append(block_row)

#def update_():
    # update logic here

def draw():
    game_manager.screen.fill([0, 200, 250])
    
    # draw level
    for row in game_manager.level:
        for column in row:
            (game_manager.screen.blit(column.texture, 
                                      (column.position_x, 
                                       column.position_y, 32, 32)))
            
    
    pygame.display.flip()

def main():
    init()
    load()
    
    exiting = False
    
    while(not exiting):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exiting = True
                if(pygame.key.get_pressed()[pygame.K_ESCAPE] != 0 ):
                    exiting = True        
            game_manager.clock.tick(game_manager.frame_rate)
            draw()
    sys.exit()            
