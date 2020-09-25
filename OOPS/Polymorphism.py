class SuperParent:
    
    def execute(self):
        print("Executing Super parent method")        
     
class SubParent:
    
    def code(self, who):
        who.execute()

class Parent:
    
    def execute(self):
        print("Executing Parent class method")


sp = SuperParent()
p = Parent()
sub = SubParent()
sub.code(p) #whatever object pass, it should have method.
        
#Consider class SuperParent and SubParent implements interface(in case of java), so they will have same method implementation -> Polymorphism
        