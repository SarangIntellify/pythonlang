class parent:

    def __init__(self, name):
        print("Constructor of parent called and name is", name)

class child(parent):
      
    def __init__(self, name):
        super().__init__(name) # calling parent constructor
        print("Constructor of child called")        

#it will prefer left to right, in this case parent class constructor will be called.
class grandchild(child):
   
      def __init__(self, n):
          super().__init__(n)
          print("Grand child Constructor called")


g  = grandchild("Sarang Kumar")