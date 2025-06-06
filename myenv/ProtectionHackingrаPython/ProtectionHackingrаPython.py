# ==================================== Библиотеки для шифрования данных ====================================================

# Рассмотрим использование библиотеки cryptography для шифрования и дешифрования данных:
# использование библиотеки cryptography для шифрования и дешифрования данных
from cryptography.fernet import Fernet

# Генерируем ключ для шифрования
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Шифруем данные
# data = b"Секретная информация"
cipher_text = cipher_suite.encrypt(data)
print("Зашифрованные данные:", cipher_text)

# Дешифруем данные
plain_text = cipher_suite.decrypt(cipher_text)
print("Расшифрованные данные:", plain_text.decode())

# Рассмотрим использование библиотеки passlib для хеширования паролей и проверки аутентификации пользователей:
# Аутентификация пользователей:
from passlib.context import CryptContext

# Создаем объект контекста для хеширования паролей
pwd_context = CryptContext(schemes = ["bcrypt"])

# Хешируем пароль
hashed_password = pwd_context.hash("passwordl23")
print("Хешированный пароль:", hashed_password)

# Проверяем пароль
is_valid = pwd_context.verify("passwordl23", hashed_password)
print("Пapoль верный:", is_valid)

# Рассмотрим использование параметризованных запросов в базе данных для предотвращения атак SQL-инъекций:
# Защита от SQL-инъекций
import sqlite3
# Подключаемся к базе данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIМARY КЕУ, username ТЕХТ, password ТЕХТ)''')
# Добавляем пользователя (используем параметризованный запрос)

username = "user1"
password = "password123"
cursor.execute('''INSERT INTO users (username, password) VALUES (?, ? ) ''', (username, password))
conn.commit()
               
# Получаем пользователя (снова используем параметризованный запрос)        
username = "user1"
cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
user = cursor.fetchone()
print("Пользователь:", user)

# Закрываем соединение с базой данных
conn.close()

# Рассмотрим использование блоков try-except для обработки исключений и предотвращения утечек конфиденциальной информации:
try:
    # Код, который может вызвать исключение
    result = 10 / 0
except ZeroDivisionError:
    # Обработка исключения
    print("Ошибка деления на ноль")