def isValidChessBoard(dict):
    validSpot = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6', '7', '8']
    pieceName = ['pawn', 'knight', 'bishop', 'rook', 'queen','king']
    
    values = list(dict.values())
    keys = list(dict.keys())

    if not values.count('bking') and not values.count('wking'): # Check if the board have a White King and Black King
        return False
    if values.count('bking') > 1 or values.count('wking') > 1: # Check if there's more than 2 King
        return False
    if values.count('wpawn') > 8 or values.count('bpawn') > 8: # Check if there's more than 8 pawns
        return False
    wPieces, bPieces = 0, 0
    for pieces in range(len(values)): # Count each player pieces
        if values[pieces][0] == 'b':
            bPieces += 1
        elif values[pieces][0] == 'w':
            wPieces += 1
        else:
            return False
    if bPieces > 16 or wPieces > 16: # Check if anyone have more than 16 pieces
        return False
    for spot in range(len(keys)):
        if keys[spot][0] not in validSpot or keys[spot][1] not in validSpot: # Check if the piece place is right
            return False
    for pieces in range(len(values)):  # Check piece name
        if values[pieces][1:] not in pieceName:
            return False
    return True


chessBoard = {
    '1h': 'bking',
    '6c': 'wqueen',
    '8g': 'bbishop',
    '8h': 'bqueen',
    '3e': 'wking'
}

print(isValidChessBoard(chessBoard))