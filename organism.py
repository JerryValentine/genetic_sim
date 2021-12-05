import random
from typing import Tuple
import numpy as np

class Organism():
    # (position: tuple, genome_size: int)
    # (position: tuple, parent_one: Organism, parent_two: Organism)
    def __init__(self, *args):
        if(len(args) == 0):
            self.genome = None
            self.brain = None
            self.pos = None
            self.direction = None
            self.color = None
        if(isinstance(args[1], int)):
            self.genome = []
            self.brain = None
            self.pos = args[0]
            self.direction = random.randint(0,3) # 0 - top 3 - left
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.generate_genome(args[1])
        elif(isinstance(args[1], Organism)):
            self.genome = []
            self.brain = None
            self.pos = args[0]
            self.direction = random.randint(0,3) # 0 - top 3 - left
            self.random_assortment(args[1], args[2])
            self.spot_mutation(1000000)
            self.color = self.calculate_color()

    def calculate_color(self):
        genome_string = ""
        for gene in self.genome:
            genome_string += gene
        genome_string_len = len(genome_string)
        genome_string_r = genome_string[:int(genome_string_len/3)]
        genome_string_g = genome_string[int(genome_string_len/3):int(genome_string_len*2/3)]
        genome_string_b = genome_string[int(genome_string_len*2/3):]
        r = int(genome_string_r, 16) % 255
        g = int(genome_string_g, 16) % 255
        b = int(genome_string_b, 16) % 255
        return (r, g, b)

    def generate_genome(self, max_genes):
        for _ in range(max_genes):
            self.genome.append(hex(random.randint(0,4294967295)).split('x')[1])

    def random_assortment(self, parent_one: object, parent_two: object):
        p1_selected = []
        p2_selected = []
        genome_size = len(parent_one.genome)
        if(genome_size % 2 == 1):
            p1_gene_index = random.randint(0,genome_size-1)
            p1_selected.append(p1_gene_index)
            self.genome.append(parent_one.genome[p1_gene_index])
        for _ in range(int(genome_size/2)):
            p1_gene_index = random.randint(0,genome_size-1)
            p2_gene_index = random.randint(0,genome_size-1)
            while p1_gene_index in p1_selected:
                p1_gene_index = random.randint(0,genome_size-1)
            while p2_gene_index in p2_selected:
                p2_gene_index = random.randint(0,genome_size-1)
            p1_selected.append(p1_gene_index)
            p2_selected.append(p2_gene_index)
            self.genome.append(parent_one.genome[p1_gene_index])
            self.genome.append(parent_two.genome[p2_gene_index])
        self.genome.sort()

    def spot_mutation(self, rate_of_mutation):
        for gene_index, gene in enumerate(self.genome):
            for char_index, _ in enumerate(gene):
                if(random.randint(0, rate_of_mutation) == 0):
                    self.genome[gene_index] = gene[:char_index] + hex(random.randint(0,15)).split('x')[1] + gene[char_index+1:]

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
                world_organisms[self.pos[0], self.pos[1]] = 0
                world_load[self.pos[0], self.pos[1]] = (255,255,255)
                self.pos = (self.pos[0] + 1, self.pos[1])
                self.direction = 1
                world_organisms[self.pos[0], self.pos[1]] = self
                world_load[self.pos[0], self.pos[1]] = self.color

    def move_left(self, world_load, world_organisms):
        if(self.pos[0]-1 >= 0):
            if(world_organisms[self.pos[0]-1, self.pos[1]] == 0):
                world_organisms[self.pos[0], self.pos[1]] = 0
                world_load[self.pos[0], self.pos[1]] = (255,255,255)
                self.pos = (self.pos[0] - 1, self.pos[1])
                self.direction = 3
                world_organisms[self.pos[0], self.pos[1]] = self
                world_load[self.pos[0], self.pos[1]] = self.color

    def move_up(self, world, world_load, world_organisms):
        if(self.pos[1]+1 <= world.size[1]-1):
            if(world_organisms[self.pos[0], self.pos[1]+1] == 0):
                world_organisms[self.pos[0], self.pos[1]] = 0
                world_load[self.pos[0], self.pos[1]] = (255,255,255)
                self.pos = (self.pos[0], self.pos[1] + 1)
                self.direction = 0
                world_organisms[self.pos[0], self.pos[1]] = self
                world_load[self.pos[0], self.pos[1]] = self.color

    def move_down(self, world_load, world_organisms):
        if(self.pos[1]-1 >= 0):
            if(world_organisms[self.pos[0], self.pos[1]-1] == 0):
                world_organisms[self.pos[0], self.pos[1]] = 0
                world_load[self.pos[0], self.pos[1]] = (255,255,255)
                self.pos = (self.pos[0], self.pos[1] - 1)
                self.direction = 2
                world_organisms[self.pos[0], self.pos[1]] = self
                world_load[self.pos[0], self.pos[1]] = self.color

class Node():
    def __init__(self):
        self.nextNode = None
        self.self
        self.weight = 0
        self.bias = 0
    def fire(self)

# Maybe a node object system would be better here
# Simple FFNN that has 1 hidden layer and uses tanh
class Brain():
    def __init__(self, *args):
        if(len(args) == 0):
            self.input_layer = None
            self.hidden_layer = None
            self.output_layer = None
        # input_layer_size, hidden_layer_size, output_layer_size, genome
        if(isinstance(args[3], list)):
            self.input_weights = np.zeros((args[0],args[1]+args[0]))
            self.input_bias = np.zeros((1,args[1]+args[0])) # Hidden layer + passthrough nodes
            self.hidden_weights = np.zeros((args[1]+args[0], args[2]))
            self.hidden_weights[0][args[1]+1:] = 1 #
            self.hidden_bias = np.zeros((1, args[2]))
            self.wire_brain(genome=args[3])

    def wire_brain(self, genome):
        input_layer_size = np.size(self.input_weights, 0)
        hidden_layer_size = np.size(self.input_weights, 1)
        output_layer_size = np.size(self.hidden_weights, 1)
        for gene in genome:
            gene_binary = str.zfill(bin(int(gene, 16)).split('b')[1], 32)
            weight = gene_binary[17:]/9000 if gene_binary[16] == 0 else gene_binary[17:]/(-9000)
            if(gene_binary[0] == 0):
                if(gene_binary[8] == 0): # Input -> Hidden
                    self.input_weights[int(gene_binary[1:7], 2) % input_layer_size, int(gene_binary[9:15], 2) % hidden_layer_size] = weight
                else: # Input -> Output
                    self.input_weights[int(gene_binary[1:7], 2) % input_layer_size, (int(gene_binary[9:15], 2) % output_layer_size) + hidden_layer_size-1] = weight
            else: # Hidden -> Output
                # if(gene_binary[8] == 0): # TODO: hidden -> hidden
                self.hidden_weights[int(gene_binary[1:7], 2) % hidden_layer_size, int(gene_binary[9:15], 2) % output_layer_size] = weight