class Product:

    def __init__(self, name, price):
        self.username = name
        self.userprice = price       

    def sayName(self):
        return self.username

    def sayPrice(self):
        return self.userprice

    def sayNamePrice(self):
        return f'наименование:' {self.username}, 'цена:', self.userprice