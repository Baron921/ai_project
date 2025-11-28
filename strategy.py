from typing import List, Optional
from logic import GameState, Move
import random

# This file as well as utils.py should be the only ones you have to edit!

class Strategy:
    """
    Base strategy class. Students should subclass this and implement select_move,
    as well as any helper methods they need.
    """
    def select_move(self, state: GameState, player: int, legal_moves: List[Move]) -> Optional[Move]:
        """
        Select a move for the given player in the given state.

        :param state: (GameState) The current game state.
        :param player: (int) The ID of the current player, 0 or 1.
        :param legal_moves: (List[Move]) A list of legal moves available to the given player.
        :return: (Optional[Move]) The selected move, or None to forfeit.
        """
        raise NotImplementedError

class RandomStrategy(Strategy):
    """
    Pick a random legal move.
    """
    
    def select_move(self, state: GameState, player: int, legal_moves: List[Move]):
        
        if legal_moves is not None:
            choice = random.choice(legal_moves)
            return choice
        return None
    

class GreedyMaxDegreeStrategy(Strategy):
    """
    Pick the move that gives your endpoint the highest number of free neighbors after the move.

    Simple and explainable baseline.
    """
    def select_move(self, state: GameState, player: int, legal_moves: List[Move]):
        moves = legal_moves
        print("Les moves: ",moves)
        node_degree_of_freedom = []
        for move in moves:
            #print("Un move: ", move)
            cpt = 0
            #print("Liste des visités: ", state.occupied)
            for visited in state.occupied:
                if move.to_node in state.G[visited]:
                    cpt += 1
            node_degree_of_freedom.append(cpt)     
        indices = [i for i, degree in enumerate(node_degree_of_freedom) if degree == min(node_degree_of_freedom)]
        
        chosen_move = legal_moves[random.choice(indices)]
        return chosen_move


# TODO: You should implement your own strategies here (Minimax, MCTS, etc.)

# Registry of available strategies.
# Add your new strategies here to run them from main.py.
STRATEGIES = {
    "random": RandomStrategy,
    "greedy": GreedyMaxDegreeStrategy,
}