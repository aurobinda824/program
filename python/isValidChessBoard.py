board ={"1h" : "bking", "6c" : "wqueen", "2g" : "bbishop", "5h": "bqueen", "3e" : "wking"}

def isValidChessBoard(board):
    count = {"w":0,"b":0,"wpawn":0,"bpawn":0}
    for i in board.values():
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1
        if i[0] == "w":
            count["w"] +=1
        if i[0] == "b":
            count["b"] +=1
    if count["wking"] !=1  or count["bking"] != 1:
        return False
    if count["w"]>16 or count["b"] >16:
        return False
    if count["wpawn"] >8 or count["bpawn"] >8:
        return False
    return True
print(isValidChessBoard(board))        