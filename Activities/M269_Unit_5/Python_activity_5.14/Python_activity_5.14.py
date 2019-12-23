#!/usr/bin/env python3

# Implementation of a genetic algorithm. The genomes are strings consisting
# of uppercase characters and spaces. Given an initial random population of
# genomes, the algorithm attempts to evolve a genome over a number of
# generations into the string given by the global variable TARGET.

# Authors: M269 Module Team
# Date: 19/12/13

import random
import string


# Global variables

TARGET = 'MONKEYS WITH TYPEWRITERS' # Target must comprise of only uppercase letters and spaces
POPULATION_SIZE = 20
MAX_GENERATIONS = 2000
RECOMBINATION_RATE = 4
GENOME_LENGTH = len(TARGET)
MUTATION_RATE = 5

def random_char():
    """
    Returns a random uppercase character or a space.
    """
    
    return random.choice(string.ascii_uppercase + ' ')



def initialPopulation():
    """
    Return an initial population of POPULATION_SIZE genomes. Each genome is a string
    of length GENOME_LENGTH and is comprised of random uppercase characters and spaces.
    """
    
    pop = []
    for i in range(POPULATION_SIZE):
        genome = ''
        for j in range(GENOME_LENGTH):
            genome = genome + random_char()
        pop.append(genome)
    return pop



def getFitness(aGenome):
    """
    For each gene (character) in the genome, function calculates the difference between
    it and the character in the same position in the TARGET string. These values
    are summed and then returned. The lower the fitness value, the fitter the genome.
    A fitness of 0 means the genome == TARGET.
    """
    
    fitness = 0
    for i in range(GENOME_LENGTH):
        fitness = fitness + abs(ord(aGenome[i]) - ord(TARGET[i]))
    return fitness



def getBest(currentPopulation):
    """
    Returns a tuple consisting of the fittest genome in the current population
    and its fitness value. The lower the fitness value, the fitter the genome.
    """
    
    bestFitness = 999999 # No genome is going to have a fitness this bad
    for aGenome in currentPopulation:
        fitness = getFitness(aGenome)
        if fitness < bestFitness:
            bestFitness = fitness
            bestTuple = (aGenome, bestFitness)
    return bestTuple



def mutate(aPopulation):
    """
    Iterates over every genome in aPopulation. For each genome there is
    a 1/MUTATION_RATE chance that one of its genes (randomly chosen) will
    be swapped for a random uppercase character or space. This ensures
    diversity in the population.
    """
    
    for i in range(POPULATION_SIZE):
        if random.randint(1, MUTATION_RATE) == MUTATION_RATE:
            # We need to change the selected genome from a string into
            # a list, as strings are immutable.
            selectedGenome = list(aPopulation[i])
            mutateBit = random.randint(0, GENOME_LENGTH - 1)
            selectedGenome[mutateBit] = random_char()
            # Using join() will change the list back into a string
            aPopulation[i] = ''.join(selectedGenome)



def crossover(matingPool):
    """
    Returns a new population created from the mating pool.
    
    The function iterates (POPULATION_SIZE / 2) times, each time it
    randomly selects two genomes from the mating pool.
    There is a 1/RECOMBINATION_RATE chance that each pair will swap
    genetic material before being added to the new population.
    """
    
    newPopulation = []
    for i in range(0, int(POPULATION_SIZE / 2)):
        # randomly pick two mates from the matingPool
        mate1 = matingPool[random.randint(0, POPULATION_SIZE - 1)]
        mate2 = matingPool[random.randint(0, POPULATION_SIZE - 1)]
        if random.randint(1, RECOMBINATION_RATE) == RECOMBINATION_RATE:
            # The two mates swap genetic material to create two new genomes
            # that are added to the new population
            crossoverPoint = random.randint(1, GENOME_LENGTH)
            newPopulation.append(mate2[:crossoverPoint] + mate1[crossoverPoint:])
            newPopulation.append(mate1[:crossoverPoint] + mate2[crossoverPoint:])
        else:
            # No genetic material swapped, the mates go unchanged into the new population
            newPopulation.append(mate1)
            newPopulation.append(mate2)
    return newPopulation



def constructMatingPool(currentPopulation):
    """
    Returns a mating pool.
    
    From the current population the function picks genomes for mating
    and adds them to the mating pool. The same genome may be added
    more than once. The mating pool will contain exactly the same
    number of genomes as the current population.
    """
    
    matingPool = []
    for i in range(POPULATION_SIZE):
        matingPool.append(selectGenome(currentPopulation))
    return matingPool



def generateNewPopulation(currentPopulation):
    """
    Returns a new population evolved from the current population.
    """
    
    matingPool = constructMatingPool(currentPopulation)
    newPopulation = crossover(matingPool)
    mutate(newPopulation)
    return newPopulation



def selectGenome(currentPopulation):
    """
    Randomly selects two genomes from the currentPopulation, then
    returns the one with the best (lowest) fitness.
    """

    genome1 = random.choice(currentPopulation)
    genome2 = random.choice(currentPopulation)
    if getFitness(genome1) < getFitness(genome2):
        return genome1
    else:
        return genome2



def GAFunction():
    """
    The main function. Generates an initial population of genomes which evolve
    over a number of generations. Function ends when a genome evolves into
    TARGET or when MAX_GENERATIONS have been created.
    """
    
    population = initialPopulation()
    print('Initial population')
    print(population)
    print()
    genomeTuple = ()
    numOfGenerations = 1
    evolved = False
    while numOfGenerations <= MAX_GENERATIONS and not evolved:
        genomeTuple = getBest(population)
        if genomeTuple[1] == 0:
            evolved = True
            print(genomeTuple[0], 'evolved in generation', numOfGenerations)
        else:
            population = generateNewPopulation(population)
            numOfGenerations = numOfGenerations + 1
    if not evolved:
        print('After', MAX_GENERATIONS, 'generations, no genome has evolved into', TARGET)
        print('The best that could be generated is', genomeTuple[0], 'with a fitness of', genomeTuple[1])
    print(population)




# Test the algorithm

GAFunction()
