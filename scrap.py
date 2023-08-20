# def get_poss_moves(self, state: CheckersGame) -> list[Move]:
    #     """
    #     Return the possible moves that self can make based on the passed game state.
    #     """
    #     poss_moves = []
    #
    #     # ------- Getting the upper right and the upper left cells -------
    #     up_right = (self.position[0] + 1, self.position[1] + 1)
    #     up_left = (self.position[0] - 1, self.position[1] + 1)
    #
    #     if _within_range(up_right, 8) and _within_range(up_left, 8):
    #         if state.board[up_right[0]][up_right[1]] == -1 and state.board[up_left[0]][up_left[1]] == -1:
    #             poss_moves.append(Move(self, up_right))
    #             poss_moves.append(Move(self, up_left))
    #         elif state.board[up_right[0]][up_right[1]] == -1:
    #             poss_moves.append(Move(self, up_right))
    #         elif state.board[up_left[0]][up_left[1]] == -1:
    #             poss_moves.append(Move(self, up_left))
    #
    #     # ------- Getting the potential right capturing moves -------
    #     curr_jump_right = (self.position[0] + 2, self.position[1] + 2)
    #     curr_just_right = (self.position[0] + 1, self.position[1] + 1)
    #
    #     while _within_range(curr_jump_right, 8) and _within_range(curr_just_right, 8) and \
    #             state.empty_at(curr_jump_right) and not state.empty_at(curr_just_right) and \
    #             state.board[curr_just_right[0]][curr_just_right[1]] >= 12:
    #         curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] + 2)
    #         curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] + 2)
    #
    #     # while (curr_jump_right[0] < 8 and curr_jump_right[1] < 8) and \
    #     #         (curr_just_right[0] < 8 and curr_just_right[1] < 8) and \
    #     #         (state.board[curr_just_right[0]][curr_just_right[1]] != -1) and \
    #     #         (state.board[curr_jump_right[0]][curr_jump_right[1]] == -1):
    #     #     print(111, curr_jump_right, curr_just_right)
    #     #     curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] + 2)
    #     #     curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] + 2)
    #     #     print(222, curr_jump_right, curr_just_right)
    #     #     print('----------------')
    #
    #     if curr_jump_right != (self.position[0] + 2, self.position[1] + 2):  # i.e. what it is initialized to
    #         poss_jump = (curr_jump_right[0] - 2, curr_jump_right[1] - 2)
    #         move = Move(self, poss_jump)
    #         poss_moves.append(move)
    #
    #     return poss_moves







# class SimpleAggressor(Player):
#     """
#     A Checkers player that makes the most aggressive move that they can play next
#     """
#     def __init__(self, color):
#         self.color = color
#
#     def play(self, state: CheckersGame) -> Move:
#         """
#         Return a move given the current state of the game.
#         """
#         if self.color == 'B':
#             if state.get_winner() is not None and not state.get_turn():
#                 poss_moves = state.get_black_moves()
#                 difflist = []
#                 for move in poss_moves:
#                     rednumber = state.red_survivors
#                     new_state = state.copy_and_record_move(move)
#                     diff = rednumber - new_state.red_survivors
#                     difflist.append(diff)
#                 diffmax = max(difflist)
#                 aggmoves = [poss_moves[i] for i in range(0, len(poss_moves)) if difflist[i] == diffmax]
#                 move = random.choice(aggmoves)
#         else:
#             if state.get_winner() is not None and state.get_turn():
#                 poss_moves = state.get_red_moves()
#                 difflist = []
#                 for move in poss_moves:
#                     blknumber = state.black_survivors
#                     new_state = state.copy_and_record_move(move)
#                     diff = blknumber - new_state.black_survivors
#                     difflist.append(diff)
#                 diffmax = max(difflist)
#                 aggmoves = [poss_moves[i] for i in range(0, len(poss_moves)) if difflist[i] == diffmax]
#                 move = random.choice(aggmoves)
#         return move


# CUSTOMIZABLE CASE
        # elif choice_of_stats == 6:
        #     # ---------- INSTRUCTIONS ----------
        #     # 1. Choose depth d (depths greater than 4 will take a long time to run, due to the branching factor)
        #     # 2. Initialize a 'black_player'. Make sure to initialize correctly as per the related documentation.
        #
        #     choice_of_depth = input("Enter the depth (note that depth > 4 takes a long time to run): ")
        #     choice_of_black_player = input("Choose black player: \n A: PrunefulMinimaxer, B: Randomizer, " + \
        #                                    "\n (type the capital letter corresponding to your choice)")
        #     choice_of_red_player = input("Choose red player: \n"
        #                                  "A: PrunefulMinimaxer, B: Randomizer \n (type"
        #                                  "the capital letter corresponding to your choice)")
        #
        #     letter_to_player = {'A': PrunefulMinimaxer, 'B': Randomizer}
        #
        #     d = int(choice_of_depth)
        #     black_player = letter_to_player[choice_of_black_player]
        #     red_player = letter_to_player[choice_of_red_player]
        #
        #     run_games_plot(black_player(depth), PrunefulMinimaxer(depth), 25, True)
