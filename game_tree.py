# """CSC111 Final Project: Checkers & Decision Trees
#
# Module Description
# ==================
# This module contains our GameTree class.
#
# Classes included: Stone, Move, CheckersGame
#
# Copyright and Usage Information
# ===============================
# This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
# """
#
# from __future__ import annotations
# from structures import *
#
#
# class GameTree:
#     """
#     A decision tree for a Checkers Game.
#     """
#
#     move: Move | str
#     score: Optional[float]
#     game: Optional[CheckersGame]
#     _subtrees: list[GameTree]
#
#     def __init__(self, move: Move | str, score=None):
#         """
#         Initializes a GameTree with only one node.
#         The GameTree is initialized without subtrees.
#         """
#         self.move = move
#         self.score = score
#         self._subtrees = []
#
#     def add_subtree(self, gt: GameTree):
#         """
#         Add a new subtree (by adding it to the self._subtrees set)
#         """
#         self._subtrees += [gt]
#
#     def show_root(self):
#         if isinstance(self.move, str):
#             return f'(L, {round(self.score, 3)})'
#         else:
#             return f'({self.move.stone_to_move.ID}, {self.move.new_position}), {round(self.score, 3)}'
#
#     def getaggroscore(self, depth: int, color: str) -> float:
#         """
#         Assign aggro score for a game tree up to a certain depth, depending on if player is Red or Black
#         """
#         game = self.game
#         subtrees = self.get_subtrees()
#         if color == 'B':
#             if self.move is None:
#                 return 0
#             elif depth == 0 or game.get_winner() is not None:
#                 return 12 - len(game.red_survivors)
#             else:
#                 return sum([subtrees[i].getaggroscore(depth - 1, color)
#                             for i in range(0, len(subtrees))]) / len(subtrees)
#         else:
#             if self.move is None:
#                 return 0
#             elif depth == 0 or game.get_winner() is not None:
#                 return 12 - len(game.black_survivors)
#             else:
#                 return sum([subtrees[i].getaggroscore(depth - 1, color)
#                             for i in range(0, len(subtrees))]) / len(subtrees)
#
#     def increasedepth(self, depth: int) -> GameTree:
#         """
#         Increase depth of gamteree (self) by 1; mutates self
#         """
#         game = self.game
#         if depth == 0:
#             return game.gametreewithdepth(1)
#         else:
#             subtrees = self.get_subtrees()
#             self._subtrees = [subtree.increasedepth(depth - 1) for subtree in subtrees]
#         return self
#
#     def get_subtrees(self) -> list[GameTree]:
#         """
#         Return self._subtrees.
#         """
#         return self._subtrees
#
#     def __str__(self):
#         return self._str_indented(0)
#
#     def _str_indented(self, i: int):
#         string = '       ' * i + self.show_root() + '\n'
#         for subtree in self._subtrees:
#             string += subtree._str_indented(i + 1)
#         return string
