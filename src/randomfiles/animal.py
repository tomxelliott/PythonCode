# within the parentheses you will need to put the name of the class that the new class inherits from.
# for this example, my class will inherit from object which is the superclass for all objects in Python.
# __init__(self) is like a constructor in Java. It must always have at least one argument - self.
# self refers to the object being created.
# pass can be used as a placeholder for when Python expects an expression.
class Animal(object):
	is_alive = True # this is like a field in Java.
    health = "good"
    def __init__(self, name, age):
        self.name = name

    # Python class method
   	def description(self):
        print self.name
        print self.age


zebra = Animal("Jeffrey", 31)
print zebra.name

hippo = Animal("Tom", 27)
hippo.description()
sloth = Animal("Bob", 31)
ocelot = Animal("Steve", 80)

print hippo.health
print sloth.health
print ocelot.health
