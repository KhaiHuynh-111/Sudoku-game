# Sudoku-game

This is a classic game with some basic rules that almost everyone know it.

In classic sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contains all of the digits from 1 to 9.

With backtracking, solve this 9x9 board in coding is a basic challenge.
I'll try solving it in an unique way - Genetic Algorithm.

## Genetic Algorithm

A genetic algorithm is a search heuristic that is inspired by Charles Darwin’s theory of natural evolution.

The process of natural selection starts with the selection of fittest individuals from a population. They produce offspring which inherit the characteristics of the parents and will be added to the next generation. If parents have better fitness, their offspring will be better than parents and have a better chance at surviving.

Five phases are considered in a genetic algorithm.

1. Initial population
2. Fitness function
3. Selection
4. Crossover
5. Mutation


## Lets 'play'

First of all, you'll need to import Pygame module in order to display sudoku board and solve with
interaction.

```python

pip install pygame

```

Now let the game begin:

```python

python Sudoku_UI.py

```
