import subprocess
import numpy as np

def IA(grid):  
    """
    Determines the best move for the Connect Four AI given the current game board.

    Parameters:
    grid (numpy.ndarray): A 6x7 numpy array representing the current state of the game board.
                          Each element can be either 0 (empty), 1 (player 1), or 2 (player 2).

    Returns:
    int: The best move for the AI, represented as a column index (1-7) where the AI should drop its token.
    """
    if np.all(grid == grid[0]):
        IA.tracking = [0, 0, 0, 1, 0, 0, 0]
        IA.position = '4'
        return 4
    
    if np.count_nonzero(grid) == 1:
        IA.tracking = [0, 0, 0, 0, 0, 0, 0]
        IA.position = ''
       
    IA.position += str(next((index+1 for index, (x, y) in enumerate(zip(IA.tracking, np.count_nonzero(grid, axis=0))) if x != y), None)
)
    process = subprocess.Popen("./connect4AI", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    min = 100
    best_choice = None
    for coup in [index+1 for index, valeur in enumerate(grid[0]) if valeur == 0]:
        process.stdin.write(str.encode(f'{IA.position + str(coup)}\n'))
        process.stdin.flush()
        output = process.stdout.readline().decode().split()
        if len(output) != 4:
            return coup
        if int(output[1]) < min:
            min = int(output[1])
            best_choice = coup

    process.terminate()

    tracking = np.count_nonzero(grid, axis=0)
    tracking[best_choice-1] += 1
    IA.tracking = tracking
    IA.position += str(best_choice)

    return best_choice
