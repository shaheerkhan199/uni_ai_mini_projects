class Stack():
    def __init__(self):
        self.stack = list()
    def push(self,dataElement):
        self.stack.append(dataElement)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is Empty")
            return None
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is Empty")
            return None
    def size(self):
        return len(self.stack)
    def __str__(self):
        stringRep = ''
        for i in range(len(self.stack)):
            stringRep += str(self.stack[i]) + ','
        return stringRep
