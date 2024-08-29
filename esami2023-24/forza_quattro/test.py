
def AddVectors(vec1 : tuple[int, int], vec2 : tuple[int, int]) -> tuple[int, int]:
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def Scalevector(vec : tuple[int, int], scaleFactor) -> tuple[int, int]:
    return (vec[0] * scaleFactor, vec[1] * scaleFactor)

def DoesBoardContainValueAtLocation(board : list[list[bool]], position : tuple[int, int], value : bool) -> bool:
    (x, y) = position
    #if out of range, then the cell must be empty or inexistant
    try:
        return (board[x][y] == value)
    except Exception: # the only possible exception is out of bounds
        return False

def DrawBoard(board : list[list[bool]]):
    for x in range(6, -1, -1):
        for l in board:
            if x >= len(l):
                print("-", end="")
            else:
                print("X" if l[x] else "O", end="")
        print() #new line
    print()

DIRECTIONS = ((0, 1), (1, 0), (1, 1)) #set outside of function to not need to re-build the list every time the function is called.

def DetectWinCondition(board : list, lastMove : int) -> bool:
    global DIRECTIONS
    centrePosition = (lastMove, len(board[lastMove]) - 1) #position to look around at
    player = board[centrePosition[0]][centrePosition[1]] #get player to test for (representative bool)
    for dir in DIRECTIONS:
        currentCount = 0
        for i in range(-3, 4):
            if DoesBoardContainValueAtLocation(board, AddVectors(centrePosition, Scalevector(dir, i)), player):
                currentCount += 1
            else:
                currentCount = 0
            if currentCount == 4:
                return True
            
def PlayMove(board : list, position : int, player : str):
    board[position].append(player == "G2")

#the use of a dynamic array rather than static size one can cause a lot of reallocation in memory and inefficiencies, 
#but for something this small and simple, it doesn't really matter...

#False is G1 (0), True is G2 (X).
board = [[],
         [],
         [],
         [],
         [],
         [],
         []]

print("Initial grid:")
DrawBoard(board)

with open("mosse.txt", "r") as file:
    for (moveNum, line) in enumerate(file):
        (player, move) = line.split(" ")
        print(player + " is to move:")
        PlayMove(board, int(move), player)
        DrawBoard(board)
        gameWon = DetectWinCondition(board, int(move))
        if gameWon:
            print(f"Player {player} has won in {moveNum} moves.")
            break
