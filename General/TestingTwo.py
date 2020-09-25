class TestingTwo:
          
        college = "SOCET" #static variable

        def __init__(self, name, age, animal):
            print("Constructor called")
            self.myName = name
            self.myAge = age
            self.myAnimal = animal

        def getName(self):
            return self.myName
        
        def getAge(self):
            return self.myAge

        def getAnimal(self):
            return self.myAnimal


t = TestingTwo("Sarang", 12, "giraffe")
print(t.getAge(), TestingTwo.college)
print(t.getName(), TestingTwo.college)
print(t.getAnimal(), TestingTwo.college)