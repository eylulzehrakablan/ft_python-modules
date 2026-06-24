#!/usr/bin/env python3

class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # instance method
    def get_info(self):
        return f"Name: {self.name}\nGPA: {self.gpa}"

    @classmethod
    def get_count(self):
        return f"Total number of students: {self.count}"

s1 = Student("zehra", 4)
s2 = Student("deniz", 4)
print(s1.get_info())
print(s2.get_info())
print(s1.get_count())
print(end="\n\n")


class Plant:
    def __init__(self, name, age = "not initialized"):
        self.name = name # instance attribute
        self.age = age
    # instance methods take the instance itself as the first argument
    # instance method is a regular method inside the class, instance methods
    # can read and modify both object-specific attributes and class-wide attributes
    # use these when the you need to know about or change a specific object's state
    
    @classmethod
    def create_instance(cls):
        print("Plant created ~")
        return cls("plant", 0)

    def get_name(self):
        return f"Plant name: {self.name}"
    
    def set_age(self, age):
        self.age = age
        print("Plant age updated")


p1 = Plant("Rose")
print(p1.get_name())
print(f"Plant age: {p1.age}")
p1.set_age(1)
print(f"Plant age: {p1.age}")
print()
p2 = Plant.create_instance()
print(p2.get_name())
p2.name = "sunflower"
print("plant name updated ~")
print(p2.get_name())
print(f"Plant age: {p2.age}")
p2.set_age(5)
print(f"Plant age: {p2.age}")
print(end="\n\n")


# static methods are completely independent of the class or instance state
# do not take cls or self as an argument, static method are not actually depend
# on anything, they are just regular methods that meants to be in
# 'that' class because the method is like a helper function relevant to class
class Burger:
    def __init__(self, toppings):
        self.toppings = toppings

    def get_info(self):
        toppings_str = ", ".join(self.toppings)

        # if self.is_healthy(self.toppings):
        if Burger.is_healthy(self.toppings): # better practice
            health_status = "Unhealthy"
        else:
            health_status = "Healthy"

        return f"The burger has {toppings_str} inside --> {health_status} choice"

    @classmethod
    def cook_burger(cls):
        print(f"A plain burger is ready!")
        return cls(["lettuce", "tomato", "onion"])

    @classmethod
    def cook_saucy_burger(cls):
        print(f"A saucy burger is ready!")
        return cls(["lettuce", "tomato", "mayonnaise", "onion"])
        
    @staticmethod
    def is_healthy(toppings):
        return "mayonnaise" not in toppings
    

b1 = Burger.cook_burger()
print(b1.get_info())

b2 = Burger.cook_saucy_burger()
print(b2.get_info())
