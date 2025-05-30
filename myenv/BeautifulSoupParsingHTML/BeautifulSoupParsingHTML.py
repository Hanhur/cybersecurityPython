# ========================================================================================================================
# Парсинг (или анализ) данных - это процесс извлечения инфор­мации из различных источников, таких как веб-страницы, доку­менты, файлы или API. 
# Веб-парсинг, в частности, сосредоточен на извлечении данных из НТМL-кода веб-страниц. 
# Для успеш­ного выполнения этой задачи необходимо обладать знаниями в следующих областях.
# =========================================================================================================================

# BeautifulSoup - это библиотека Python, предназначенная для парсинга HTML- и ХМL-документов. 
# Она предоставляет удобные методы для извлечения данных из НТМL-страниц, облегчая работу с веб-контентом и анализ его структуры.

# pip install beautifulsoup4 requests

# Пример парсинга НТМL-документа:

import requests
from bs4 import BeautifulSoup

# Загрузка НТМL-страницы
url = 'http://example.com'
response = requests.get(url)

# Создание объекта BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Вывод отформатированного HTML
print(soup.prettify())

# Пример извлечения данных:

# Извлечение заголовка страницы
title = soup.title.string
print(f"Title: {title}")

# Извлечение всех ссылок на странице
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# Пример навигации по дереву элементов:

# Извлечение первого параграфа и его текста
first_paragraph = soup.find( 'p')
print(first_paragraph.text)

# Извлечение родительского элемента
parent = first_paragraph.parent
print(parent.narne)

# Извлечение всех дочерних элементов
children = first_paragraph.findChildren()
for child in children:
    print(child.narne)

# Извлечение следующего и предыдущего элемента
next_siЫing = first_paragraph.find_next_siЫing()
previous_siЫing = first_paragraph.find_previous_siЫing()
print(f"Next sibling: {next_sibling}")
print(f"Previous sibling: {previous_sibling}")

# Допустим, у нас есть следующая НТМL-страница:
# <!DOCTYPE htrnl>
# <htrnl lang="en">
# <head>
#     <meta charset= "UTF-8">
#     <title>Exarnple Page</title>
# </head>
# <body>
#     <hl>Welcorne to Exarnple.corn</hl>
#     <р class= "description">This is an exarnple page.</p>
#     <а href = "http://exarnple.com/pagel">Page 1</а>
#     <а href = "http://exarnple.com/page2">Page 2</а>
#     <а href="http://exarnple.com/page3">Page 3</а>
# </body>
# </htrnl>

# Парсинг страницы с BeautifulSoup
import requests
from bs4 import BeautifulSoup

# Загрузка НТМL-страницы
url = 'http://example.com'
response = requests.get(url)

# Соэдание объекта BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение заголовка страницы
title = soup.title.string
print(f"Title: {title}")

# Извлечение заголовка Hl
hl = soup.finct('h1') .text
print(f"H1: {h1}")

# Извлечение параграфа с классом description
description = soup.find('p', class_ = 'description').text
print(f"Description: {description}")

# Извлечение всех ссылок на странице
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.text
    print(f"Link text: {text}, URL: {href}")


# Пример использования Beautiful Soup для извлечения заголовков новостей с веб-страницы
import requests
from bs4 import BeautifulSoup

# Загрузка НТМL-страницы
url = 'https://example.com'
response = requests.get(url)

# Соэдание объекта Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение заголовков новостей
headlines = soup.find_all('h2', class_ = 'news-headline')

# Вывод заголовков
for headline in headlines:
    print(headline.text)


# Предположим, что у нас уже есть объект soup, представляющий НТМL-документ
headlines = soup.find_all('h2')
for headline in headlines:
    print(headline.text)


# Предположим, что у нас уже есть объект soup, представляющий НТМL-документ
table = soup.find('table', class_ = 'data-table')
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        print(cell.text)


# Предположим, что у нас уже есть объект soup, представляющий НТМL-документ
navigation_menu = soup.find( 'ul', class_ = 'nav-menu')
links = navigation_menu.find_all('a')
for link in links:
    print(link. get( 'href'))


# Предположим, что у нас уже есть объект soup, представляющий НТМL-документ
elements_with_class = soup. find_all(class_ = 'highlighted')
for element in elements_with_class:
    print(element.text)


# Предположим, что у нас уже есть объект soup, представляющий НТМL-документ
element_with_id = soup.find(id = 'content')
print(element_with_id.text)


# Предположим, что у нас уже есть объект soup, представляющий НТМL-документ
elements_with_href = soup.find_all (href = True)
for element in elements_with_href:
    print(element['href'])


# Предположим, что у нас уже есть объект soup, представляющий НТМL-документ
elements_with_text = soup.find_all(text = 'Hello')
for element in elements_with_text:
    print(element.parent.name) # Вывести имя родительского тега


import re
# Поиск всех элементов, у которых атрибут class начинается с 'highlight'
elements = soup.find_all(class_ = re.compile('^highlight'))


# Парсинг НТМL-кода веб-страницы с использованием BeautifulSoup
from bs4 import BeautifulSoup
import requests

# Получаем НТМL-код веб-страницы
response = requests.get("https://example.com")
html_content = response.text

# Инициализируем объект BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Находим все ссылки на странице и выводим их
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# ===========================================================================================================================

# Установка необходимых библиотек pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def extract_news_headlines(url, selector):
    """
    Извлекает заголовки новостей с указанного URL.
    
    Параметры:
        url (str): URL веб-страницы с новостями
        selector (str): CSS-селектор для поиска заголовков
        
    Возвращает:
        list: Список заголовков новостей
    """
    try:
        # Отправляем GET-запрос к веб-странице
        response = requests.get(url, timeout = 10)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим все элементы, соответствующие селектору
        headlines = soup.select(selector)
        
        # Извлекаем текст из каждого элемента и очищаем его
        cleaned_headlines = [h.get_text().strip() for h in headlines if h.get_text().strip()]
        
        return cleaned_headlines
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

# Пример использования
if __name__ == "__main__":
    # URL новостного сайта (пример с BBC News)
    news_url = "https://www.bbc.com/news"
    
    # CSS-селектор для заголовков (может отличаться для разных сайтов)
    # Это пример для BBC News, для других сайтов нужно определить правильный селектор
    headline_selector = "h3.gs-c-promo-heading__title"
    
    # Извлекаем заголовки
    headlines = extract_news_headlines(news_url, headline_selector)
    
    # Выводим результат
    print(f"Найдено {len(headlines)} заголовков новостей с {news_url}:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")

# ===================================================================================================================================

# Установите зависимости: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def get_product_data(url, product_selector, price_selector, discount_selector = None):
    """
    Получает данные о товарах с веб-страницы интернет-магазина.
    
    Параметры:
        url (str): URL страницы с товарами
        product_selector (str): CSS-селектор для названий товаров
        price_selector (str): CSS-селектор для цен
        discount_selector (str, optional): CSS-селектор для скидок
        
    Возвращает:
        list: Список словарей с информацией о товарах
    """
    try:
        # Заголовки для имитации браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Отправляем GET-запрос
        response = requests.get(url, headers = headers, timeout = 10)
        response.raise_for_status()
        
        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        products = []
        
        # Находим все элементы товаров (обычно они находятся в общем контейнере)
        product_items = soup.select(product_selector['container']) if isinstance(product_selector, dict) else soup.select(product_selector)
        
        for item in product_items:
            product_data = {}
            
            # Извлекаем название товара
            if isinstance(product_selector, dict):
                name_elem = item.select_one(product_selector['name'])
            else:
                name_elem = item.select_one('a > span') or item  # fallback
            
            product_data['name'] = name_elem.get_text(strip = True) if name_elem else 'Нет названия'
            
            # Извлекаем цену
            price_elem = item.select_one(price_selector)
            if price_elem:
                price_text = price_elem.get_text(strip = True)
                # Извлекаем числа из текста цены
                price = float(re.sub(r'[^\d.,]', '', price_text).replace(',', '.'))
                product_data['price'] = price
            else:
                product_data['price'] = None
            
            # Извлекаем скидку (если указан селектор)
            if discount_selector:
                discount_elem = item.select_one(discount_selector)
                if discount_elem:
                    discount_text = discount_elem.get_text(strip = True)
                    # Извлекаем числа из текста скидки
                    discount = float(re.sub(r'[^\d.,]', '', discount_text).replace(',', '.'))
                    product_data['discount'] = discount
                else:
                    product_data['discount'] = None
                
                # Рассчитываем старую цену, если есть скидка
                if product_data['discount'] and product_data['price']:
                    product_data['old_price'] = round(product_data['price'] / (1 - product_data['discount'] / 100), 2)
                else:
                    product_data['old_price'] = None
            
            # Извлекаем ссылку на товар
            link_elem = item.find('a')
            if link_elem and 'href' in link_elem.attrs:
                product_data['url'] = urljoin(url, link_elem['href'])
            else:
                product_data['url'] = None
            
            products.append(product_data)
        
        return products
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

def analyze_prices(products):
    """Анализирует цены товаров и выводит статистику"""
    if not products:
        print("Нет данных для анализа")
        return
    
    prices = [p['price'] for p in products if p['price'] is not None]
    
    if prices:
        avg_price = sum(prices) / len(prices)
        min_price = min(prices)
        max_price = max(prices)
        
        print("\nАнализ цен:")
        print(f"Всего товаров: {len(products)}")
        print(f"Средняя цена: {avg_price:.2f}")
        print(f"Минимальная цена: {min_price:.2f}")
        print(f"Максимальная цена: {max_price:.2f}")
        
        # Товары со скидкой
        discounted = [p for p in products if p.get('discount')]
        if discounted:
            avg_discount = sum(p['discount'] for p in discounted) / len(discounted)
            print(f"\nТоваров со скидкой: {len(discounted)}")
            print(f"Средний размер скидки: {avg_discount:.1f}%")
            
            # Топ-3 самых выгодных предложений
            discounted_sorted = sorted(discounted, key = lambda x: x['discount'], reverse = True)[:3]
            print("\nТоп-3 самых выгодных предложений:")
            for i, product in enumerate(discounted_sorted, 1):
                print(f"{i}. {product['name']} - {product['price']:.2f} (скидка {product['discount']}%, было {product['old_price']:.2f})")

if __name__ == "__main__":
    # Пример для Wildberries (селекторы могут измениться!)
    wb_url = "https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki"
    wb_selectors = {
        'container': '.product-card',
        'name': '.product-card__name',
        'price': '.price__lower-price',
        'discount': '.product-card__sale'
    }
    
    print("Парсим данные с Wildberries...")
    wb_products = get_product_data(wb_url, wb_selectors, wb_selectors['price'], wb_selectors['discount'])
    
    # Выводим первые 5 товаров для проверки
    print("\nПервые 5 товаров:")
    for i, product in enumerate(wb_products[:5], 1):
        print(f"{i}. {product['name']} - {product['price']:.2f} руб." +  (f" (скидка {product['discount']}%)" if product.get('discount') else ""))
    
    # Анализируем цены
    analyze_prices(wb_products)

# ======================================================================================================================================================

# Установите зависимости: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import json

def extract_table_data(url, table_selector = None, output_format = 'list', include_headers = True):
    """
    Извлекает данные из таблицы на веб-странице.
    
    Параметры:
        url (str): URL веб-страницы с таблицей
        table_selector (str): CSS-селектор для таблицы (если None, берется первая таблица на странице)
        output_format (str): Формат вывода ('list', 'dict' или 'json')
        include_headers (bool): Включать ли заголовки в результат
        
    Возвращает:
        Данные таблицы в указанном формате
    """
    try:
        # Заголовки для имитации браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Отправляем GET-запрос
        response = requests.get(url, headers = headers, timeout = 10)
        response.raise_for_status()
        
        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим таблицу
        if table_selector:
            table = soup.select_one(table_selector)
        else:
            table = soup.find('table')
            
        if not table:
            raise ValueError("Таблица не найдена на странице")
        
        # Извлекаем заголовки (если есть)
        headers = []
        if include_headers:
            header_rows = table.find_all('th')
            headers = [th.get_text(strip = True) for th in header_rows]
            if not headers:  # если нет th, попробуем взять первую строку
                first_row = table.find('tr')
                if first_row:
                    headers = [td.get_text(strip = True) for td in first_row.find_all('td')]
        
        # Извлекаем данные таблицы
        data = []
        rows = table.find_all('tr')
        
        for row in rows:
            # Пропускаем строку, если она содержит только заголовки
            if row.find('th') and not row.find('td'):
                continue
                
            cells = row.find_all(['td', 'th'])
            row_data = [cell.get_text(strip = True) for cell in cells]
            
            # Обрабатываем ячейки с colspan
            for i, cell in enumerate(cells):
                if 'colspan' in cell.attrs:
                    colspan = int(cell['colspan'])
                    if colspan > 1:
                        # Вставляем пустые значения для объединенных ячеек
                        for _ in range(1, colspan):
                            row_data.insert(i + 1, '')
            
            if row_data:
                data.append(row_data)
        
        # Преобразуем в нужный формат
        if output_format == 'dict' and headers:
            result = []
            for row in data:
                if len(row) == len(headers):
                    result.append(dict(zip(headers, row)))
                elif len(row) > len(headers):
                    # Если данных больше чем заголовков, добавляем недостающие заголовки
                    extended_headers = headers + [f'Column_{i}' for i in range(len(headers), len(row))]
                    result.append(dict(zip(extended_headers, row)))
                else:
                    # Если данных меньше чем заголовков, обрезаем заголовки
                    result.append(dict(zip(headers[:len(row)], row)))
            return result
        elif output_format == 'json':
            if headers:
                dict_data = []
                for row in data:
                    if len(row) == len(headers):
                        dict_data.append(dict(zip(headers, row)))
                return json.dumps(dict_data, ensure_ascii = False, indent = 2)
            else:
                return json.dumps(data, ensure_ascii = False, indent = 2)
        else:
            if include_headers and headers:
                return [headers] + data
            return data
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def save_to_csv(data, filename):
    """Сохраняет данные таблицы в CSV файл"""
    with open(filename, 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Данные сохранены в {filename}")

def save_to_json(data, filename):
    """Сохраняет данные таблицы в JSON файл"""
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent = 2)
    print(f"Данные сохранены в {filename}")

if __name__ == "__main__":
    # Пример использования
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    table_selector = "table.wikitable"
    
    print(f"Извлекаем таблицу с {url}...")
    table_data = extract_table_data(url, table_selector, output_format = 'dict')
    
    if table_data:
        # Выводим первые 5 строк для демонстрации
        print("\nПервые 5 строк таблицы:")
        for i, row in enumerate(table_data[:5], 1):
            print(f"{i}. {row}")
        
        # Сохраняем в файлы
        save_to_csv([[row.get(k, '') for k in table_data[0].keys()] for row in table_data], 'table_data.csv')
        save_to_json(table_data, 'table_data.json')
    else:
        print("Не удалось извлечь данные таблицы")

# =====================================================================================================================================================

# Универсальный скрипт для парсинга веб-страниц с сохранением в CSV/JSON
# Установите зависимости: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
import json
import os
from urllib.parse import urljoin

def parse_website(url, config):
    """
    Парсит данные с веб-страницы согласно конфигурации
    
    :param url: URL целевой страницы
    :param config: Словарь с настройками парсинга
    :return: Список словарей с извлеченными данными
    """
    try:
        # Заголовки для имитации браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Загружаем страницу
        response = requests.get(url, headers = headers, timeout = 15)
        response.raise_for_status()
        
        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим контейнеры с данными
        items = soup.select(config['container_selector'])
        if not items:
            raise ValueError("Не найдены элементы по указанному селектору")
        
        extracted_data = []
        
        # Извлекаем данные из каждого элемента
        for item in items:
            data = {}
            for field in config['fields']:
                element = item.select_one(field['selector'])
                if element:
                    # Обрабатываем разные типы данных
                    if field.get('attribute'):
                        value = element.get(field['attribute'])
                    else:
                        value = element.get_text(strip = True)
                    
                    # Применяем кастомную обработку если есть
                    if field.get('processor'):
                        value = field['processor'](value)
                    
                    data[field['name']] = value
                else:
                    data[field['name']] = None
            
            # Добавляем URL если требуется
            if config.get('include_url'):
                link = item.find('a')
                if link and 'href' in link.attrs:
                    data['url'] = urljoin(url, link['href'])
                else:
                    data['url'] = None
            
            extracted_data.append(data)
        
        return extracted_data
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return None
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return None

def save_to_csv(data, filename):
    """Сохраняет данные в CSV файл"""
    if not data:
        return False
    
    try:
        os.makedirs(os.path.dirname(filename), exist_ok = True)
        
        with open(filename, 'w', newline = '', encoding = 'utf-8') as file:
            writer = csv.DictWriter(file, fieldnames = data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Данные успешно сохранены в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")
        return False

def save_to_json(data, filename):
    """Сохраняет данные в JSON файл"""
    if not data:
        return False
    
    try:
        os.makedirs(os.path.dirname(filename), exist_ok = True)
        
        with open(filename, 'w', encoding = 'utf-8') as file:
            json.dump(data, file, ensure_ascii = False, indent = 2)
        
        print(f"Данные успешно сохранены в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении в JSON: {e}")
        return False

if __name__ == "__main__":
    # Конфигурация парсера для примера (новости с BBC)
    CONFIG = {
        'container_selector': '.gs-c-promo',
        'include_url': True,
        'fields': [
            {
                'name': 'title',
                'selector': '.gs-c-promo-heading__title',
                'processor': lambda x: x.strip() if x else None
            },
            {
                'name': 'summary',
                'selector': '.gs-c-promo-summary',
                'processor': lambda x: x.strip() if x else None
            },
            {
                'name': 'time',
                'selector': 'time',
                'attribute': 'datetime'
            }
        ]
    }
    
    # URL для парсинга
    TARGET_URL = "https://www.bbc.com/news"
    
    # Парсим данные
    print(f"Парсим данные с {TARGET_URL}...")
    parsed_data = parse_website(TARGET_URL, CONFIG)
    
    if parsed_data:
        # Выводим первые 3 записи для примера
        print("\nПервые 3 записи:")
        for i, item in enumerate(parsed_data[:3], 1):
            print(f"{i}. {item}")
        
        # Сохраняем в файлы
        save_to_csv(parsed_data, 'output/data.csv')
        save_to_json(parsed_data, 'output/data.json')
    else:
        print("Не удалось получить данные")

# Парсинг товаров с Amazon
CONFIG = {
    'container_selector': '.s-result-item',
    'include_url': True,
    'fields': [
        {
            'name': 'name',
            'selector': 'h2 a span',
            'processor': lambda x: x.strip() if x else None
        },
        {
            'name': 'price',
            'selector': '.a-price .a-offscreen',
            'processor': lambda x: float(x.replace('$', '').replace(',', '')) if x else None
        },
        {
            'name': 'rating',
            'selector': '.a-icon-star-small .a-icon-alt',
            'processor': lambda x: float(x.split()[0]) if x else None
        }
    ]
}

#  Парсинг вакансий с HH.ru
CONFIG = {
    'container_selector': '.vacancy-serp-item',
    'include_url': True,
    'fields': [
        {
            'name': 'title',
            'selector': '.resume-search-item__name',
            'processor': lambda x: x.strip() if x else None
        },
        {
            'name': 'company',
            'selector': '.vacancy-serp-item__meta-info-company',
            'processor': lambda x: x.strip() if x else None
        },
        {
            'name': 'salary',
            'selector': '.vacancy-serp-item__compensation',
            'processor': lambda x: x.strip() if x else None
        },
        {
            'name': 'location',
            'selector': '.vacancy-serp-item__meta-info',
            'processor': lambda x: x.get_text(', ', strip = True) if x else None
        } 
    ]
}

# =======================================================================================================================================================

# Установите зависимости: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import hashlib
import time
import smtplib
from email.mime.text import MIMEText
import difflib
import json
import os
from datetime import datetime

class WebPageMonitor:
    def __init__(self, config_file = 'config.json'):
        self.config = self.load_config(config_file)
        self.history_file = 'page_history.json'
        self.page_history = self.load_history()
        
    def load_config(self, config_file):
        """Загружает конфигурацию из JSON файла"""
        default_config = {
            "url": "https://example.com",
            "check_interval": 3600,  # секунды
            "notification_email": "your@email.com",
            "smtp_server": "smtp.example.com",
            "smtp_port": 587,
            "smtp_username": "your@email.com",
            "smtp_password": "yourpassword",
            "ignore_selectors": [".advertisement", ".counter"],  # Элементы, которые игнорируются
            "watch_selectors": None,  # Специфичные элементы для мониторинга (None для всей страницы)
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                # Объединяем с дефолтными значениями
                return {**default_config, **config}
        except FileNotFoundError:
            print(f"Конфиг файл {config_file} не найден, используем настройки по умолчанию")
            return default_config
        except json.JSONDecodeError:
            print(f"Ошибка в формате {config_file}, используем настройки по умолчанию")
            return default_config
    
    def load_history(self):
        """Загружает историю изменений из файла"""
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_history(self):
        """Сохраняет историю изменений в файл"""
        with open(self.history_file, 'w') as f:
            json.dump(self.page_history, f, indent = 2)
    
    def fetch_page(self):
        """Загружает веб-страницу"""
        headers = {'User-Agent': self.config['user_agent']}
        try:
            response = requests.get(self.config['url'], headers = headers, timeout = 30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Ошибка при загрузке страницы: {e}")
            return None
    
    def process_content(self, html):
        """Обрабатывает HTML, извлекая только важные части"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Удаляем элементы, которые нужно игнорировать
        if self.config['ignore_selectors']:
            for selector in self.config['ignore_selectors']:
                for element in soup.select(selector):
                    element.decompose()
        
        # Если указаны специфичные селекторы, извлекаем только их
        if self.config['watch_selectors']:
            content = []
            for selector in self.config['watch_selectors']:
                elements = soup.select(selector)
                content.extend(str(e) for e in elements)
            return '\n'.join(content)
        
        return str(soup)
    
    def get_page_hash(self, content):
        """Генерирует хеш для содержимого страницы"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def compare_content(self, old_content, new_content):
        """Сравнивает две версии контента и возвращает различия"""
        diff = difflib.unified_diff(
            old_content.splitlines(keepends = True),
            new_content.splitlines(keepends = True),
            fromfile = 'old',
            tofile = 'new',
            n = 3
        )
        return ''.join(diff)
    
    def send_notification(self, subject, message):
        """Отправляет email уведомление"""
        if not self.config['notification_email']:
            print("Email уведомления отключены в конфигурации")
            return
        
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = self.config['smtp_username']
        msg['To'] = self.config['notification_email']
        
        try:
            with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
                server.starttls()
                server.login(self.config['smtp_username'], self.config['smtp_password'])
                server.send_message(msg)
            print("Уведомление отправлено")
        except Exception as e:
            print(f"Ошибка при отправке уведомления: {e}")
    
    def check_for_changes(self):
        """Проверяет страницу на изменения"""
        print(f"\nПроверяем {self.config['url']} в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Загружаем страницу
        html = self.fetch_page()
        if not html:
            return
        
        # Обрабатываем контент
        processed_content = self.process_content(html)
        current_hash = self.get_page_hash(processed_content)
        
        # Проверяем, есть ли предыдущая версия
        if self.config['url'] in self.page_history:
            last_hash = self.page_history[self.config['url']]['hash']
            last_content = self.page_history[self.config['url']]['content']
            
            if current_hash != last_hash:
                print("Обнаружены изменения!")
                diff = self.compare_content(last_content, processed_content)
                
                # Сохраняем diff в файл
                diff_filename = f"diffs/diff_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                os.makedirs('diffs', exist_ok = True)
                with open(diff_filename, 'w', encoding = 'utf-8') as f:
                    f.write(diff)
                
                # Отправляем уведомление
                subject = f"Обнаружены изменения на {self.config['url']}"
                message = f"На странице {self.config['url']} обнаружены изменения.\n\n" \
                          f"Сравнение изменений сохранено в {diff_filename}\n\n" \
                          f"Для просмотра изменений выполните:\n" \
                          f"cat {diff_filename}"
                self.send_notification(subject, message)
            else:
                print("Изменений не обнаружено")
        else:
            print("Первая проверка, сохраняем базовую версию")
        
        # Обновляем историю
        self.page_history[self.config['url']] = {
            'hash': current_hash,
            'content': processed_content,
            'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.save_history()
    
    def run(self):
        """Запускает мониторинг с заданным интервалом"""
        print(f"Запуск мониторинга {self.config['url']}")
        print(f"Интервал проверки: {self.config['check_interval']} секунд")
        print("Нажмите Ctrl+C для остановки")
        
        try:
            while True:
                self.check_for_changes()
                time.sleep(self.config['check_interval'])
        except KeyboardInterrupt:
            print("\nМониторинг остановлен")

if __name__ == "__main__":
    monitor = WebPageMonitor()
    monitor.run()

# Создайте конфигурационный файл config.json:
{
    "url": "https://example.com",
    "check_interval": 600,
    "notification_email": "your@email.com",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "smtp_username": "your@gmail.com",
    "smtp_password": "yourpassword",
    "ignore_selectors": [".ad", ".counter", ".footer"],
    "watch_selectors": ["#main-content", ".news-item"]
}

# Telegram/SMS уведомления:
def send_telegram_notification(self, message):
    import telegram
    bot = telegram.Bot(token = "YOUR_TELEGRAM_BOT_TOKEN")
    bot.send_message(chat_id = "YOUR_CHAT_ID", text = message)

# Распознавание значимых изменений:
def is_significant_change(self, diff):
    # Игнорировать изменения в цифрах, датах и т.д.
    lines = diff.split('\n')
    added = sum(1 for line in lines if line.startswith('+') and not line.startswith('+++'))
    deleted = sum(1 for line in lines if line.startswith('-') and not line.startswith('---'))
    return added + deleted > 5  # Пример: минимум 5 изменений


# ======================================================= САРТСНА =======================================================

# САРТСНА используется для предотвращения автоматизированных дей­ствий, таких как спам-регистрации, автоматическое создание учетных запи­сей, 
# спам-комментарии и другие формы злоупотреблений на веб-сайтах.

# Пример использования 2Captcha с библиотекой requests в Python
import requests

АРI_КЕУ = 'YOUR_2САРТСНА_АРI_КЕУ'
САРТСНА_SITE_КЕУ = 'SITE_КЕУ_FROM_САРТСНА'
URL = 'URL_OF_ТНЕ_SITE_WITH_САРТСНА'

# Шаг 1: Отправка запроса на решение САРТСНА
captcha_id = requests.post(
    'http://2captcha.com/in.php',
    data = {'key': API_KEY, 'method': 'userrecaptcha', 'googlekey': CAPTCHA_SITE_KEY, 'pageurl': URL}).text.split(' 1 ') [ 1]

# Шаг 2: Ожидание и получение ответа САРТСНА
captcha_solution = ''
while True:
    response = requests.get(f'http://2captcha.com/res.php?key={API_KEY}&action=get&id={captcha_id}').text
    if response == 'CAPCHA_NOT_READY':
        time.sleep(5)
        continue
    if 'OK' in response:
        captcha_solution = response.split(' 1 ') [ 1]
        break

# Шаг 3: Использование решения САРТСНА для отправки запроса на сайт
response = requests.post(URL, data = {'g-recaptcha-response':captcha_solution})
print(response.content)

# код для отправки САРТСНА и получения результата
import requests
import time

API_KEY = 'your_2captcha_api_key'
CAPTCHA_SITE_KEY = 'site_key_of_the captcha'
URL = 'url of_the_page_with_captcha'

# Отправка запроса на решение reCAPTCHA
def solve_recaptcha(api_key, site_key, url):
    payload = {
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url
    }
    response = requests.post('http://2captcha.com/in.php', data = payload)
    request_id = response.text.split(' 1 ') [1]

    # Ожидание решения САРТСНА
    time.sleep(20)
    while True:
        result = requests.get(f'http://2captcha.com/res.php?key={api_key}&action= get&id= {request_id} ')
        if result.text == 'САРСНА NOT READY':
            time.sleep(5)
        else:
            break
    return result.text.split(' 1 ') (1)

captcha_solution = solve_recaptcha(API_KEY, CAPTCHA_SITE_KEY, URL)
print(f'ReCAPTCHA solution: {captcha_solution}')

# пример использования Selenium на Python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Настройка веб-драйвера
driver = webdriver.Chrome()

# Открытие веб-страницы
driver.get('https://example.com')

# Имитация случайных движений МЬШIИ
def move_mouse_randomly():
    for _ in range(random.randint(5, 10)):
        action = webdriver.ActionChains(driver)
        action.move_by_offset(random.randint(-10, 10), random.
        randint(-10, 10)).perform()
    time.sleep(random.uniform(0.1, 0.5))

# Имитация ввода текста
search_box = driver.find_element_by_name( 'q')
search_box.click()
move_mouse_randomly()
query = "Selenium Python"
for char in query:
    search_box.send_keys(char)
    time.sleep(random.uniform(0.1, 0.3))

search_box.send_keys(Keys.RETURN)

# Закрытие веб-драйвера
time.sleep(5)
driver.quit()