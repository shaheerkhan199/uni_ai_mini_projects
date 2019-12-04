from searchStrategy import SearchStrategy
from assignment import Assignment
import math
from inferenceInfo import InferenceInfo
class BactrackingSearch(SearchStrategy):
    def __init__(self,listeners = [],variableOrdering=False,valueOrdering=False):
        SearchStrategy.__init__(self, listeners)
        #self._inferenceProcedure = inferenceProcdeure
        self._variableOrdering = variableOrdering
        self._valueOrdering = valueOrdering
        
    def createBoard(self,n):
        board = list()
        for i in range(n):
            row = list()
            for j in range(n):
                row.append("A")
            board.append(row)
        return board
    
    def displayBoard(self,board):
        for i in range(len(board[0])):
            print(board[i])
            
    def check_cord(self,board,i,j):
        i+=2
        j+=1
        if i<=len(board[0]) and j<=len(board[0]):
            return True
        else:
            return False
    def placeAKnights(self,board,noOfKnights):
        tempBoard = board[:]
        tempBoard[0][0] = "k"
        tempBoard[1][2] = "x"
        tempBoard[2][1] = "x"
        return tempBoard
    
    def placeAllKnights(self,board,noOfKnights):
        if not noOfKnights <= math.pow(len(board[0]),2):
            print("No of nights must be less than or equal to n")
            return " "
        listOfBoard = list()
        dimension = board[0]
        for i in range(len(dimension)):
            for j in range(len(dimension)):
                #print("[",i,",",j,"]")
                if noOfKnights != 0:
                    if not board[i][j] == "X":
                        board[i][j] = "K"
                        listOfBoard.append(board)
                        noOfKnights-=1
                        '''if i+1 <= len(dimension) and j+2 <= len(dimension):
                            board[i+1][j+2] = "X"
                        if i+2 <= len(dimension) and j+1 <= len(dimension):
                            board[i+2][j+1] = "X"
                        
                        #board[i+1][j+2] = "X"'''
                        '''try:
                            a = i+2
                            b = j+1
                            board[a][b] = "X"
                            a = i+1
                            b = j+2
                            board[a][b] = "X"
                        except IndexError:
                            continue'''
                        m = len(dimension)
                        n = m
                        if ((i + 2) < m and (j - 1) >= 0):
                            board[i + 2][j - 1] = "X"
                        if ((i - 2) >= 0 and (j - 1) >= 0):
                            board[i - 2][j - 1] = "X"
                        if ((i + 2) < m and (j + 1) < n):
                            board[i + 2][j + 1] = "X"
                        if ((i - 2) >= 0 and (j + 1) < n):
                            board[i - 2][j + 1] = "X"
                        if ((i + 1) < m and (j + 2) < n):
                            board[i + 1][j + 2] = "X"
                        if ((i - 1) >= 0 and (j + 2) < n):
                            board[i - 1][j + 2] = "X"
                        if ((i + 1) < m and (j - 2) >= 0):
                            board[i + 1][j - 2] = "X"
                        if ((i - 1) >= 0 and (j - 2) >= 0):
                            board[i - 1][j - 2] = "X" 
                        if noOfKnights != 0:
                            self.placeAllKnights(board, noOfKnights-1)
                    else:
                        continue
        return board

    def solve(self,csp):
        return self.recursiveBacktrackingSearch(csp, Assignment())
    
    def orderDomainValues(self,csp,var):
        return csp.getDomainValues(var)
    
    def fireListeners(self,csp,assignment):
        for listener in self._listeners:
            listener.fireChange(csp,assignment)

if __name__=="__main__":
   
    #infInfo = InferenceInfo()
    bts = BactrackingSearch()
    board = bts.createBoard(3)
    print("Initial Empty Board")
    bts.displayBoard(board)
    print("After Placing kights")
    resulting_board = bts.placeAllKnights(board,3)
    bts.displayBoard(resulting_board)