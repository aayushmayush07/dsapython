class Solution:
    def simplifyPath(self, path):
        str_breakdown = []
        last_slash_index = 0
        simplified_stack = []
        final_string = ""

        for i in range(len(path)):
            if path[i] == "/" and i!= len(path)-1:
                print(f"The value of i is {i}")

                word = ""
                if i != 0 and i != len(path) - 1:
                    for j in range(last_slash_index + 1, i):
                        word += path[j]
                    if word != "":
                        str_breakdown.append(word)
                    last_slash_index = i



            elif i == len(path) - 1:
                word = ""
                for j in range(last_slash_index + 1, i + 1):
                    word += path[j]
                if word != "":
            
                    if(word[len(word)-1]=='/'):

                        word=word[:-1]
                    if(word!=""):    
                        str_breakdown.append(word)          
                last_slash_index = i


        for i in range(len(str_breakdown)):
            if str_breakdown[i].startswith('/') or str_breakdown[i] == '.':
                pass
            elif str_breakdown[i] == '..':
                if len(simplified_stack) != 0:
                    simplified_stack.pop()
            else:
                simplified_stack.append(str_breakdown[i])

        print(str_breakdown)        

        for i in range(len(simplified_stack)):
            if(i== len(simplified_stack)-1 and simplified_stack[i]=='/'):
                pass
            else:    
                final_string += '/' + simplified_stack[i]

        
                




        return final_string if final_string else "/"





solution=Solution()

print(solution.simplifyPath("/a/../../b/../c//.//"))



string_to_split="/a/../../b/../c//.//"

component=string_to_split.split('/')

print(component)

