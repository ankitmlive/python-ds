from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, model, company, make):
        self.model = model
        self.make = make
        self.company = company
 
    def show(self):
        print("I am a abstract class")

class Car(Vehicle):

    def __init__(self, model, company, make, *args):
        super().__init__(model, company, make)

class Bike(object):
    """docstring for Bike."""

    def __init__(self, model, company, make, *args):
        self.args = []
        super().__init__(model, company, make)
        for args in *args:
            self.args.appned(args)
