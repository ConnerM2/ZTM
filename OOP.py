class Object: # This is a class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
        return 'Hello' # Without this return, the function will return None

obj1 = Object("John", 20) # This is an instance of the Object class
obj2 = Object("Jane", 21)

obj2.last_name = "Doe" # This is an attribute of the Object class


print(obj1.name, obj1.age)
print(obj2.name, obj2.age, obj2.last_name)
print(obj1.greet())
print(type(obj1))