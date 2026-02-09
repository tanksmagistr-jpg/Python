class Address:

    def __init__(self, code, city, street, building, apartment):
        self.code = code
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def __str__(self):
        return f'{self.code}, {self.city}, {self.street}, ' /
               f'{self.building} - {self.apartment}'
