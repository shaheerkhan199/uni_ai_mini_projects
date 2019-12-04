from queue import PriorityQueue
class UniformCostSearch():
    def __init__(self):
        self.priorityQueue = PriorityQueue()
    def isEmpty(self):
        return self.priorityQueue.empty() == ""
    def addNode(self,pathCost,dataElement):
        self.priorityQueue.put(pathCost,dataElement)
    def removeNode(self):
        self.priorityQueue.get()
        