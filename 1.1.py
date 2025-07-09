# 1. Implement the simple methods get_num and get_den that will return the numerator
# and denominator of a fraction.


class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom


    def get_num(self):
        print(f"The numerator is {self.num}")    

    def get_den(self):
        print(f"The denominator is {self.den}")



my_fraction=Fraction(3,5)

my_fraction.get_num()
my_fraction.get_den()