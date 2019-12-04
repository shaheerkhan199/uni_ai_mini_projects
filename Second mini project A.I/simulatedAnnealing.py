from datetime import datetime
import random
class SimulatedAnnealing():
    def __init__(self,board, noOfKnights):
        self.board = board
        self.noOfKnights = noOfKnights
        self.elapsedTime = 0
        self.temperature = 4000
        self.schedule = 0.9
        self.startTime = datetime.now()
        
    def placeKnightRandomly(self):
        states = list()
        while self.noOfKnights != 0:
            i = random.randint(0,len(self.board[0]))
            j = random.randint(0,len(self.board[0]))
            if self.board[i,j] != 'K':
                self.board[i,j] = 'K'
                self.noOfKnights -=1
                states.append(self.board)
        return states
                
    def run(self):
        self.solutionFound = False
        self.current = self.placeKnightRandomly()[0]
        self.next = self.placeKnightRandomly()[0]
        while True:
            self.temperature *= self.schedule
            if self.temperature == 0:
                return self.current
            
            