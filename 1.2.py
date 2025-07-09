# 2. In many ways it would be better if all fractions were maintained in lowest terms right
# from the start. Modify the constructor for the Fraction class so that GCD is used to
# reduce fractions immediately. Notice that this means the __add__ function no longer
# needs to reduce. Make the necessary modifications.

def gcd(num, den):
    while num % den != 0:
        old_num = num
        old_den = den
        num = den
        den = old_num % old_den
    return den







class Fraction:
    def __init__(self,top,bottom):

        if not isinstance(top, int) or not isinstance(bottom, int):
            raise TypeError("Both numerator and denominator must be integers")

        if bottom == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        # Normalize sign: move minus to numerator
        if bottom < 0:
            top = -top
            bottom = -bottom            
        divisor=gcd(top,bottom)
        self.num=top//divisor
        self.den=bottom//divisor




    def show(self) :
           print(f"The fraction is {self.num}/{self.den}")


    def __add__(self,other_fraction):
         
         new_num=self.num*other_fraction.den+self.den*other_fraction.num
         new_den=self.den*other_fraction.den

         print(f"The result of addition is {new_num}/{new_den}")

    def __sub__(self,other_fraction):
        new_num=self.num*other_fraction.den-self.den*other_fraction.num
        new_den=self.den*other_fraction.den  
        print(f"The result of substraction is {new_num}/{new_den}")

    def __mul__(self,other_fraction):
        new_num=self.num*other_fraction.num
        new_den=self.den*other_fraction.den

        greatest_divisor=gcd(new_num,new_den)

        new_num=new_num/greatest_divisor
        new_den=new_den/greatest_divisor

        print(f"The result of multiplication is {new_num}/{new_den}")



    def __truediv__(self,other_fraction):
        new_num=self.num*other_fraction.den
        new_den=self.den*other_fraction.num

        greatest_divisor=gcd(new_num,new_den)

        new_num=new_num/greatest_divisor
        new_den=new_den/greatest_divisor

        print(f"The result of division is {new_num}/{new_den}")


    def __gt__(self,other_fraction):

        if(self.num*other_fraction.den>self.den*other_fraction.num):
            return True

        else:
            return False    

    def __ge__(self,other_fraction):

        if(self.num*other_fraction.den>=self.den*other_fraction.num):
            return True

        else:
            return False                
    

    def __lt__(self,other_fraction):

        if(self.num*other_fraction.den<self.den*other_fraction.num):
            return True

        else:
            return False        


    def __le__(self,other_fraction):

        if(self.num*other_fraction.den<=self.den*other_fraction.num):
            return True

        else:
            return False      

    def __ne__(self,other_fraction):

        if(self.num*other_fraction.den!=self.den*other_fraction.num):
            return True

        else:
            return False 

    def __radd__(self,other_value):
        other_value=Fraction(other_value,1)


        self.__add__(other_value)
    
    def __iadd__(self,other_fraction):

        self.num=self.num*other_fraction.den+self.den*other_fraction.num
        self.den=self.den*other_fraction.den  

        return self

    def __repr__(self):
        string=f"Fraction({self.num},{self.den})"
        return string

                
first_fraction=Fraction(6,10)
second_fraction=Fraction(6,14)


first_fraction+second_fraction
first_fraction-second_fraction
first_fraction*second_fraction
first_fraction/second_fraction

print(first_fraction>second_fraction)
print(first_fraction>=second_fraction)
print(first_fraction<second_fraction)
print(first_fraction<=second_fraction)
print(first_fraction!=second_fraction)


5+second_fraction


first_fraction+= second_fraction

first_fraction.show()


print(first_fraction)