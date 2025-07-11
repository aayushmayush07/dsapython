items= [ 23,21,45,61,12,1,7,99,0,888 ]




def nsqrsolution():
    min_num=9999
    

    for item in items:
        print(item)
        for i in range(0,len(items)):
            if (item<items[i] and item<min_num):
          
                min_num=item
    
    return min_num


def nsolution():
    min_num=9999
    item=items[0]
    for i in range(len(items)):
        if(item>items[i]):
            min_num=items[i]

    return min_num        




nsqrsolution=nsqrsolution()
nsolution=nsolution()

print(f"The n square solution is {nsqrsolution} ")
print(f"The n solution is {nsolution}")
    