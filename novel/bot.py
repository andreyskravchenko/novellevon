class Bot:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell_about_myself(self):
        print "Hello."
        print "I am " + self.name + ", My age is " + str(self.age)