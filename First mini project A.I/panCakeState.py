from searchState import SearchState
class PanCakeState(SearchState):
    def __init__(self,currentState,action,cost):
        self.currentState = currentState
        self.action = action
        self.cost = cost
        self.stringRep = ''
        
    def getCurrentState(self):
        return self.currentState
    
    def getAction(self):
        return self.action
    
    def getCost(self):
        return self.cost
    
    def getStringRep(self):
        if self.stringRep == '':
            stackOfPanCakes = ''
            for i in range(len(self.currentState)):
                stackOfPanCakes += str(self.currentState[i]) + ','
            self.stringRep = stackOfPanCakes
        return self.stringRep

#panCake = PanCakeState([5,9,8,7,6,2],'',0)
#print(panCake.getStringRep())