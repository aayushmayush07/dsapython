from data_structures.Stack import Stack

digit=2899


def convert_decimal_to_binary(digit):

    stack=Stack()
    bits=[]

    while digit!=0:
        remainder=digit%2
        digit=digit//2
        stack.push(remainder)


    while stack.is_empty()==False:
        s=stack.pop()
        
        bits.append(str(stack.pop()))



    return ''.join(bits)




binary=convert_decimal_to_binary(digit)

print(f"The binary of decimal {digit} is {binary}")

    


