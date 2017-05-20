from util import *
from function import *


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    # values is a dictinary
    for v in values:        
        # only looks at the box on the board where value is determined already
        if len(values[v]) == 1:
            for box in peers[v]:
                values[box] = values[box].replace(values[v], '')
        
    return values
        
        
        
        
    
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
values = grid_values(grid)
ans = eliminate(values)