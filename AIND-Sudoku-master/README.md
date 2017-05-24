# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver


# Terminology
- The individual squares at the intersection of rows and columns will be called boxes. These boxes will have labels 'A1', 'A2', ..., 'I9'.
- The complete rows, columns, and 3x3 squares, will be called units. Thus, each unit is a set of 9 boxes, and there are 27 units in total.
- For a particular box (such as 'A1'), its peers will be all other boxes that belong to a common unit (namely, those that belong to the same row, column, or 3x3 square).


# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: When trying to solve Sudoku, we find that there are some local constraints to each square. These constraints help us narrow the possibilities for the answer, which can be very helpful. Furthermore, by iteratively applying these contraints to the units, we can extract the maximum information and get closer to our solution. 

In particular, the naked twins in Sudoky means that if 2 digits can only appear in 2 boxes within the same unit, then they must appear in those 2 boxes given the rules of sudoku requires all digits from 1 to 9 appear in the unit. This necessarily means 2 things:
- No other digit can appear in those 2 boxes.
- The 2 digits cannot appear in the other boxes of the unit.

We see that applying these local constraints helps reducing the search space.

In `naked_twins()`, we considered that we were solving a regular sudoku problem (not a diagonal sudoku) and looked for twins in each row, column and square. 


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: For the diagonal sudoku problem, we use the same constraint propagation method as for regular sudokus ("elimitate" and "only choice") but apply them to 2 extra units (the 2 diagonals), on top of rows, columns and squares. This reduces the search space more aggressively.

### Install

This project requires **Python 3**.

We recommend you install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software. 


##### Optional: Pygame

Pygame can be used to visualize the game as it progresses. 


### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

