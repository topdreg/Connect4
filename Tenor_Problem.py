#Global variable to track if there is a player who has won. 
winState = False
winPlayer = 0

#Basic piece used in a game.
#The variables right and down point to the adjacent right and down pieces. 
#"Hit" describes whether a piece has actually fallen in that area from either player 1 or player 2. 
#There are four winTracker variables to tally whether four of the same colored pieces are adjacent
#to one another, so as to avoid a brute force method of determining a win. 

class x4Piece(object):  
    hit = False 
    winTrackerVert = 0
    winTrackerHoriz = 0
    winTrackerDiagUp = 0
    winTrackerDiagDown = 0 
    player = 0 

#I hate how long and bloated this method is. However, I don't see much benefit in separating the separate cases 
#into their own methods. It would just be more bloat spread farther out.
# The code this time takes into account pieces to the left as well as the right, and if a piece falls in the middle
#of two sequences.  

def updateTrackers(player, row, col, game):
    global winPlayer
    global winState
    #check win condition to see if we can bypass the trackers
    if (winState == True): 
        return 
    updateValue = 0 
    
    #-Horizontal tracker check and update-
    if col < 6 and game[row][col + 1].hit == True and game[row][col + 1].player == player:
        game[row][col].winTrackerHoriz += game[row][col + 1].winTrackerHoriz 
    if col > 0 and game[row][col - 1].hit == True and game[row][col - 1].player == player: 
        game[row][col].winTrackerHoriz += game[row][col - 1].winTrackerHoriz 
    game[row][col].winTrackerHoriz = game[row][col].winTrackerHoriz + 1 
    updateValue = game[row][col].winTrackerHoriz
    #Update other horizontal winTracker values 
    for Col in range(col - 1, 0): 
        if game[row][Col].player != player:
            break 
        else: 
            game[row][Col].winTrackerHoriz = updateValue
    for Col in range(col + 1, 6): 
        if game[row][Col].player != player: 
            break 
        else: 
            game[row][Col].winTrackerHoriz = updateValue 
    #Check if win condition achieved
    if updateValue == 4: 
        winState = True
        winPlayer = player 

    #-Vertical tracker check and update-
    if row < 5 and game[row + 1][col].player == player:
        game[row][col].winTrackerVert += game[row + 1][col].winTrackerVert
    game[row][col].winTrackerVert = game[row][col].winTrackerVert + 1
    #check win condition
    if game[row][col].winTrackerVert == 4: 
        winState = True
        winPlayer = player 

    #-Diagonal check and update- 
    #Down diagonal check
    if col < 6 and row < 5 and game[row + 1][col + 1].hit == True and game[row + 1][col + 1].player == player:
        game[row][col].winTrackerDiagDown += game[row + 1][col + 1].winTrackerDiagDown     
    if col > 0 and row > 0 and game[row - 1][col - 1].hit == True and game[row - 1][col - 1].player == player:
        game[row][col].winTrackerDiagDown += game[row - 1][col - 1].winTrackerDiagDown
    game[row][col].winTrackerDiagDown = game[row][col].winTrackerDiagDown + 1 
    updateValue = game[row][col].winTrackerDiagDown 
    #Update other down diagonal values
    for Col, Row in zip(range(col + 1, 6), range(row + 1, 5)): 
        if game[Row][Col].player == player:
            break
        else:
            game[Row][Col].winTrackerDiagDown = updateValue          
    for Col, Row in zip(range(col - 1, 0), range(row - 1, 0)): 
        if game[Row][Col].player == player:
            break
        else:
            game[Row][Col].winTrackerDiagDown = updateValue
    #Check win condition
    if game[row][col].winTrackerVert == 4: 
        winState = True
        winPlayer = player

    #Up diagonal check
    if col < 6 and row > 0 and game[row - 1][col + 1].hit == True and game[row - 1][col + 1].player == player:
        game[row][col].winTrackerDiagUp += game[row - 1][col + 1].winTrackerDiagUp     
    if col > 0 and row < 5 and game[row + 1][col - 1].hit == True and game[row + 1][col - 1].player == player:
        game[row][col].winTrackerDiagUp += game[row + 1][col - 1].winTrackerDiagUp
    game[row][col].winTrackerDiagUp = game[row][col].winTrackerDiagUp + 1 
    updateValue = game[row][col].winTrackerDiagUp 
    #Update other up diagonal values
    for Col, Row in zip(range(col + 1, 6), range(row - 1, 0)): 
        if game[Row][Col].player == player:
            break
        else:
            game[Row][Col].winTrackerDiagUp = updateValue          
    for Col, Row in zip(range(col - 1, 0), range(row + 1, 5)): 
        if game[Row][Col].player == player:
            break
        else:
            game[Row][Col].winTrackerDiagUp = updateValue
    #Check win condition
    if game[row][col].winTrackerVert == 4: 
        winState = True
        winPlayer = player 




#Method for putting a piece into the game from either player 1 or player 2. The game, based on looking at it on Wikipedia, 
#has 6 rows and 7 columns.
#The variable "player" takes either value 1 or 2. "col" stands for column. After marking the piece and identify which player put the piece in, the winTracker variables are uupdated.  
def inputPiece(player, col, game):
    if (game[0][col].hit == True): 
        print('The column selected is full\n')
        return 
    #Find the most recent piece in the column 
    for row in range(6):  
        if row == 5 or game[row + 1][col].hit == True:
            game[row][col].hit = True
            game[row][col].player = player
            updateTrackers(player, row, col, game)
            break
    
def checkVictory(): 
    global winPlayer
    global winState
    if winState == False: 
        print 'No player has won yet :(\n'
    else:
        print 'Player ' + str(winPlayer) + ' is the winner!\n' 

def printBoard(game):
    for row in range(6): 
        for col in range(7): 
            if game[row][col].hit == False: 
                print '*', 
            elif game[row][col].player == 1: 
                print 'X', 
            else:
                print 'O', 
        print '\n' 
 
game = [[x4Piece() for i in range(7)] for j in range(6)]
inputPiece(1, 0, game)
inputPiece(1, 1, game)
inputPiece(1, 1, game)
inputPiece(2, 0, game)
inputPiece(1, 0, game)
inputPiece(1, 0, game)
inputPiece(1, 0, game)
printBoard(game)
checkVictory() 



        
