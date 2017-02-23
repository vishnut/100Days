class MyQueue(object):
    def __init__(self):
        self.ls = []
    
    def peek(self):
        if len(self.ls) == 0:
            return None
        return self.ls[0]
        
    def pop(self):
        return self.ls.pop(0)
        
    def put(self, value):
        self.ls.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
