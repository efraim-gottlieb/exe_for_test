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
    
    def add_car(self, car):
        car.owner_id = self.person_id
        DBmanager.cursor.execute("UPDATE cars SET owner_id = ? WHERE car_id = ?",(self.person_id, car.car_id))

    def get_cars_count(self):
        cars = DBmanager.cursor.execute('SELECT * FROM cars WHERE owner_id = ?', (self.person_id,))
        cars = cars.fetchall()
        return cars

    def __str__(self):
        """String representation of person"""
        return "".join([f'{k}: {v}\n' for k,v in vars(self).items()])

    
    def to_dict(self):
        return vars(self)
    
a = Person('a326080025', 'efraim', 21, 'efgo583208979@gmail.com')
DBmanager.insert_person(a)
# mycar = Car(1, 'toyota', 'corola', 2021, 'blue')
# a.add_car(a)
