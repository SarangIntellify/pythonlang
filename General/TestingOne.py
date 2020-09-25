class TestingOne:
    
    def __init__(self):
        print("Constructor called")
        self.name = "Sarang"
        self.age = 20
    
    def updateAge(self):
        print("Object called update age method", self) # self becomes the object who is calling the method. Example below.
        self.age = 30

    def compare(self, other): #here self is t because on that object we are calling compare method.
        if (self.age == other.name):
            return True
        else:
            return False

t = TestingOne()
t2 = TestingOne()
t2.name = "Kumar"

t.updateAge()
print(t.age)

if t.compare(t2):
    print("They are same")
else :
    print("They are not same")



