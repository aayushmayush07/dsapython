class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if(len(self.items)==0):
            return True
        return False

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    
    def peek(self):
        return self.items[len(self.items)-1]   


    def size(self):

        return len(self.items)     