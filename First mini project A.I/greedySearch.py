from queue import PriorityQueue
class GreedySearch():
    def __init__(self,heuristic):
        self.heuristic = heuristic
        self.frindge = PriorityQueue()
    def isEmpty(self):
        return self.frindge == []
    def addNode(self,node):
        self.frindge.put(self.heuristic.evaluateNode(node.state.currentState),node)
    def removeNode(self):
        return self.frindge.get()   
            