from tictactoe_ys3874 import tictactoe_ys3874


#Tester for valid make_move
def test_make_move_valid():
    board = tictactoe_ys3874.initialize_board()
    test1 = tictactoe_ys3874.make_move(board, 0,0, 'X') # should be sucessful
    if test1:
        print(f'The move test1 is sucessful.')
    else:
        print('The move test1 is not sucessful.')

    test2 = tictactoe_ys3874.make_move(board, 1,1, 'O') # should be sucessful
    if test2:
        print('The move test2 is sucessful.')
    else:
        print('The move test2 is not sucessful.')


#Tester for check_winner
def test_game_winner():
    board = tictactoe_ys3874.initialize_board()
    tictactoe_ys3874.make_move(board, 1, 1, 'X') # should be sucessful
    tictactoe_ys3874.make_move(board, 0, 2, 'O') # should be sucessful
    tictactoe_ys3874.make_move(board, 0, 0, 'X') # should be sucessful
    tictactoe_ys3874.make_move(board, 2, 0, 'O') # should be sucessful
    tictactoe_ys3874.make_move(board, 2, 2, 'X') # should be sucessful
    print(board)
    winner = tictactoe_ys3874.check_winner(board) # check if X is the winner
    print(f'The winner is {winner}')
    board = tictactoe_ys3874.reset_game() # reset the game board
    print(board)