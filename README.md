[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-orange)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-6-green)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Report-red)](https://docs.qameta.io/allure/)

[![Tests Passing](https://img.shields.io/badge/Tests-Passing-brightgreen)]()


## 📊 Allure Test Report

🔗 **[Live report:](https://Aznavyr.github.io/AQA-Python-Selenium/)**




# AQA Python Selenium Project / Проект автоматизации AQA на Python и Selenium

Автоматизация тестирования веб-приложения [SauceDemo](https://www.saucedemo.com) с использованием:
Automation of the [SauceDemo](https://www.saucedemo.com) web application using:

- Python 3.x  
- Selenium WebDriver  
- Page Object Pattern  
- pytest + pytest fixtures  
- YAML configuration (`settings.yaml`)  
- Allure for reporting  

---

## Структура проекта / Project structure

```
project/
│
├─ config/
│   ├─ config.py           # Загружает настройки из settings.yaml / Loads settings from settings.yaml
│   └─ settings.yaml       # Конфигурация браузеров, base_url, таймауты / Browser configuration, base_url, timeouts
│
├─ driver_factory.py       # Фабрика создания WebDriver с headless и параметрами / WebDriver factory with headless options
│
├─ pages/                  # PageObjects
│   └─ login_page.py
│
├─ tests/
│   ├─ conftest.py         # Фикстуры для pytest (driver, parametrize по браузерам) / Pytest fixtures (driver, browser parameterization)
│   ├─ test_login_page.py  # Тесты логина / Login tests
│   └─ ...
│
├─ utils/
│   └─ logger.py           # Настройка логирования / Logger setup
│
├─ requirements.txt        # Зависимости / Dependencies
└─ README.md
```

---

## Установка / Installation

1. Клонируем проект / Clone the project:

```bash
git clone <репозиторий>
cd project
```

2. Создаём и активируем виртуальное окружение / Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate       # Linux / Mac
.venv\Scripts\activate          # Windows
```

3. Устанавливаем зависимости / Install dependencies:

```bash
pip install -r requirements.txt
```

4. Установите Allure Commandline (для отчетов) / Install Allure Commandline:

- Windows: [Allure release](https://github.com/allure-framework/allure2/releases)  
- Добавьте `bin` папку в PATH / Add the `bin` folder to PATH  

Проверка / Check installation:

```bash
allure --version
```

---

## Конфигурация / Configuration

Файл `config/settings.yaml` содержит настройки / The `config/settings.yaml` file contains settings:

```yaml
base_url: "https://www.saucedemo.com"
timeout: 10

browser:
  name: "chrome"
  headless: False

browsers:
  chrome:
    name: "chrome"
    headless: True
    window_size: "1920,1080"
  firefox:
    name: "firefox"
    headless: True
```

- `headless` → True/False для запуска без UI / True/False for headless browser  
- `window_size` → размер окна браузера / Browser window size  
- `timeout` → WebDriverWait для элементов / WebDriverWait timeout  

---

## Запуск тестов / Running tests

### 1. pytest

```bash
pytest --alluredir=allure-results
```

- Фикстура `driver` из `conftest.py` поднимает **Chrome и Firefox** по очереди  
- Headless берётся из YAML / The `driver` fixture from `conftest.py` runs Chrome and Firefox sequentially Headless is taken from YAML  

### 2. Allure отчет / Allure report

```bash
allure serve allure-results
```

- Запускает локальный веб-сервер с интерактивным отчетом / Starts a local web server with interactive report  

---

## Структура тестов / Test scenarios

- Тесты используют **PageObject** (`pages/login_page.py`) / Test scenarios use **PageObject** (`pages/login_page.py`)  
- Примеры:  
  - Login с валидными данными / Valid user login
  - Login с невалидными данными / Invalid user login
  - Login с заблокированным пользователем / Locked user login
  - Login с пустыми полями / Empty fields login
  - Performance glitch user
- Все действия логируются через `logger` и шаги Allure через `@allure.step` / All actions are logged via `logger` and Allure steps using `@allure.step`  

---

## Логирование / Logging

- Логи действий браузера фиксируются в `utils/logger.py`/ 
Browser actions are logged in `utils/logger.py`  
- Тесты остаются чистыми / Tests remain clean  
- Пример шагов с логами: открытие страницы, заполнение формы, клик по кнопке / Example of logged steps: page open, fill form, click button  

---

## Контакты / Contacts

Автор / Author: Aznavyr  
QA Engineer  

