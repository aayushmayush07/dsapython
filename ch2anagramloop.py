def checkanagram(first_word,second_word):
    second_word_list=list(second_word)

    matched=True


    if(len(first_word)==len(second_word)):
        for i in range(0,len(first_word)):
            if(matched==False):
                break
            found=[]
            for j in range(0,len(second_word)):
                if(first_word[i]==second_word_list[j]):
                    found.append(j)


            if(len(found)!=0):
                second_word_list[found[0]]=None

            else:
                matched=False            



    return matched


result=checkanagram("veloe","levoe")

print(result)  

    
