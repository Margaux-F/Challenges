# Python 3.8.6 64-bit
# UTF-8
# Margaux Faurie

# The pep8 has to be corrected...

from functools import reduce
from itertools import chain
import numpy as np
from datetime import datetime


def WhichTurn(nested_list, target_coin):
    startTime = datetime.now()
    print("\n\nProgram in process. Please Wait. \n\n")

    if target_coin > 64 or target_coin < 0:
        return "The guard must choose an existing square..."

    init_board = np.array(nested_list)  # Stock the initial board
    Board = list(chain.from_iterable(nested_list))  # Unnest the list
    final_board = Board  # Final Board without modifications

    Board[target_coin] = not Board[target_coin]  # Create an error on the guard's square
    NbFlipCoin = (reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(Board) if bit]))  # Find the square to flip

    if final_board[NbFlipCoin]:
        final_board[NbFlipCoin] = 0
    else:
        final_board[NbFlipCoin] = 1

    final_board = np.array(final_board).reshape(-1, 8)

    finishTime = datetime.now()
    timeDetla = finishTime - startTime

    print("Program has ended. \n")
    print("The process was completed in : " + str(
        timeDetla.total_seconds()) + "s.\n\n")

    print('\n\nFor a given board, with Head = 1, Tails = 0 :\n\n',
          init_board,
          '\n\nThe target coin is on the square n°',
          target_coin, bin(target_coin),
          '. \n\n The final board is : \n\n',
          final_board,
          '\n\nYou should turn the coin on the square :',
          NbFlipCoin, bin(NbFlipCoin))
    return "\n\n-- End of process--"


# Exemple to run :
nested_list = [[1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 1, 1],
               [1, 1, 1, 1, 0,
                0, 0, 1], [1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1, 0, 1]]
target_coin = int(input("The gard has to choose a square. Which number does it have ? n° = "))

print(WhichTurn(nested_list, target_coin))
