# ProSetSolver

A Projective Set solver designed for EXPERT mode.

[Projective Set Game](https://www.ocf.berkeley.edu/~dadams/proset/)

## Overview

ProSetSolver helps you find valid sets in the Projective Set card game. The console application prompts you to input the color data of seven cards and returns all possible valid sets.

## How to Use

### Input Format

The console will prompt you to input the color data for each of the seven cards.

For each card, input the active colors by listing the first letters of each active color:

### Example

![Example Card](https://user-images.githubusercontent.com/57467707/194764985-fbbee4e8-f94b-4b42-8411-1c0f68269115.png)

For this card, you would enter `ryp` for the active red, yellow, and purple spots.

### Output

The program returns the sequence of correct cards as numbered positions.

**Note:** The order in which you enter the cards doesn't matter, but it will affect how the program returns the sequence. For example, if the program returns `(1,3,5)`, this means:
- `1` = first card you entered
- `3` = third card you entered  
- `5` = fifth card you entered

## Dependencies

- **None** - only uses the built-in `itertools` library

