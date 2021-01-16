class Test:
    def __init__(self):
        self.str = "kingforaday"
        self.x = 20

def fun():
    return Test()

t = fun()
print(t.str)
print(t.x)




# A Python program to return multiple   
# values from a method using class  
class Test:  
    def __init__(self):  
        self.str = "geeksforgeeks"
        self.x = 20   
    
# This function returns an object of Test  
def fun():  
    return Test()  
        
# Driver code to test above method  
t = fun()   
print(t.str)  
print(t.x) 