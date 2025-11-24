from datetime import datetime

class Person:
    def __init__(self, person_id, name, age, email):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.email = email
        self.cars = []
    
    def add_car(self, car):
        """Add a car to person's cars list"""
        # TODO: implement
        pass
    
    def get_cars_count(self):
        """Return the number of cars owned"""
        # TODO: implement
        pass
    
    def __str__(self):
        """String representation of person"""
        # TODO: implement
        pass
    
    def to_dict(self):
        return vars(self)
