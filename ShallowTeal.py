import math
import chess
from ChessBotBase import Bot

class Bot(Bot):
    def name(self):
        return "Bro didn't read the chromatism"

    def evaluate(self, board):
        stalemate_threshold = -75
        score = 0

        pawn_val, knight_val, bishop_val, rook_val, queen_val = 10, 30, 35, 55, 100

        my_material = (
            len(board.pieces(chess.PAWN, self.color)) * pawn_val +
            len(board.pieces(chess.KNIGHT, self.color)) * knight_val +
            len(board.pieces(chess.BISHOP, self.color)) * bishop_val +
            len(board.pieces(chess.ROOK, self.color)) * rook_val +
            len(board.pieces(chess.QUEEN, self.color)) * queen_val
        )
        
        opponent_material = (
            len(board.pieces(chess.PAWN, not self.color)) * pawn_val +
            len(board.pieces(chess.KNIGHT, not self.color)) * knight_val +
            len(board.pieces(chess.BISHOP, not self.color)) * bishop_val +
            len(board.pieces(chess.ROOK, not self.color)) * rook_val +
            len(board.pieces(chess.QUEEN, not self.color)) * queen_val
        )

        score += my_material
        score -= opponent_material

        if board.is_checkmate():
            return -math.inf if board.turn == self.color else math.inf
        elif board.is_fivefold_repetition or board.is_stalemate or board.is_seventyfive_moves:
            return math.inf if score < stalemate_threshold else -math.inf
        print(score)
        return score