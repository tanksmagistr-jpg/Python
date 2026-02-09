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


user1 = User('1')
user2 = User('2')
user3 = User('3')

user1.sayName()
user1.sayAge()
user1.sayAge(33)
