from datetime import datetime
from DBmanager import DatabaseManager
DBmanager = DatabaseManager('mydb.db')
from car import Car


class Person:
    def __init__(self, person_id, name, age, email):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.email = email
        self.cars = []
    
    def add_car(self, car):
        return DBmanager.cursor.insert_car(car)

    def get_cars_count(self):
        cars = DBmanager.cursor.execute('SELECT * FROM cars WHERE owner_id = ?', (self.person_id,))
        cars = cars.fetchall()
        return cars

    def __str__(self):
        """String representation of person"""
        return "".join([f'{k}: {v}\n' for k,v in vars(self).items()])

    
    def to_dict(self):
        return vars(self)
    
a = Person('326080025', 'efraim', 21, 'efgo583208979@gmail.com')
mycar = Car('2323', 'toyota', 'corola', 2021, 'blue')