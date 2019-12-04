from abc import abstractmethod
class Heuristic(abstractmethod):
    def __init__(self):
        pass
    def evaluateNode(self,state,goal):
        pass