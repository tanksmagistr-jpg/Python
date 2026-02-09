class Product:

    def __init__(self, name, price):
        print('Наименование', name, 'Цена', )
        self.username = name
        self.userprice = price


    def sayName(self):
        print(self.username)

    def sayPrice(self):
        print(self.userprice)