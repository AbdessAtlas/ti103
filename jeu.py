import chess

board = chess.Board()

print(board)
# print(repr(board))

# for lm in board.legal_moves:
#    print(lm, repr(lm))

board.push_san("e4")
print()
print(board)

for lm in board.legal_moves:
    print(lm, repr(lm))

if not board.is_checkmate():
    print("La partie n'est pas finie")
