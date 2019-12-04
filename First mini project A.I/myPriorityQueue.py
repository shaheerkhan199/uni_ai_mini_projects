class priorityQueue():
    def __init__(self):
        self.priorityQueue = dict()
    def enqueue(self,dataElement,pathCost):
        self.priorityQueue[pathCost] = dataElement
    def dequeue(self):
        '''cost,data = self.priorityQueue.items()
        minCost = min(cost)
        maxPriorityElement = self.priorityQueue[minCost]
        return maxPriorityElement
        print(self.cost)'''
        for cost,data in self.priorityQueue.items():
            print("COst is ", cost,"Data is",data)
            
    
q = priorityQueue()
q.enqueue(5,"Ali")
q.enqueue(3,"Ahmed")
q.enqueue(2,"Kashif")
print(q.dequeue)
print(q)
        