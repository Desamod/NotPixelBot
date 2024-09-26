[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f342952117)

## Рекомендация перед использованием

# 🔥🔥 Используйте PYTHON 3.10 🔥🔥

> 🇪🇳 README in english available [here](README.md)

## Функционал  
| Функционал                                              | Поддерживается |
|---------------------------------------------------------|:--------------:|
| Многопоточность                                         |       ✅        |
| Поддержка tdata / pyrogram .session / telethon .session |       ✅        |
| Привязка прокси к сессии                                |       ✅        |
| Привязка User-Agent к сессии                            |       ✅        |
| Авторегистрация в боте                                  |       ✅        |
| Авто-закрашивание пикселей                              |       ✅        |
| Авто-выполнение тасок                                   |       ✅        |
| Авто-сбор наград за майнинг PX                          |       ✅        |
| Авто-апгрейд усилителей                                 |       ✅        |




## [Настройки](https://github.com/Desamod/NotPixelBot/blob/master/.env-example/)
| Настройка               |                              Описание                               |
|-------------------------|:-------------------------------------------------------------------:|
| **API_ID / API_HASH**   |        Данные платформы, с которой запускать сессию Telegram        | 
| **SLEEP_TIME**          |        Время сна между циклами (по умолчанию - [3200, 3600])        |
| **START_DELAY**         |     Задержка между сессиями на старте (по умолчанию - [5, 20])      |
| **AUTO_PAINT**          |          Авто-закрашивание пикселей (по умолчанию - True)           |
| **AUTO_MINING**         |          Авто-сбор наград за майнинг (по умолчанию - True)          |
| **AUTO_TASK**           |             Авто-выполнение тасок (по умолчанию - True)             |
| **AUTO_UPGRADE_PAINT**  |      Авто-апгрейд бустера 'Paint Reward' (по умолчанию - True)      |
| **MAX_PAINT_LEVEL**     |   Максимальный уровень прокачки 'Paint Reward' (по умолчанию - 5)   |
| **AUTO_UPGRADE_CHARGE** |    Авто-апгрейд бустера 'Recharging Speed' (по умолчанию - True)    |
| **MAX_CHARGE_LEVEL**    | Максимальный уровень прокачки 'Recharging Speed' (по умолчанию - 5) |
| **AUTO_UPGRADE_ENERGY** |      Авто-апгрейд бустера 'Energy Limit' (по умолчанию - True)      |
| **MAX_ENERGY_LEVEL**    |   Максимальный уровень прокачки 'Energy Limit' (по умолчанию - 2)   |
| **REF_ID**              |                 Реф. ссылка для регистрации в боте                  |

## Быстрый старт 📚

Для быстрой установки и последующего запуска - запустите файл run.bat на Windows или run.sh на Линукс

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **версии 3.10**

## Получение API ключей
1. Перейдите на сайт [my.telegram.org](https://my.telegram.org) и войдите в систему, используя свой номер телефона.
2. Выберите **"API development tools"** и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/Desamod/NotPixelBot) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/Desamod/NotPixelBot
cd NotPixelBot
```

Затем для автоматической установки введите:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux ручная установка
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
python3 main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/NotPixelBot >>> python3 main.py --action (1/2)
# Or
~/NotPixelBot >>> python3 main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```


# Windows ручная установка
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/NotPixelBot >>> python main.py --action (1/2)
# Или
~/NotPixelBot >>> python main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```

### Использование
При первом запуске бота создайте для него сессию с помощью команды «2». В процессе будет создана папка 'sessions', в которой хранятся все сессии, а также файл accounts.json с конфигурациями.
Если у вас уже есть сессии, просто поместите их в папку 'sessions' и запустите кликер. В процессе запуска вы сможете настроить использование прокси для каждой сессии.
Юзер-агент создается для каждого аккаунта автоматически.

Пример того, как должен выглядеть accounts.json:
```shell
[
  {
    "session_name": "name_example",
    "user_agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
    "proxy": "type://user:pass:ip:port"   # "proxy": "" - если прокси не используется
  }
]
```

### Контакты

Для поддержки или вопросов, вы можете связаться со мной

[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/desforge_crypto)

