def is_year_leap(year):
    return 'True' if year % 4 == 0 else 'False'


numb = int(input('Введите год '))
answer = is_year_leap(numb)
print(f'год {numb}: {answer}')
