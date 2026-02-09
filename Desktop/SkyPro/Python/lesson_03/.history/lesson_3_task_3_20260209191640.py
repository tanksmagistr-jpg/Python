from address import Address
from mailing import Mailing


to_address = Address('644000', 'г.Омск', 'ул.Ленина', 'д. 36', 'кв.11')
from_address = Address('628400', 'г.Сургут', 'ул.30 лет Победы', 'д. 5', '124')
cost = 366
track = 876856798796

mailing1 = Mailing(to_address, from_address, cost, track)
print(mailing1)
