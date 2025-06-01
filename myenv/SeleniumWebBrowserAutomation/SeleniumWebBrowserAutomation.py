# ============================================================================================================================
# Selenium - это мощный инструмент для автоматизации действий веб-браузера. Он позволяет программно управлять браузером, 
# открывать веб-страницы, заполнять формы, кликать по элементам, извлекать данные и многое другое.
# =============================================================================================================================

# pip install selenium

# Пример открытия браузера
from selenium import webdriver

# Запуск браузера (например, Chrome)
driver = webdriver.Chrome('/path/to/chromedriver')

# Загрузка веб-страницы
driver.get('https://www.example.com')

# Поиск элемента по id'
element = driver.find_element_by_id ('username')

# Поиск элемента по имени класса
elements = driver.find_elements_by_class_name('btn-primary')

# Ввод текста в поле ввода
element.send_keys('John Doe')

# Клик по кнопке
element.click()

# Извлечение текста элемента
text = element.text

# Извлечение значения атрибута
value = element.get_attribute('href')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ЕС

# Ожидание появления элемента
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))

# Пример
from selenium import webdriver

# Запуск браузера
driver = webdriver.Chrome('/path/to/chromedriver')

# Загрузка страницы для входа
driver.get('https://example.com/login')

# Находим поля ввода и кнопку входа
username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')
login_button = driver.find_element_by_id('login_button')

# Вводим данные и нажимаем кнопку входа
username_input.send_keys('my_username')
password_input.send_keys('my_password')
login_button.click()

# Пример 2
from selenium import webdriver
import time

# Запуск браузера
driver = webdriver.Chrome('/path/to/chromedriver')

# Загрузка страницы
driver.get('https://example.com/users')

# Прокрутка страницы вниз
for i in range(З):
    driver.execute_script("window.scrollTo(O, document.body.scrollHeight); ")
    time.sleep(2) # Пауза для загрузки дополнительных данных

# Извлечение данных о пользователях
users = driver.find_elements_by_class_name('user-info')
for user in users:
    print(user.text)

# Пример 3
from selenium import webdriver

# Запуск браузера
driver = webdriver.Chrome('/path/to/chromedriver')

# Загрузка страницы веб-приложения
driver.get('https://example.com/new_post')

# Находим поля ввода для заголовка и содержимого записи
title_input = driver.find_element_by_id('title')
content_input = driver.find_element_by_id( 'content')
submit_button = driver.find_element_by_id('submit')

# Вводим данные и отправляем форму
title_input.send_keys('Hoвaя запись')
content_input.send_keys('Coдepжимoe новой записи')
submit_button.click()

# Пример 4
import unittest
from selenium import webdriver

class TestApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/path/to/chromedriver')
    def test_login(self):
        self.driver.get('https://example.com/login')

    # Здесь проводите тестирование входа на сайт
    def test_create_post(self):
        self.driver.get('https: //exarnple. corn/new_post')

    # Здесь проводите тестирование создания новой записи
    def tearDown(self):
        self.driver.quit()

if __name__== "__main__":
    unittest.rnain()

# ==================================================================================================================================

# Программа для автоматизации поиска в Google с использованием Selenium
# Установите необходимые библиотеки: pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def google_search(query):
    # Настройка Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Режим без графического интерфейса
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Укажите путь к вашему chromedriver
    service = Service('путь/к/chromedriver')  # Замените на актуальный путь
    
    # Инициализация драйвера
    driver = webdriver.Chrome(service = service, options = chrome_options)
    
    try:
        # Открытие Google
        driver.get("https://www.google.com")
        
        # Поиск поля ввода
        search_box = driver.find_element(By.NAME, "q")
        
        # Ввод поискового запроса
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Ждем загрузки результатов
        time.sleep(2)
        
        # Получение результатов поиска
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        
        # Вывод результатов на экран
        print(f"Результаты поиска для запроса '{query}':\n")
        for i, result in enumerate(results[:5], 1):  # Выводим первые 5 результатов
            try:
                title = result.find_element(By.CSS_SELECTOR, "h3").text
                link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                snippet = result.find_element(By.CSS_SELECTOR, "div.IsZvec").text
                
                print(f"{i}. {title}")
                print(f"   Ссылка: {link}")
                print(f"   Описание: {snippet}\n")
            except Exception as e:
                print(f"Не удалось извлечь данные для результата {i}: {e}")
                continue
        
    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    search_query = input("Введите поисковый запрос: ")
    google_search(search_query)

# Альтернативная версия с автоматической загрузкой драйвера:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def google_search(query):
    # Настройка Chrome WebDriver с автоматической загрузкой драйвера
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    
    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        
        # Вывод HTML страницы с результатами
        print(driver.page_source)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    search_query = input("Введите поисковый запрос: ")
    google_search(search_query)

# ===============================================================================================================================

# Скрипт автоматизации регистрации на веб-сайте
# Установите необходимые зависимости: pip install selenium webdriver-manager
# Запустите скрипт: python registration_script.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

def generate_random_email():
    """Генерация случайного email"""
    username = ''.join(random.choices(string.ascii_lowercase, k = 8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com'])
    return f"{username}@{domain}"

def generate_random_phone():
    """Генерация случайного номера телефона"""
    return ''.join(random.choices(string.digits, k = 10))

def automate_registration():
    # Настройка драйвера
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Открытие страницы регистрации
        driver.get("https://demoqa.com/automation-practice-form")
        time.sleep(2)
        
        # Заполнение полей формы
        # Личная информация
        first_name = driver.find_element(By.ID, "firstName")
        first_name.send_keys("Иван")
        
        last_name = driver.find_element(By.ID, "lastName")
        last_name.send_keys("Петров")
        
        email = driver.find_element(By.ID, "userEmail")
        email.send_keys(generate_random_email())
        
        gender = driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
        gender.click()
        
        phone = driver.find_element(By.ID, "userNumber")
        phone.send_keys(generate_random_phone())
        
        # Дата рождения
        dob = driver.find_element(By.ID, "dateOfBirthInput")
        dob.click()
        
        month_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_select.select_by_value("4")  # Май
        
        year_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_select.select_by_value("1990")
        
        day = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--015")
        day.click()
        
        # Предметы
        subjects = driver.find_element(By.ID, "subjectsInput")
        subjects.send_keys("Maths")
        subjects.send_keys(Keys.RETURN)
        
        # Хобби
        hobby = driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]")
        hobby.click()
        
        # Загрузка изображения
        picture = driver.find_element(By.ID, "uploadPicture")
        picture.send_keys("/путь/к/тестовому/изображению.jpg")  # Замените на реальный путь
        
        # Адрес
        address = driver.find_element(By.ID, "currentAddress")
        address.send_keys("ул. Примерная, д. 123, кв. 45")
        
        # Выбор штата и города
        state = driver.find_element(By.ID, "state")
        state.click()
        state_option = driver.find_element(By.ID, "react-select-3-option-0")
        state_option.click()
        
        city = driver.find_element(By.ID, "city")
        city.click()
        city_option = driver.find_element(By.ID, "react-select-4-option-0")
        city_option.click()
        
        # Отправка формы
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        
        # Проверка успешной регистрации
        time.sleep(2)
        success_message = driver.find_element(By.ID, "example-modal-sizes-title-lg")
        if success_message.text == "Thanks for submitting the form":
            print("Регистрация прошла успешно!")
        else:
            print("Что-то пошло не так при регистрации")
            
        # Можно добавить сохранение скриншота
        driver.save_screenshot("registration_result.png")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        driver.save_screenshot("error_screenshot.png")
        
    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    automate_registration()

# ===========================================================================================================================================

# Утилита для автоматического просмотра новостей
# Установите необходимые зависимости: pip install selenium webdriver-manager
# апустите скрипт: python news_scraper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    """Настройка веб-драйвера"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Режим без графического интерфейса
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(
        service = Service(ChromeDriverManager().install()),
        options = chrome_options
    )
    return driver

def get_news_links(driver, url):
    """Получение списка ссылок на новости с главной страницы"""
    driver.get(url)
    time.sleep(3)  # Ожидание загрузки
    
    # Собираем все новостные карточки
    news_cards = driver.find_elements(By.CSS_SELECTOR, 'div[class*="gs-c-promo"] a.gs-c-promo-heading')
    
    # Извлекаем уникальные ссылки
    links = set()
    for card in news_cards:
        href = card.get_attribute('href')
        if href and '/news/' in href:  # Фильтруем только новостные ссылки
            links.add(href)
    
    return list(links)[:10]  # Берем первые 10 новостей для примера

def parse_news_page(driver, url):
    """Парсинг отдельной новостной страницы"""
    driver.get(url)
    time.sleep(2)
    
    try:
        # Извлекаем заголовок
        title = driver.find_element(By.TAG_NAME, 'h1').text
        
        # Извлекаем описание (может быть в разных местах)
        description = ""
        try:
            description = driver.find_element(By.CSS_SELECTOR, 'p[class*="ssrcss"]').text
        except:
            try:
                description = driver.find_element(By.CSS_SELECTOR, 'div[data-component*="text-block"] p').text
            except:
                description = "Не удалось извлечь описание"
        
        return {
            'title': title,
            'description': description[:200] + '...' if len(description) > 200 else description,
            'url': url
        }
    except Exception as e:
        print(f"Ошибка при парсинге {url}: {str(e)}")
        return None

def main():
    driver = setup_driver()
    main_url = "https://www.bbc.com/news"
    
    try:
        print("⏳ Собираю ссылки на новости...")
        news_links = get_news_links(driver, main_url)
        
        print(f"🔍 Найдено {len(news_links)} новостей. Парсинг...\n")
        
        for i, link in enumerate(news_links, 1):
            news_data = parse_news_page(driver, link)
            if news_data:
                print(f"📰 Новость #{i}")
                print(f"🔹 Заголовок: {news_data['title']}")
                print(f"🔹 Описание: {news_data['description']}")
                print(f"🔹 Ссылка: {news_data['url']}")
                print("-" * 80)
                
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        driver.quit()
        print("\n✅ Готово! Скрипт завершил работу.")

if __name__ == "__main__":
    main()

# Сохранение результатов:
import json

# В конец функции main() перед driver.quit()
with open('news_data.json', 'w', encoding = 'utf-8') as f:
    json.dump(all_news_data, f, ensure_ascii = False, indent = 2)

# Многопоточность для ускорения обработки:
from concurrent.futures import ThreadPoolExecutor

# Заменить цикл for в main() на:
with ThreadPoolExecutor(max_workers = 3) as executor:
    results = list(executor.map(lambda url: parse_news_page(driver, url), news_links))

# =========================================================================================================================================

# Скрипт для сбора данных с интернет-магазина
# Установите необходимые зависимости: pip install selenium webdriver-manager
# Запустите скрипт: python amazon_scraper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
from datetime import datetime

def setup_driver():
    """Настройка веб-драйвера с пользовательскими опциями"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Работа в фоновом режиме
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    
    driver = webdriver.Chrome(
        service = Service(ChromeDriverManager().install()),
        options = chrome_options
    )
    return driver

def accept_cookies(driver):
    """Принятие cookies, если появилось окно"""
    try:
        cookie_btn = driver.find_element(By.ID, "sp-cc-accept")
        cookie_btn.click()
        time.sleep(1)
    except:
        pass

def search_books(driver, search_query):
    """Поиск книг по запросу"""
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

def scrape_product_data(driver):
    """Сбор данных о товарах на странице"""
    products = []
    items = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    
    for item in items:
        try:
            # Название товара
            title = item.find_element(By.CSS_SELECTOR, "h2 a span").text
            
            # Цена (может быть несколько вариантов)
            try:
                price = item.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen").get_attribute("textContent")
            except:
                price = "Цена не указана"
            
            # Рейтинг
            try:
                rating = item.find_element(By.CSS_SELECTOR, "span.a-icon-alt").get_attribute("innerHTML")
            except:
                rating = "Нет рейтинга"
            
            # Ссылка на товар
            link = item.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
            
            products.append({
                "title": title,
                "price": price,
                "rating": rating,
                "link": link
            })
        except Exception as e:
            print(f"Ошибка при парсинге товара: {str(e)}")
            continue
    
    return products

def save_to_csv(data, filename):
    """Сохранение данных в CSV файл"""
    with open(filename, mode = 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.DictWriter(file, fieldnames = data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Данные сохранены в файл {filename}")

def main():
    driver = setup_driver()
    base_url = "https://www.amazon.com"
    
    try:
        # Открываем главную страницу
        driver.get(base_url)
        time.sleep(2)
        
        # Принимаем cookies
        accept_cookies(driver)
        
        # Ищем книги по запросу
        search_query = "Python programming"
        search_books(driver, search_query)
        
        # Собираем данные с первой страницы результатов
        print("⏳ Собираю данные о товарах...")
        products_data = scrape_product_data(driver)
        
        # Сохраняем данные
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"amazon_products_{timestamp}.csv"
        save_to_csv(products_data, filename)
        
        # Выводим статистику
        print(f"\n📊 Собрано данных о {len(products_data)} товарах")
        for i, product in enumerate(products_data[:3], 1):  # Показываем первые 3 для примера
            print(f"\nПример #{i}:")
            print(f"📖 Название: {product['title']}")
            print(f"💰 Цена: {product['price']}")
            print(f"⭐ Рейтинг: {product['rating']}")
            print(f"🔗 Ссылка: {product['link']}")
        
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        driver.save_screenshot("error.png")
    finally:
        driver.quit()
        print("\n✅ Скрипт завершил работу")

if __name__ == "__main__":
    main()

# Парсинг нескольких страниц:
def scrape_multiple_pages(driver, pages = 3):
    all_products = []
    for page in range(1, pages + 1):
        print(f"Парсинг страницы {page}...")
        all_products.extend(scrape_product_data(driver))
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
            next_btn.click()
            time.sleep(3)
        except:
            break
    return all_products

# ========================================================================================================================================================

# Приложение для автоматизации работы с почтовым ящиком
# Установите необходимые зависимости: pip install selenium webdriver-manager python-dotenv keyring
# Запустите приложение: python gmail_automation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass
from dotenv import load_dotenv
import os
import keyring

class GmailAutomation:
    def __init__(self, headless = True):
        """Инициализация драйвера"""
        self.chrome_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Убедитесь, что используете правильную версию ChromeDriver
        self.driver = webdriver.Chrome(
            service = Service(ChromeDriverManager().install()),
            options = self.chrome_options
        )
        self.wait = WebDriverWait(self.driver, 20)

    def login(self, email, password):
        """Авторизация в Gmail"""
        try:
            self.driver.get("https://mail.google.com")
            
            # Ввод email
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
            email_field.send_keys(email)
            email_field.send_keys(Keys.RETURN)
            
            # Ввод пароля
            password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            
            # Ожидание загрузки почты
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@role, 'main')]")))
            print("✅ Успешная авторизация")
            return True
        except Exception as e:
            print(f"❌ Ошибка авторизации: {str(e)}")
            return False

    def check_new_emails(self, max_emails = 5):
        """Проверка новых писем"""
        try:
            # Ожидаем загрузки списка писем
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='tabpanel']//tbody/tr")))
            
            # Получаем все письма
            emails = self.driver.find_elements(By.XPATH, "//div[@role='tabpanel']//tbody/tr")
            new_emails = []
            
            # Ограничиваем количество проверяемых писем
            for email in emails[:max_emails]:
                try:
                    # Проверяем, является ли письмо непрочитанным
                    is_unread = "zE" in email.get_attribute("class")
                    
                    if is_unread:
                        # Извлекаем информацию о письме
                        sender = email.find_element(By.XPATH, ".//span[@email]").text
                        subject = email.find_element(By.XPATH, ".//span[@class='bog']").text
                        snippet = email.find_element(By.XPATH, ".//span[@class='y2']").text
                        time_sent = email.find_element(By.XPATH, ".//td[@class='xW xY ']").text
                        
                        new_emails.append({
                            "sender": sender,
                            "subject": subject,
                            "snippet": snippet,
                            "time": time_sent,
                            "is_unread": is_unread
                        })
                        
                        # Помечаем как прочитанное (опционально)
                        email.click()
                        time.sleep(1)
                except Exception as e:
                    print(f"Ошибка при обработке письма: {str(e)}")
                    continue
            
            return new_emails
        except Exception as e:
            print(f"Ошибка при проверке писем: {str(e)}")
            return []

    def logout(self):
        """Выход из аккаунта"""
        try:
            # Открываем меню пользователя
            account_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@aria-label, 'Аккаунт Google')]")))
            account_button.click()
            
            # Нажимаем "Выйти"
            logout_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Выйти')]")))
            logout_button.click()
            print("✅ Успешный выход из аккаунта")
        except Exception as e:
            print(f"❌ Ошибка при выходе из аккаунта: {str(e)}")

    def close(self):
        """Закрытие браузера"""
        self.driver.quit()

def get_credentials():
    """Безопасное получение учетных данных"""
    try:
        # Попробуем получить из переменных окружения
        load_dotenv()
        email = os.getenv("GMAIL_EMAIL")
        password = os.getenv("GMAIL_PASSWORD")
        
        if not email or not password:
            # Если нет в переменных окружения, запросим у пользователя
            email = input("Введите ваш email Gmail: ")
            password = getpass.getpass("Введите ваш пароль: ")
            
            # Предложим сохранить в системном хранилище
            save = input("Сохранить учетные данные в безопасном хранилище? (y/n): ")
            if save.lower() == 'y':
                keyring.set_password("gmail_automation", email, password)
                print("🔐 Учетные данные сохранены в безопасном хранилище")
        
        return email, password
    except Exception as e:
        print(f"Ошибка при получении учетных данных: {str(e)}")
        return None, None

def main():
    print("🚀 Запуск Gmail Automation")
    
    # Инициализация
    gmail = GmailAutomation(headless = False)  # Установите False для видимого браузера
    
    # Получение учетных данных
    email, password = get_credentials()
    if not email or not password:
        print("❌ Не удалось получить учетные данные")
        return
    
    # Авторизация
    if gmail.login(email, password):
        # Проверка новых писем
        print("\n🔍 Проверяю новые письма...")
        new_emails = gmail.check_new_emails(max_emails = 10)
        
        if new_emails:
            print(f"\n📩 Найдено {len(new_emails)} новых писем:")
            for i, email in enumerate(new_emails, 1):
                print(f"\n✉️ Письмо #{i}")
                print(f"👤 Отправитель: {email['sender']}")
                print(f"📌 Тема: {email['subject']}")
                print(f"🕒 Время: {email['time']}")
                print(f"📝 Фрагмент: {email['snippet']}")
        else:
            print("📭 Новых писем не найдено")
        
        # Выход из аккаунта
        gmail.logout()
    
    # Завершение работы
    gmail.close()
    print("\n✅ Работа приложения завершена")

if __name__ == "__main__":
    main()

# Двухфакторная аутентификация:
def handle_2fa(self, code):
    """Обработка 2FA"""
    code_field = self.wait.until(EC.presence_of_element_located((By.NAME, "otp")))
    code_field.send_keys(code)
    code_field.send_keys(Keys.RETURN)

# Скачивание вложений:
def download_attachments(self, email_element):
    """Скачивание вложений из письма"""
    email_element.click()
    attachments = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@download, '')]")))
    for attachment in attachments:
        attachment.click()
        time.sleep(1)