class Over:
    
    #Overloading concept is not there is python
    #means we can't have two methods with same name but diff arguments.
    #below method can be used to acheive Overloadig indirectly.
    #we can pass single argument that will be assigned to a.
    @staticmethod
    def sum(self, a=0, b=0, c=0):
        return a + b + c

#Overriding
class Overriding(Over):
    
    def sum(self, a=0, b=0,c=0):
        return a-b-c

o = Overriding()
print(o.sum(1,2,3))    
    
        