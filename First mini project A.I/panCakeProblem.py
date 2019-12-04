from searchProblem import SearchProblem
from panCakeState import PanCakeState
class PanCakeProblem(SearchProblem):
    def __init__(self,initialState,goalState):
        if len(initialState) < 5:
            print("Pan Cakes Must be greater than 5")
        else:
            self._initialState = PanCakeState(initialState,'',0)
            self._goalState = goalState
        
    def initialState(self):
        return self._initialState
    
    def flip(self,currentState,index):
        newStackOfPanCakes = currentState[:]
        sliceOfStack = currentState[index:]
        sliceOfStack.reverse()
        #newStack = currentState[(index+1):]
        for i in range(index,len(currentState)):
            newStackOfPanCakes[i] = sliceOfStack[i-2]
        return newStackOfPanCakes
    
    def successorFunction(self,cs,index):
        nextMoves = list()
        currentState = cs.getCurrentState()
        newState = self.flip(currentState,index)
        nextMoves.append(newState)
    
    def goalTest(self,currentState):
        goalState = sorted(self.currentState.getCurrentState())
        cs =  currentState.getCurrentState()
        if cs == goalState:
            return True
        else:
            return False

