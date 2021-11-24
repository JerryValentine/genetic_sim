import random
import numpy as np

class Organism():
    def __init__(self, position):
        self.genome = None
        self.brain = None
        self.pos = position
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def do_action(self, world, world_load, world_organisms):
        rand = random.randint(1,4)
        if(rand == 1):
            self.move_right(world, world_load, world_organisms)
        elif rand == 2:
            self.move_left(world_load, world_organisms)
        elif rand == 3:
            self.move_up(world, world_load, world_organisms)
        else:
            self.move_down(world_load, world_organisms)

    def move_right(self, world, world_load, world_organisms):
        if(self.pos[0]+1 <= world.size[0]-1):
            if(world_organisms[self.pos[0]+1, self.pos[1]] == 0):
                world_organisms[self.pos] = 0
                world_load[self.pos] = (255,255,255)
                self.pos = (self.pos[0] + 1, self.pos[1])
                world_organisms[self.pos] = self
                world_load[self.pos] = self.color

    def move_left(self, world_load, world_organisms):
        if(self.pos[0]-1 >= 0):
            if(world_organisms[self.pos[0]-1, self.pos[1]] == 0):
                world_organisms[self.pos] = 0
                world_load[self.pos] = (255,255,255)
                self.pos = (self.pos[0] - 1, self.pos[1])
                world_organisms[self.pos] = self
                world_load[self.pos] = self.color
    
    def move_up(self, world, world_load, world_organisms):
        if(self.pos[1]+1 <= world.size[1]-1):
            if(world_organisms[self.pos[0], self.pos[1]+1] == 0):
                world_organisms[self.pos] = 0
                world_load[self.pos] = (255,255,255)
                self.pos = (self.pos[0], self.pos[1] + 1)
                world_organisms[self.pos] = self
                world_load[self.pos] = self.color

    def move_down(self, world_load, world_organisms):
        if(self.pos[1]-1 >= 0):
            if(world_organisms[self.pos[0], self.pos[1]-1] == 0):
                world_organisms[self.pos] = 0
                world_load[self.pos] = (255,255,255)
                self.pos = (self.pos[0], self.pos[1] - 1)
                world_organisms[self.pos] = self
                world_load[self.pos] = self.color

