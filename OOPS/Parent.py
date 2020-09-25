class Parent:

    def featureOne(self):
        print("Feature one of parent")
    
    def featureTwo(self):
        print("Feature two of parent")

class Child(Parent):  #inheriting from parent class

        def featureThree(self):
            print("Feature Three of child")

        def featureFour(self):
            print("Feature Four of child")

class SmallChild(Child): #multi level inheritance

        def featureFive(self):
            print("Feature Five of Small Child")

class Others:

        def featureFive(self):
            print("Feature of others")

#if inherited class have same method name then class you write first inside parenthesis, that class method will be considered => left to right
class GrandParent(Others, SmallChild): #multiple inheritance

        def featureSix(self):
            print("Feature six of grandparent")


g = GrandParent()
g.featureFive()
