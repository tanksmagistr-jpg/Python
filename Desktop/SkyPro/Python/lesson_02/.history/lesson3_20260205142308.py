class User:
    age = 0;

    def __init__(self, name):
        print('я создался')
        self.username = name

    def sayName(self):
        print('меня зовут', self.username)

    def sayAge(self):
        print(self.age)    

    def setAge(self, newAge):
        self.age = newAge


alex = User('Alex')
mark = User('Mark')
marta = User('3')

user1.sayName()
user1.sayAge()
user1.setAge(33)
user1.sayAge()
