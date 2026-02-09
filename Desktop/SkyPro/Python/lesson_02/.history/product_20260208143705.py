class Product:

    def __init__(self, name, price):
        self.username = name
        self.userprice = price
        

    def sayName(self):
        print(self.username)

    def sayPrice(self):
        print(self.userprice)

    def sayNamePrice(self):
        print('наименование', self.username, '')    