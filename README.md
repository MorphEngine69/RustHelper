# RustHelper Discord Bot

## Функции:
- Рассчитать сколько нужно ресурсов на определенное количество взрывчатки
- Узнать сколько потребуется взрывчатки на определенный объект
- Узнать как лутать определенное рт
- Узнать сколько нужно ресурсов на застройку печки

## Как пользоваться:
После установки и настройки вашего бота, запустить его и в чат ввести команду !help или сокращенно !h

## Системные требования
```sh
Python 3.9+
Windows/Linux/macOS
```
---

## Установка проекта на Windows

1. Клонировать репозиторий на компьютер и перейти в него из командной строки:
```sh
git clone git@github.com:MorphEngine69/RustHelper.git

cd RustHelper
```

2. Создать и активировать виртуальное окружение:
```sh
python -m venv env

source venv/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:
```sh
pip install -r requirements.txt
```

4. В директории создать файл .env и вставить токен от вашего дискорд бота как в примере .env.example:
```sh
touch .env
```

5. Запустить бота:
```sh
python bot.py
```
---

## Установка проекта на Linux и macOS

1. Клонировать репозиторий на компьютер и перейти в него из командной строки:
```sh
git clone git@github.com:MorphEngine69/RustHelper.git

cd RustHelper
```

2. Создать и активировать виртуальное окружение:
```sh
python3 -m venv venv

source venv/bin/activate
```

3. Установить зависимости из файла requirements.txt:
```sh
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

4. В директории создать файл .env и вставить токен от вашего дискорд бота как в примере .env.example:
```sh
touch .env
```

5. Запустить бота:
```sh
python3 bot.py
```

