from ChessBotBase import Bot
import chess
import math

class Bot(Bot):
    def name(self):
        return "Escanor, The Lion's Sin of Pride"
    def count_captures_on_moved_piece(self, board):
              move = board.peek()
              moved_to = move.to_square

              moved_to = move.to_square
              ene_color = not self.color
              Attackers = board.attackers(ene_color, moved_to)
              Attackcount = len(Attackers)                
              return Attackcount
    def count_defenses_on_moved_piece(self, board):
              move = board.peek()
              moved_to = move.to_square

              moved_to = move.to_square
              my_color = self.color
              defenders = board.attackers(my_color, moved_to)
              defendcount = len(defenders)                
              return defendcount
    def count_pieces_on_my_side(self, board):
              if self.color == chess.WHITE:
                  my_side = range(0, 32)   # ranks 1–4
              else:
                  my_side = range(32, 64)  # ranks 5–8
              enemy = not self.color
              count = 0
              for sq in my_side:
                  piece = board.piece_at(sq)
                  if piece and piece.color == enemy:
                      count += 1

              return count
    def count_my_pieces_on_ENE_side(self, board):
              if self.color == chess.WHITE:
                  ene_side = range(32, 64)   # ranks 1–4
              else:
                  ene_side = range(0, 32)  # ranks 5–8
              me = self.color
              count = 0
              for sq in ene_side:
                  piece = board.piece_at(sq)
                  if piece and piece.color == me:
                      count += 1

              return count
    
    def evaluate(self, board):

        # Checkmate / stalemate
        if board.is_checkmate():
            return -math.inf if board.turn == self.color else math.inf

        if board.is_stalemate():
            return 0

        # Determine mode based on turn count
        # Every 12 turns, Escanor switches personality
        cycle = (self.turn // 12) % 2
        pride_mode = (cycle == 0)

        score = 0
        # --- MATERIAL VALUES ---
        piece_values = {
            chess.PAWN: 50,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.ROOK: 500,
            chess.QUEEN: 1200,
        }
        move = chess.Move.from_uci("e2e4")

        piece = board.piece_at(move.from_square)
        material_self = 0
        material_opp = 0
        pride_multiplier = 1.2 * max(1.0, self.count_defenses_on_moved_piece(board) + self.count_captures_on_moved_piece(board))

        for piece_type in piece_values:
            material_self += len(board.pieces(piece_type, self.color)) * piece_values[piece_type]
            material_opp += len(board.pieces(piece_type, not self.color)) * piece_values[piece_type]

        material_score = material_self - material_opp
        if pride_mode:
            score += material_score 

            mobility_self = len(list(board.legal_moves))
            board.turn = not board.turn
            mobility_opp = len(list(board.legal_moves))
            board.turn = not board.turn
            score += (mobility_self - mobility_opp) * 20
            if piece in [chess.ROOK, chess.BISHOP, chess.QUEEN]:
                 score *= 1.5
            if board.is_capture(move):  
                score += material_score + (self.count_my_pieces_on_ENE_side(board) * 25) * pride_multiplier
            else:
                score += material_score + (self.count_my_pieces_on_ENE_side(board) * 25) 


        else:

            score += (mobility_self) * 25 + (material_score - (self.count_pieces_on_my_side(board) * 50)) - self.count_captures_on_moved_piece(board) *0.75
        return score