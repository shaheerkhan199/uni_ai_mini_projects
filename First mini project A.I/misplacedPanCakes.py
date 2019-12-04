from heuristicForGreedy import Heuristic
class MisplacedPanCakes(Heuristic):
    def __init__(self,goal):
        self.goal = goal
    def evaluateNode(self,state):
        totalCost = 0
        for i in range(len(state)):
            for j in range(len(state)-1-i):
                if state[j] > state[j+1]:
                    state[j], state[j+1] = state[j+1], state[j]  
                    totalCost=totalCost+1
        return totalCost
            
            
        
    