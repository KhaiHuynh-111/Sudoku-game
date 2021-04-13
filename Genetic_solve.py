from operator import itemgetter
import Sudoku_UI as sd
import random
import numpy as np
import matplotlib.pyplot as plt
import timeit
import pygame


def fitness_row(sudoku):
    score = 0
    num_dict = {}

    for row in sudoku:
        for num in row:
            if num == 0:
                continue
            if num not in num_dict.keys():
                num_dict[num] = 0
            num_dict[num] += 1
        score += len(num_dict)
        num_dict.clear()

    return score


def fitness_col(sudoku):
    score = 0
    num_dict = {}

    for i in range(9):
        for j in range(9):
            num = sudoku[j][i]
            if num == 0:
                continue
            if num not in num_dict.keys():
                num_dict[num] = 0
            num_dict[num] += 1
        score += len(num_dict)
        num_dict.clear()

    return score


def fitness_grid(sudoku):
    score = 0
    num_dict = {}

    for i in range(9):
        for j in range(9):
            co_x = (i//3) * 3 + j//3
            co_y = (i % 3) * 3 + j % 3
            num = sudoku[co_x][co_y]
            if num == 0:
                continue
            if num not in num_dict.keys():
                num_dict[num] = 0
            num_dict[num] += 1
        score += len(num_dict)
        num_dict.clear()

    return score


# 81 * 3 = 243 -> solved
def fitness(sudoku):
    return fitness_row(sudoku) + fitness_col(sudoku) + fitness_grid(sudoku)


# Generate initial population
def population_gen(sudoku, n):
    # Make n copies of the initial configuration
    population = [[0, [row[:] for row in sudoku]] for _ in range(n)]

    for sample in population:
        for i in range(9):
            # Random value list
            randomValList = [num for num in range(1, 10)]
            for j in range(9):
                if sample[1][i][j] != 0:
                    randomValList.remove(sample[1][i][j])
            for j in range(9):
                if sample[1][i][j] == 0:
                    randomVal = random.choice(randomValList)
                    sample[1][i][j] = randomVal
                    randomValList.remove(randomVal)
        sample[0] = fitness(sample[1])

    return population


# Crossover
def one_point_crossover(parent1, parent2):
    point = random.randint(1, 8)

    child = [parent1[row][:] for row in range(point)]
    for row in range(point, 9):
        child.append(parent2[row][:])

    return child


def two_point_crossover(parent1, parent2):
    pass


def uniform_crossover(parent1, parent2):
    pass


# Mutation
def random_resetting(child, init_configuration, score=None):
    pass


def swap_mutation(child, init_configuration, score=None):
    num_row = random.randint(1, 9)
    if 231 < score:
        num_row = 3
    if 239 < score:
        num_row = 2
    if 241 < score:
        num_row = 1
    for _ in range(num_row):
        row = random.randint(0, 8)
        column1 = random.randint(0, 8)
        column2 = random.randint(0, 8)
        if init_configuration[row][column1] == 0 and init_configuration[row][column2] == 0:
            child[row][column1], child[row][column2] = child[row][column2], child[row][column1]


# Plot fitness scores over generations
def plotFitness(generation, fitnessScore):
    plt.plot(generation, fitnessScore)
    plt.title("Optimum fitness score over each gereration")
    plt.xlabel("Generation")
    plt.ylabel("Best fitness score")
    plt.show()


NUM_GENS = 300  # number of generations
N = 100  # initial population count


def genetic(sudoku, crossover, mutate):
    # sudoku = [[7, 9, 2, 1, 5, 4, 3, 8, 6],
    #           [6, 4, 3, 8, 2, 7, 1, 5, 9],
    #           [8, 5, 1, 3, 9, 6, 7, 2, 4],
    #           [2, 6, 5, 9, 7, 3, 8, 4, 1],
    #           [4, 8, 9, 5, 6, 1, 2, 7, 3],
    #           [3, 1, 7, 4, 8, 2, 9, 6, 5],
    #           [1, 3, 6, 7, 4, 8, 5, 9, 2],
    #           [9, 7, 4, 2, 1, 5, 6, 3, 8],
    #           [5, 2, 8, 6, 3, 9, 4, 1, 7]]

    # sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 2, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #           [0, 0, 0, 0, 1, 0, 0, 8, 0],
    #           [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #           [0, 0, 0, 0, 9, 0, 6, 0, 0],
    #           [1, 0, 0, 0, 0, 0, 0, 5, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #           [0, 0, 5, 0, 0, 0, 3, 0, 0]]

    # sudoku = [
    #     [3, 0, 6, 5, 0, 8, 4, 0, 0],
    #     [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #     [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #     [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #     [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #     [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #     [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # sudoku = [[0] * 9] * 9

    ######################################################################################

    population = population_gen(sudoku, N)

    optimum = 0
    counter = 0
    gen_best_samples_scores = []
    while counter != NUM_GENS:
        # Sort population's samples in ascending order based on their score to take out top 10
        population.sort(key=lambda x: x[0], reverse=True)

        # Update optimum
        optimum = max(optimum, population[0][0])

        # Add it to a list for plotting purpose
        gen_best_samples_scores.append(optimum)

        # If GA found one solution, it would stop generate new generation
        if optimum == 243:
            break

        # Start new generation with 10 best samples of previous generation
        next_generation = []
        count = 10
        for sample in population:
            if count == 0:
                break
            next_generation.append(sample)
            count -= 1

        # Generate next generation population
        while len(next_generation) != N:
            parent1_idx, parent2_idx = 0, 0

            # Choose randomly among first 10 best samples in current generation
            parent1_idx = random.randint(0, 9)
            parent2_idx = random.randint(0, 9)

            # Performing crossover
            child = crossover(
                population[parent1_idx][1], population[parent2_idx][1])

            # Perform mutation
            mutate(child, sudoku, fitness(child))

            # Creating next generation
            next_generation.append([fitness(child), child])

        # Set the next generation to the current generation
        population = next_generation

        # Ready for next generation
        counter += 1

        # Print the temp best configuration
        sd.draw_board(population[0][1])
        pygame.display.update()
        pygame.time.delay(20)

    # Return
    # best configuration (possibly not solved),
    # its' score,
    # number of generations has pass,
    # best score of each generation
    return (population[0][1], optimum, counter, gen_best_samples_scores)


def genetic_solve(sudoku):
    # Start timer
    start = timeit.default_timer()

    # Execute GA
    optimumAttempt, optimumScore, gen, gen_best_samples_scores = genetic(
        sudoku=sudoku, crossover=one_point_crossover, mutate=swap_mutation)

    # End timer
    stop = timeit.default_timer()

    # Print the duration
    print('Time: ', stop - start)

    # Print messages based on what the best score is
    if optimumScore == 243:
        print(
            f"Solution found at generation {gen} with the configuration as shown:")
    else:
        print("Solution not found!")
        print(
            f"Best attempt score is {optimumScore} with the configuration as shown:")

    # Print the best configuration found by GA
    for row in optimumAttempt:
        print(row)

    # Do the plotting of each generation's best score
    if gen < NUM_GENS:
        genList = [gen for gen in range(gen + 1)]
    else:
        genList = [gen for gen in range(gen)]
    plotFitness(genList, gen_best_samples_scores)


