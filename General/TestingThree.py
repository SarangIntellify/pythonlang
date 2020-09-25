class TestingThree:
    
    school  = "Sarang" #class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getaverage(self):  #accessor - getters and mutator - setters
        return ((self.m1 + self.m2 + self.m3) / 3)
    
    @classmethod #this decorator defines the method as class method it is not static method, we can ignore self keyword for that method
    def getSchool(cls):
        print(cls.school) #calling class variable by using class reference, cls is a keyword to refer class

    @staticmethod 
    def info(): #this is static method. If you dont want to do anything with class or object variable then use static method
        print("This is static function")

t = TestingThree(1,2,3)
print(t.getaverage())

TestingThree.getSchool() #calling class function. no need to pass anything as cls keyword helps is referring class on which method is called same like self for object.
TestingThree.info() #calling static function. no keyword for static function