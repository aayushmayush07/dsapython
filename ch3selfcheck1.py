#my implementation
# class Stack():
#     def __init__(self):
#         self.items=[]

#     def is_empty(self):
#         return self.items==[]

#     def pop(self):
#         return self.items.pop()

#     def push(self,item):

#         self.items.append(item)

#     def peek(self):
#         return self.items[len(self.items)-1]   


#     def size(self):

#         return len(self.items) 
    



# letter="aayush"

# def rev_string(my_str):

#     l=Stack()
#     rev_string=[]
#     for i in range(0,len(my_str)):
#         l.push(my_str[i])

#     for j in range(0,len(my_str)):
#         last_alphabet=l.pop()
#         rev_string.append(last_alphabet)


#     final_rev_string="".join(rev_string)

#     return final_rev_string    



# print(rev_string(letter))



class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)


def rev_string(my_str):
    stack = Stack()
    for char in my_str:
        stack.push(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


print(rev_string("aayush"))
