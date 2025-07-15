class Stack():
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def pop(self):
        return self.items.pop()

    def push(self,item):

        self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]   


    def size(self):

        return len(self.items) 



s=Stack()

print(s.items)

s.push(5)

print(s.items)