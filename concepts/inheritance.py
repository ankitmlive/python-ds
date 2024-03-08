class Parent1:
    def __init__(self, value1):
        self.value1 = value1

    def method1(self):
        print("Method from Parent1")
        print("Value from Parent1:", self.value1)


class Parent2:
    def __init__(self, value2):
        self.value2 = value2

    def method2(self):
        print("Method from Parent2")
        print("Value from Parent2:", self.value2)


class Child(Parent1, Parent2):
    def __init__(self, value1, value2, value3):
        Parent1.__init__(self, value1)
        Parent2.__init__(self, value2)
        self.value3 = value3

    def method3(self):
        print("Method from Child")
        print("Values from Child:", self.value1, self.value2, self.value3)


# Creating an object of Child class
child_obj = Child("Value1 from Child", "Value2 from Child", "Value3 from Child")

# Accessing methods from Parent1
child_obj.method1()

# Accessing methods from Parent2
child_obj.method2()

# Accessing method from Child
child_obj.method3()
