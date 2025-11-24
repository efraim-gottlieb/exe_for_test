class Car:
    def __init__(self, car_id, brand, model, year, color, owner_id=None):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.owner_id = owner_id
    
    def get_age(self):
        """Calculate car age"""
        # TODO: implement
        pass
    
    def __str__(self):
        """String representation of car"""
        # TODO: implement
        pass
    
    def to_dict(self):
        """Convert car to dictionary"""
        # TODO: implement
        pass