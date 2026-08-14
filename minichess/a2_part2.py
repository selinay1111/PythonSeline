"""CSC111 Winter 2026 Assignment 2: Trees, Chess, and Artificial Intelligence (Part 2)

Instructions (READ THIS FIRST!)
===============================

This Python module contains the start of functions and/or classes you'll define
for Part 2 of this assignment. Please note that in addition to this file, you will
also need to modify a2_game_tree.py by following the instructions on the assignment
handout. You should NOT make any changes to a2_minichess.py.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC111 Teaching Team
"""
import random
from typing import Optional
import a2_game_tree
import a2_minichess


def generate_complete_game_tree(root_move: str, game_state: a2_minichess.MinichessGame,
                                d: int) -> a2_game_tree.GameTree:
    """Generate a complete game tree of depth d for all valid moves from the current game_state.

    For the returned GameTree:
        - Its root move is root_move.
        - Its `is_white_move` attribute is set using the current game_state.
        - It contains all possible move sequences of length <= d from game_state.
          For each node in the tree, its subtrees appear in the same order that their
          moves were returned by game_state.get_valid_moves(),
        - If d == 0, a size-one GameTree is returned.

    Note that some paths down the tree may have length < d, because they result in an end state
    (win or draw) from game_state in fewer than d moves.

    Preconditions:
        - d >= 0
        - root_move == GAME_START_MOVE or root_move is a valid chess move
        - if root_move == GAME_START_MOVE, then game_state is in the initial game state

    Implementation hints:
        - This function must be implemented recursively.
        - In the recursive step, use the MinichessGame.copy_and_make_move method to create
          a copy of the game state with one new move made.
        - You'll need to review the public interface of the MinichessGame class to see what
          methods are available to help implement this function.

    WARNING: we recommend not calling this function with depth greater than 6, as this will
    likely take a very long time on your computer.
    """
    is_white = game_state.is_white_move()
    winner = game_state.get_winner()
    win_probability = 0.0
    if winner == "White":
        win_probability = 1.0

    # If d == 0, a size-one GameTree is returned
    if d == 0:
        return a2_game_tree.GameTree(root_move, is_white, win_probability)

    # IF there are no valid moves, also base case, we return game tree as is
    valid_moves = game_state.get_valid_moves()
    if not valid_moves:
        return a2_game_tree.GameTree(root_move, is_white, win_probability)

    # recursive step
    result = a2_game_tree.GameTree(root_move, is_white, win_probability)
    for move in valid_moves:
        next_state = game_state.copy_and_make_move(move)
        sub_tree = generate_complete_game_tree(move, next_state, d - 1)
        result.add_subtree(sub_tree)

    return result


class GreedyTreePlayer(a2_minichess.Player):
    """A Minichess player that plays greedily based on a given GameTree.

    See assignment handout for description of its strategy.
    """
    # Private Instance Attributes:
    #   - _game_tree:
    #       The GameTree that this player uses to make its moves. If None, then this
    #       player just makes random moves.
    _game_tree: Optional[a2_game_tree.GameTree]
    white_player: bool

    def __init__(self, game_tree: a2_game_tree.GameTree, white_player: bool = True) -> None:
        """Initialize this player.

        Preconditions:
            - game_tree represents a game tree at the initial state (root is '*')
        """
        self._game_tree = game_tree
        self.white_player = white_player

    def make_move(self, game: a2_minichess.MinichessGame, previous_move: Optional[str]) -> str:
        """Make a move given the current game.

        previous_move is the opponent player's most recent move, or None if no moves
        have been made.

        Preconditions:
            - There is at least one valid move for the given game
        """
        # Only update _game_tree when we have an actual previous move
        if previous_move is not None and self._game_tree is not None:
            self._game_tree = self._game_tree.find_subtree_by_move(previous_move)

        # If we have a game tree with subtrees, pick a subtree and use its .move
        if self._game_tree is not None and self._game_tree.get_subtrees():
            # get all the win probabilities as a list
            win_probability = [sub_tree.white_win_probability for sub_tree in self._game_tree.get_subtrees()]
            # if it is white move, pick the highest win probability path
            if self.white_player:
                win_rate = max(win_probability)
                index = win_probability.index(win_rate)
                subtree = self._game_tree.get_subtrees()[index]
                chosen_move = subtree.move
            # if it is black move, pick the lowest white win rate
            else:
                win_rate = min(win_probability)
                index = win_probability.index(win_rate)
                subtree = self._game_tree.get_subtrees()[index]
                chosen_move = subtree.move
            self._game_tree = subtree
            return chosen_move

        # Otherwise fallback to a random valid move and forget the tree
        chosen_move = random.choice(game.get_valid_moves())
        self._game_tree = None
        return chosen_move


def part2_runner(d: int, n: int, white_greedy: bool) -> None:
    """Create a complete game tree with the given depth, and run n games where
    one player is a GreedyTreePlayer and the other is a RandomPlayer.

    The GreedyTreePlayer uses the complete game tree with the given depth.
    If white_greedy is True, the White player is the GreedyTreePlayer and Black is a RandomPlayer.
    This is switched when white_greedy is False.

    Precondtions:
        - d >= 0
        - n >= 1

    Implementation notes:
        - Your implementation MUST correctly call a2_minichess.run_games. You may choose
          the values for the optional arguments passed to the function.
    """
    game_tree = generate_complete_game_tree(a2_game_tree.GAME_START_MOVE, a2_minichess.MinichessGame(), d)
    if white_greedy:
        a2_minichess.run_games(n, GreedyTreePlayer(game_tree), a2_minichess.RandomPlayer(), False)
    else:
        a2_minichess.run_games(n, a2_minichess.RandomPlayer(), GreedyTreePlayer(game_tree, False), False)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120,
    #     'disable': ['static_type_checker'],
    #     'extra-imports': ['random', 'a2_minichess', 'a2_game_tree']
    # })

    # Sample call to part2_runner (you can change this, just keep it in the main block!)
    part2_runner(5, 50, False)
