from myStack import Stack
class DepthFirstSearch():
    def __init__(self):
        self.stack = Stack()
    def isEmpty(self):
        return self.stack.isEmpty()
    def addNode(self,node):
        self.stack.push(node)
    def removeNode(self):
        self.stack.pop()