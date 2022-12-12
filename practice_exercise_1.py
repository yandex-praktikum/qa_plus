from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
...

# Добавь явное ожидание загрузки страницы (подожди появления на странице описание профиля)
WebDriverWait(driver, 30).until(...)

# В переменную old_avatar_url сохрани ссылку на изображение
old_avatar_url = ...

# Кликни по изображению профиля
driver.find_element(...)...

# В поле ссылки на изображение введи ссылку, используй переменную avatar_url
avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"
driver.find_element(...)....

# Сохрани новое изображение
driver.find_element(...)...

# Обнови страницу
driver.refresh()

# Добавь явное ожидание загрузки страницы (подожди появления на странице описание профиля)
WebDriverWait(driver, 30).until(...)

# Запиши в переменную style значение атрибута style для элемента с изображением профиля
style = driver.find_element(...)...
# Проверь, что в style содержится ссылка на аватар
assert ...

# Верни старое изображение профиля
# Кликни по изображению профиля
driver.find_element(...)...

# В поле ссылки на изображение введи ссылку, используй переменную old_avatar_url
driver.find_element(...)....

# Сохрани старое изображение
driver.find_element(...)...

# Обнови страницу
driver.refresh()

# Добавь явное ожидание загрузки страницы (подожди появления на странице описание профиля)
WebDriverWait(driver, 30).until(...)

# Запиши в переменную style значение атрибута style для элемента с изображением профиля
style = driver.find_element(...)...
# Проверь, что в style содержится ссылка на старый аватар
assert ...

# Закрой браузер
driver.quit()
