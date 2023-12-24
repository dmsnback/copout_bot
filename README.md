## Copout Bot

Профакапил? Сорвал сроки? Не знаешь что сказать боссу?
Бот помогающий с отмазками

- [Описание](#Описание)
- [Технологии](#Технологии)
- [Запуск](#Запуск)
- [Автор](#Автор)

### Описание
#
___Copout Bot___ - Telegram бот для парсинга отмазок с сайта [copout.me](http://copout.me). 
Создан на базе ____Selenium____ и ____Aiogram 3____ с целью их изучения.

### Технологии
#
![Static Badge](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python&logoColor=white&labelColor=black&cacheSeconds=3600)
![Static Badge](https://img.shields.io/badge/aiogram-3-black?style=for-the-badge&logo=aiogram&logoColor=white&labelColor=black&color=gray&cacheSeconds=3600)
![Static Badge](https://img.shields.io/badge/Selenium-black?style=for-the-badge&logo=Selenium&logoColor=white&link=https%3A%2F%2Fwww.selenium.dev%2F)


### Запуск
#
### Локальный запуск

 - __Клонировать репозиторий.__
```shell
git clone git@github.com:dmsnback/copout_bot.git
```
- __Перейти в директорию.__
```shell
cd copout_bot
```
- __Создать файл ```.env```.__
```shell
touch .env
```
- __Заполнить файл ```.env``` по шаблону__.
```python
API_TOKEN = Ваш токен
```
- __Установите и активируйте виртуальное окружение__
```shell
python3 -m venv venv
```
Для ```Windows```
```shell
source venv/Scripts/activate
```
Для ```Mac/Linux```
```shell
source venv/bin/activate
```
- __Установите зависимости из файла__ ```requirements.txt```

```shell
python3 -m pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```
- Выполнить запуск
```shell
python bot.py
```

### Автор

- [Титенков Дмитрий](https://github.com/dmsnback)
