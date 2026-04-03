from bs4 import BeautifulSoup
import re

# Содержимое файла DetailedStatement5030.htm (переменная html_content)
# или чтение из файла:
with open('DetailedStatement5030.htm', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')
results = {}

i = 0
while i < len(rows):
    row = rows[i]
    cells = row.find_all('td')
    # Ищем строку сделки: должно быть не менее 14 ячеек, и тип 'buy' или 'sell'
    if len(cells) >= 14 and cells[2].get_text(strip=True) in ('buy', 'sell'):
        # Извлекаем commission и profit
        commission = float(cells[10].get_text(strip=True).replace(',', ''))
        profit = float(cells[13].get_text(strip=True).replace(',', ''))
        net = commission + profit
        # Следующая строка содержит Magic и имя бота
        if i+1 < len(rows):
            next_cells = rows[i+1].find_all('td')
            if len(next_cells) >= 4 and next_cells[1].get_text(strip=True).isdigit():
                magic = int(next_cells[1].get_text(strip=True))
                bot_name = next_cells[3].get_text(strip=True)
                results[magic] = results.get(magic, 0) + net
        i += 2  # пропускаем строку с пояснением
    else:
        i += 1

print("Доход по ботам (чистый результат с учётом комиссии):")
for magic, net in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"Magic {magic} ({bot_names.get(magic, '?')}): {net:.2f} USD")
