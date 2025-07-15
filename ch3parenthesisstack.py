from data_structures.Stack import Stack


example_parenthesis="((())))"


def check_balanced(parenthesis):

    stack=Stack()

    for i in range(len(parenthesis)):
        if(parenthesis[i]=="("):

            stack.push("(")

        elif(parenthesis[i]==")" ):
            if(stack.is_empty()==True):
                print("parenthesis is not balanced")
                return
            stack.pop()   


    if(stack.is_empty()==True):

        print("parenthesis is balanced")
    else:
        print("parenthesis isnt balanced")     




check_balanced(example_parenthesis)