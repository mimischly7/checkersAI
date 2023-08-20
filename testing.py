import copy

from structures import CheckersGame, Move, Stone
from simulation import run_game
from players import PrunelessMinimaxer, Randomizer
from minimax import show_board

# prun = PrunelessMinimaxer('B', 2)
# rando = Randomizer('R')
# game, winner = run_game(prun, rando)
#
# moves = game.get_moves()

def game_state_generator(lst_moves: list[Move], game: CheckersGame) -> list[CheckersGame]:
    lst = [game]
    for move in lst_moves:
        new_game = game.copy_and_record_move(move)
        lst.append(new_game)
        game = new_game

    return lst


# if __name__ == '__main__':
#
#     prun = PrunelessMinimaxer(2)
#     rando = Randomizer()
#     game, winner = run_game(prun, rando)
#
#     moves = copy.deepcopy(game.get_moves())
#     game1 = CheckersGame()
#
#     game_states = game_state_generator(moves, game1)

# TODO: check record_move (check if the stones dict and board are updating, history updating correctly),
#  _copy working correctly?, we believe that given a list of correct game_states we can run it w/out error is this wrong?


#
# mx,my = evnt.pos
#
# if 45 < mx < 395:
#     if   250 < my < 350
#
#     if  380 < my < 480
#
#     if  510 < my < 610
#
#     if 640  < my < 740
#
# if 400 < mx < 750:
#
#     if 250 < my < 350
#
#     if 380 < my < 480
#
#     if 510 < my < 610
#
#     if 640 < my < 740
