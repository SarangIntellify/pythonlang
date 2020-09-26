class TestingException:
    
    def __init__(self):
        pass
    
    def handle(self, a, b, k):
        try:
            print("resource open")
            print(a/b)
            k = int(input("Enter a number"))
        except ZeroDivisionError as e: #except ZeroDivisionError allowed, handling specific exception.
            print("You cannot divide a number by zero", e)
        except ValueError as e:
            print(e)
        except Exception:
             print(e)       
        finally:
            print("resource close")    
            

t = TestingException()
t.handle(5,1,0)
    