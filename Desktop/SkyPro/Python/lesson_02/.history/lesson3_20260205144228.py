from user import User
from card import Card

alex = User('Alex')

alex.sayName()
alex.setAge(33)
alex.sayAge()
alex

card = Card('6655 1234 2345 4567',  '11/28', 'Alex F')
card.pay(1000)
