from abc import abstractmethod

class SearchProblem(object):

    @abstractmethod
    def __init__(self, params):pass
    
    @abstractmethod
    def initialState(self): pass
    
    @abstractmethod
    def succesorFunction(self,currentState): pass
    
    @abstractmethod
    def goalTest(self,currentState): pass
    
    @abstractmethod
    def __str__(self) : pass
        
        
        