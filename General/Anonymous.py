from functools import reduce

class Play:
    
    v = 4
    
    def checkAno(self, f):
       return f(4) + Play.v
   

p = Play()

f = lambda a : a * a  # lambda function in python

#print(p.checkAno(f))

nums = [1,2,3,4,6]

evens = list(filter(lambda a : a % 2 == 0  , nums))
evens = list(map(lambda a : a * 2,  evens))
print(evens)
sum = reduce(lambda a,b : a + b, evens) #it process two variables at a time
print(sum)