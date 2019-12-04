from Node import Node
from panCakeProblem import PanCakeProblem
from breadthFirstSearch import BreadthFirstSearch
from depthFirstSearch import DepthFirstSearch
class Search():
    def __init__(self,searchProblem,searchStrategy):
        self.searchProblem = searchProblem
        self.searchStrategy = searchStrategy
        
    def solveProblem(self):
        node = Node(self.searchProblem.initialState(),None,0,0,'')
        self.searchStrategy.addNode(node)
        result = None
        duplicateMap = {}
        duplicateMap[node.state.getStringRep()] = node.state.getStringRep()
        while not self.searchStrategy.isEmpty():
            nodePopUp = self.searchStrategy.removeNode()
            #print(nodePopUp)
            #type(nodePopUp)
            if self.searchProblem.goalTest(nodePopUp.state):
                result = nodePopUp
                break
            else:
                nextMoves = self.searchProblem.succesorFunction(nodePopUp.state)
            for nextState in nextMoves:
                if nextState.getStringRep() not in duplicateMap:
                    newNode = Node(nextState,nodePopUp,nodePopUp.depth+1,nodePopUp.cost+nextState.cost,nextState.action)
                    self.searchStrategy.addNode(newNode)
                    duplicateMap[newNode.state.getStringRep()] = newNode.state.getStringRep() 
        return result
    def printResult(self,result):
        if result.parentNode is None:
            print("Search Start")
            print("Initial State is ", result.state.getCurrentState())
            return
        else:
            self.printResult(result.parentNode)
            print("All Parameters are here")
            print("Action is ", result.action)
            print("Current State is ", result.state.getCurrentState())
            print("Cost is ", result.cost)

if __name__=="__main__":
    searchProblem = PanCakeProblem([5,6,8,7,2,6,1],[8,7,6,5,2,1])
    searchStrategy = DepthFirstSearch()
    search = Search(searchProblem,searchStrategy)
    result = search.solveProblem()
    if result is not None:
        search.printResult(result)
            