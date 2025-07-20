class Solution:
    def trap(self, height) -> int:
        stack=[]
        output=0
        h=[]
        w=[]

        for i in range(0,len(height)):
            if(i==0):
                stack.append(i)
            elif(height[i]<=height[i-1]):
                stack.append(i)

            else:
                last_max_height=0
                print(f"The value of i is {i}")
                print(f"The element in stack right now is")
                

                base_height=height[stack[len(stack)-1]]
                print(f"The initialised base height is {base_height}")
                for j in range(stack[len(stack)-1],-1,-1):
                    if(height[j]>base_height):
                        last_max_height=height[j]
                        min_height=min(last_max_height,height[i])
                        print(f"The min height is {min_height}")
                        if(min_height==height[i]):
                            print("Entered a case where the h[i] is less")
                            print(h,w)
                            h.append(min_height-base_height)
                            w.append(i-j-1)
                            stack.pop()
                            break

                        h.append(min_height-base_height)
                        w.append(i-j-1)
                        print(f"The height is {h} and width is {w}")
                        base_height=min_height
                        stack.pop()
                        print(f"the changed base height is {base_height}")









                


                
        for i in range(0,len(h)):

            output+=h[i]*w[i]


        print(f"The output is {output}")    


                




        return output








solution=Solution() 

print(solution.trap([4,2,0,3,2,5]
))




        