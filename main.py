import chess
import torch
import numpy as np

class State(object):
    def __init__(self, board = None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board

    def serialize(self):
        initial_state = np.zeros(64, dtype=np.int8)

        pieces_to_int = {
            chess.PAWN: 1,
            chess.KNIGHT: 2,
            chess.BISHOP: 3,
            chess.ROOK: 4,
            chess.QUEEN: 5,
            chess.KING: 6
        }

        for i in range(64):
            piece = self.board.piece_at(i)
            if piece:
                value = pieces_to_int.get(piece.piece_type, 0)
                if piece.color == chess.BLACK:
                    value[i] = -value[i]
                initial_state[i] = value

        initial_state = initial_state.reshape(8,8)
    
        self.white_kingside_castling = self.board.has_kingside_castling_rights(chess.WHITE)
        self.white_queenside_castling = self.board.has_queenside_castling_rights(chess.WHITE)
        self.black_kingside_castling = self.board.has_kingside_castling_rights(chess.    BLACK)
        self.black_queenside_castling = self.board.has_queenside_castling_rights(chess.BLACK)

        state = np.zeros((5,8,8), dtype = np.uint8)

        state[0] = (initial_state >> 3) & 1
        state[1] = (initial_state >> 2) & 1
        state[2] = (initial_state >> 1) & 1
        state[3] = (initial_state >> 0) & 1
        state[4] = (self.board.turn * 1.0)

        return initial_state

if __name__ == "__main__":
    v = State()
    print(v.board)
