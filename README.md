## Introduction

We have used Monte Carlo Tree Search (MCTS) as part of our approach to playing Tetris. By simulating multiple potential future game states, MCTS helps guide decision-making by selecting actions that maximize long-term performance. Through random sampling of possible moves and evaluating the outcomes, MCTS enables the agent to make strategic choices for piece placement, balancing immediate moves with longer-term goals such as clearing lines and maintaining manageable stack height.

## Demo
![Tetris Game Screenshot](https://github.com/nuno-faria/tetris-ai/raw/master/demo.gif)


# Monte-Carlo Tree Search:

It is a search algorithm that works by building a tree of possible moves and their outcomes. At each node in the tree, the algorithm chooses the next move to explore by using a combination of exploration and exploitation strategies. The algorithm then simulates a game from that point, choosing moves randomly until the game ends. The outcome of the game is then used to update the statistics at the corresponding node in the tree. This process is repeated many times, and the algorithm selects the move with the highest expected outcome based on the statistics gathered during the simulations.

![Tetris Game Screenshot](https://media.geeksforgeeks.org/wp-content/uploads/mcts_own.png)

## MCTS In Tetris

### 1. State Representation:
We represented tetris game as a 10 * 20 grid. A block is represented as a 4 *4 grid. We have taken into consideration 6 blocks I, T, L, J, Z, S. All the possible rotations of the blocks are provided. As the blocks collide with the ground, we consider the positions in the grid to be filled. 

### 2. Score Evaluation : 
Score: 1 + (lines_cleared ** 2) * Board_width(i.e 10)

If the maximum height of the block crosses the max height(i.e 20 rows)of the grid, the game is considered to be over.We aim to maximize points.

## Heuristics
### 1. Holes Minimization
A hole is defined as follows:
.An empty square under the topmost filled square in a column.

Each hole is difficult to fill, since it would require clearing all the lines above it, they should be avoided whenever possible. We try to minimize these holes along a row.

### 2.  Minimization of sum of heights across every column
The second heuristic used the sum of  the height of each column. Keeping the aggregate height of the field is desirable, as once the 20 height limit is broken the game ends. So we try to minimize the aggregate height of all the columns so we can achieve a maximum number of points.

