class TestingFour:
   
    classV = "Class variable"

    def __init__(self, name):
        print("Constructor called")
        self.name = name
    
    def instanceFunction(self):
        print(self.name)
        print(TestingFour.classV) # can access class variable inside instance function

    @classmethod
    def classFunction(self, cls):
        print(cls.classV)
       # print("Instance variable ",  self.name)  cannot use instance or object variable inside the class methods
   
    @staticmethod
    def staticFunction(self): # or can ad class reference)
        print(self.name) #can use instance or object variable inside static function
        print(TestingFour.classV) #can use class variable inside static function

    
t = TestingFour("Sarang")
t.staticFunction(t) 
t.instanceFunction()  
