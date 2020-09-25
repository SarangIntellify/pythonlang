class Sample:
    
    def __init__(self, a , b):
        self.a = a
        self.b = b
    
    def checkOperators(self):
        return self.a + self.b
    
    def check(self, a, b, c):
        return int.__add__(a+b+c)
    
    def __add__(self, other): 
        a = self.a + other.a #this are like input to constructor, so no need to write self.
        b = self.b + other.b
        return Sample(a,b)
     
    def __sub__(self,a):
        return 1   
    
    def __str__(self): #toString() method
        return '{} {} '.format(self.a , self.b)
   
s1 = Sample(1,2) 
s2 = Sample(3,4)

# whenever you use + operator behind the scene __add__ method getting callled we can overload this method in class.
#without operator overloading addition of two object is not possible
#But by overloading the __add__ method in class we can write our own logic.

s3 = s1 + s2 #__add__ method called which we implemented above
print(s3.a)
print(s1-s2)
print(s1) # __str__ method called which we overloaded.
#s1.checkOperatoors("Sarang", 12) -> not allowed, as we are using + operator in that case either both must be int or String.

#s1.check(1,2,3)
