from organism import Organism
from PIL import Image
from collections import Counter
import numpy as np
import glob, random

def is_cell_empty(position, world_organisms):
    return world_organisms[position[0], position[1]] == 0

def randomly_place_organisms(world, world_load, world_organisms, max_organisms, repoducers=None):
    if len(repoducers if repoducers is not None else []) == 0: # Inital Generation
        for _ in range(max_organisms):
            organism = Organism((random.randint(0,world.size[0]-1), random.randint(0,world.size[1]-1)), 5) # Create organism
            while(not is_cell_empty(organism.pos, world_organisms)): # Find empty spot for organism
                organism.pos = (random.randint(0,world.size[0]-1), random.randint(0,world.size[1]-1))
            world_organisms[organism.pos[0],organism.pos[1]] = organism # Place organism in 2d array and put his color on the image
            world_load[organism.pos[0],organism.pos[1]] = organism.color
    else: # New offspring
        repoducers_num = len(repoducers)
        for i in range(max_organisms):
            organism = Organism((random.randint(0,world.size[0]-1), random.randint(0,world.size[1]-1)), repoducers[i%repoducers_num], repoducers[(i+1)%repoducers_num]) # Create organism

            while(not is_cell_empty(organism.pos, world_organisms)): # Find empty spot for organism
                organism.pos = (random.randint(0,world.size[0]-1), random.randint(0,world.size[1]-1))

            world_organisms[organism.pos[0],organism.pos[1]] = organism # Place organism in 2d array and put his color on the image
            world_load[organism.pos[0],organism.pos[1]] = organism.color

def selection_event(world, world_environment, world_organisms): # TODO: Write code to cull part of the population based on selection criteria.
    repoducers = []
    unique_colors = []
    for x in range(world.size[0]):
        for y in range(world.size[1]):
            if(world_environment.getpixel((x,y))[0] == 255): # Check if pixel has red color
                world_organisms[x,y] = 0
    for organism in world_organisms.flatten():
        if(organism != 0):
            repoducers.append(organism)
            unique_colors.append(organism.color)
    # print(f"Unique Colors: {len(Counter(unique_colors).keys())}")
    return repoducers

def start_sim(world_size_x=128, world_size_y=128, steps=10, max_gen=50000, max_organisms=1000, environment_image="C:\\Users\\valenj11\\Documents\\Other\\genetic_sim\\environment-zones\\environment-zone-right.png", image_save_prefix="C:\\Users\\valenj11\\Documents\\Other\\genetic_sim\\images\\test\\", gif_save_prefix="C:\\Users\\valenj11\\Documents\\Other\\genetic_sim\\gifs\\"):
    world = Image.new('RGBA', (world_size_x, world_size_y), color = 'white')
    world_load = world.load()
    world_environment = Image.open(environment_image, 'r')
    world_organisms = np.zeros(shape=(world.size[0], world.size[1]), dtype=Organism)
    randomly_place_organisms(world, world_load, world_organisms, max_organisms)
    for generation in range(max_gen):
        for step in range(steps):
            for row in world_organisms:
                for organism in row:
                    if(organism != 0):
                        organism.do_action(world, world_load, world_organisms)
            if (generation % 50 == 0):
                world.save(f"{image_save_prefix}world_{str.zfill(str(step),3)}.png")
        if (generation % 50 == 0):
            print(f"Generation {generation}")
            img, *imgs = [Image.open(f) for f in sorted(glob.glob(f"{image_save_prefix}world_*.png"))]
            img.save(fp=f"{gif_save_prefix}generation-{generation}.gif", format='GIF', append_images=imgs,
                save_all=True, duration=200, loop=0)
        repoducers = selection_event(world, world_environment, world_organisms)
        del world, world_load, world_organisms
        world = Image.new('RGBA', (world_size_x, world_size_y), color = 'white')
        world_load = world.load()
        world_organisms = np.zeros(shape=(world.size[0], world.size[1]), dtype=Organism)
        randomly_place_organisms(world, world_load, world_organisms, max_organisms, repoducers)

if __name__ == '__main__':
    start_sim()