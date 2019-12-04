# Variables = Knights
# Domain = Cordinates of the board
# Constraint 2Hand1V or 2Vand1H
class ForwardChecking():
    def __init__(self):
        pass
    def removeDomainFromVariable(self,knight,dictOfVariablesWithDomain,i,j):
        domainOfKnight = dictOfVariablesWithDomain[knight] 
        cordinate = [i,j]
        index = domainOfKnight.index(cordinate)
        del domainOfKnight[index]
        
    def doInference(self,noOfKnights,board):
        self.emptyDomain = False
        boardSize = len(board[0])
        listOfCordinates = list()
        for i in range(boardSize):
            for j in range(boardSize):
                listOfCordinates.append([i,j])
        #print(listOfCordinates)
        variablesWithDomain = dict()
        for i in range(noOfKnights):
            variablesWithDomain['K'+str(i+1)] = listOfCordinates
        #print(variablesWithDomain)
        i = 1
        for i in range(boardSize):
            for j in range(boardSize):
                knight = 'K'+str(i)
                board[i][j] = knight
                self.removeDomainFromVariable(knight,variablesWithDomain,i,j)
                
                if ((i + 2) < len(board[0]) and (j - 1) >= 0):
                    board[i + 2][j - 1] = "X"
                    row,col = i+2,j-1
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                    
                if ((i - 2) >= 0 and (j - 1) >= 0):
                    board[i - 2][j - 1] = "X"
                    row,col = i-2,j-1
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                    
                if ((i + 2) < len(board[0]) and (j + 1) < len(board[0])):
                    board[i + 2][j + 1] = "X"
                    row,col = i+2,j+1
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                    
                if ((i - 2) >= 0 and (j + 1) < len(board[0])):
                    board[i - 2][j + 1] = "X"
                    row,col = i-2,j+1
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                    
                if ((i + 1) < len(board[0]) and (j + 2) < len(board[0])):
                    board[i + 1][j + 2] = "X"
                    row,col = i+1,j+2
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                    
                if ((i - 1) >= 0 and (j + 2) < len(board[0])):
                    board[i - 1][j + 2] = "X"
                    row,col = i-1,j+2
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                    
                if ((i + 1) < len(board[0]) and (j - 2) >= 0):
                    board[i + 1][j - 2] = "X"
                    row,col = i+1,j-2
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                    
                if ((i - 1) >= 0 and (j - 2) >= 0):
                    board[i - 1][j - 2] = "X" 
                    row,col = i-1,j-2
                    self.removeDomainFromVariable(knight,variablesWithDomain,row,col)
                i+=1
                if i == noOfKnights:
                    break
                if (variablesWithDomain[knight] == []):
                    print("Error is detected!!!")
                    print("Domain of",knight,"is empty")
                    self.emptyDomain = True
                if self.emptyDomain:
                    self.doInference(noOfKnights,board)
                    
                
                
         
         
        