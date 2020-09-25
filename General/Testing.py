class Testing:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("Init method is a constructor")
    
    def functionName(self, name):
        print("Hey this is " + name)
        print("In order to refer the instance variable use self ", self.cpu)

t = Testing(12, 13)
t1 = Testing(12, 14)
t.functionName("sarang")