# read version from installed package
from importlib.metadata import version
__version__ = version("tictactoe_ys3874")
from .tictactoe_ys3874 import initialize_board, make_move, check_winner, reset_game
