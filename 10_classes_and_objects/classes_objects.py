class MyClass:
    variable = "bleh"

    def function(self):
        print("message inside the class")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yuh"

#print(myobjectx.variable)
#print(myobjecty.variable)

#myobjectx.function()

class NumberHolder:

    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number
    
var = NumberHolder(7)
print(var.returnNumber())