a="lovoe"
b="voloe"


def checkanagram(first_word,second_word):

    if(len(a)==len(b)):
        letters_matched=0
        for i in range(0,len(a)):
            for j in range(0,len(b)):
                if(a[i]==b[j]):
                    letters_matched+=1

        if(letters_matched==len(a)):
            return True

        else:
            return False


        


result =checkanagram(a,b)

print(result)


#O(n^2)