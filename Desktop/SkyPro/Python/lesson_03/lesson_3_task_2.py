from smartphone import Smartphone

catalog = [
    Smartphone('iPhone', '17 Pro', '+79228000102'),
    Smartphone('Samsung', 'Galaxy S25', '+79228000103'),
    Smartphone('Xiaomi', '15 Ultra', '+79228000104'),
    Smartphone('HONOR', 'Magic7 Pro', '+79228000105'),
    Smartphone('HUAWEI', 'Pura 80 Ultra', '+79228000106')
]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.t_number}')
