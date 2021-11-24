from organism import Organism
from PIL import Image
import numpy as np
import glob, random

def is_cell_empty(position, world_organisms):
    return world_organisms[position] == 0

def randomly_place_organisms(world, world_load, world_organisms, max_organisms):
    for _ in range(max_organisms):
        organism = Organism(position=(random.randint(0,world.size[0]-1), random.randint(0,world.size[1]-1))) # Create organism

        while(not is_cell_empty(organism.pos, world_organisms)): # Find empty spot for organism
            organism.pos = (random.randint(0,world.size[0]-1), random.randint(0,world.size[1]-1))
        
        world_organisms[organism.pos[0],organism.pos[1]] = organism # Place organism in 2d array and put his color on the image
        world_load[organism.pos[0],organism.pos[1]] = organism.color
    


def start_sim(world_size_x=128, world_size_y=128, steps=300, max_organisms=1000, image_save_prefix=".\\images\\test\\", gif_save_prefix=".\\gifs\\test\\"):
    world = Image.new('RGBA', (world_size_x, world_size_y), color = 'white')
    world_load = world.load()
    world_organisms = np.zeros(shape=(world.size[0], world.size[1]), dtype=Organism)
    randomly_place_organisms(world, world_load, world_organisms, max_organisms)
    for step in range(steps):
        for row in world_organisms:
            for organism in row:
                if(organism != 0):
                    organism.do_action(world, world_load, world_organisms)
        world.save(f"{image_save_prefix}world_{str.zfill(str(step),3)}.png")
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(f"{image_save_prefix}world_*.png"))]
    img.save(fp=f"{gif_save_prefix}sim_gif.gif", format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)


if __name__ == '__main__':
    start_sim()