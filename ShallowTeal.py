import math

from ChessBotBase import Bot

class Bot(Bot):
    def evaluate(self, board):
        if board.is_checkmate():
            return -math.inf if board.turn == self.color else math.inf
        
        score = 0

        pawn_val, knight_val, bishop_val, rook_val, queen_val = 10, 30, 35, 55, 100