class User:

    def __init__(self, name):
        print('я создался')
        self.username = name

    def sayName(self):
        print('меня зовут', self.username)

user1 = User('1')
user2 = User('2')
user3 = User('3')

user1.sayName
user2,sau