from data_structures.Stack import Stack


example_parenthesis="[({[{(())}]})]"


def checker(parenthesis):
    stack=Stack()
    opening_closing_pair={"(":")","[":"]","{":"}"}


    for i in range(0,len(parenthesis)):

        if parenthesis[i] in opening_closing_pair:
            stack.push(parenthesis[i])

        else:

            
            if(stack.is_empty()==True):

                print("The parenthesis is unbalanced")
                return   

            element=stack.peek()

            
                
            if opening_closing_pair[element]==parenthesis[i]:
                stack.pop()

            else:    
                print("The parenthesis is unbalanced")
                return


    if(stack.is_empty()==True):
        print("The parenthesis is balanced")

    else:
        print("The parenthesis is not balanced")            




checker(example_parenthesis)