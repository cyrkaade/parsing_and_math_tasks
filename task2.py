# 2
import time

import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0' \
      '%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83 '

# Для расчета суммы животных для каждой буквы алфавита.
counting = 0

# Все буквы которые встречаются в сайте
alphabet_lst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
                'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']

# Используем цикл while (до тех пор пока не дойдем до последней страницы)
while url is not None:
    page = requests.get(url)
    lst = []

    # Используем модуль beautifulsoup для parsing
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="mw-pages")
    names = results.find_all('a')

    # Проходимся по всем <a> тегам.
    for name in names:
        if name.text == 'Следующая страница':
            continue
        elif name.text == 'Предыдущая страница':
            continue
        # Проверяем на ошибки с сайта (там есть имена животных которые по идее начинаются на букву, по которой мы
        # собираем информацию, однако используют синонимы). Из-за этого нужно предусмотреть данную ситуацию с
        # условием.
        if len(alphabet_lst) > 2:
            if str(name.text[0]) != alphabet_lst[0]:
                if str(name.text[0]) != alphabet_lst[1]:
                    counting += 1
                    continue
        if len(alphabet_lst) != 0:
            # Проверяем на совпадение первой буквы слова и буквы в алфавите.
            if str(name.text[0]) != alphabet_lst[0]:
                print(f'{alphabet_lst[0]}: {counting}')
                alphabet_lst.pop(0)
                counting = 0
        else:
            # Завершаем программу после последней буквы.
            time.sleep(2)
            raise StopIteration('That\'s all')

        counting += 1

    # Берем аттрибут с href чтобы парсить следующие 200 имен животных.
        url = 'https://ru.wikipedia.org/' + names[-1].get('href')
