from queue import Queue
class BreadthFirstSearch():
    def __init__(self):
        self.queue = Queue()
    def isEmpty(self):
        return self.queue.empty()
    def addNode(self,node):
        self.queue.put(node)
    def removeNode(self):
        self.queue.get()