# как то получить от пользователя оценку
rate_as_str = input('Оцените работу от 1 до 5:')
rate = int(rate_as_str)

# проверить, что оценка от 1 до 5
if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

print(rate)
# в зависимости от оценки предложить дать обратную связь

feedback = ''

if rate == 1 or 2:
    feedback = input('расскажите что нам улучшить')
#else:
 #   if rate == 2:
  #      feedback = input('расскажите что Вас смутило')

print(feedback)