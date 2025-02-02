# 🩺 Трекер артериального давления

Трекер артериального давления - это веб-приложение, построенное на Django, которое позволяет пользователям записывать и отслеживать показания своего артериального давления с течением времени.

## ✨ Функции

- 🔐 Аутентификация пользователей
- 📝 Создание записей артериального давления
- 👀 Просмотр последней записи артериального давления
- 📊 Просмотр статистики показаний артериального давления за определенный период (последние 24 часа или последние 30 дней)

## 📋 Предварительные требования

- 🐳 Docker и Docker Compose
- 🐙 Git
- 🛠️ Make

## ⚙️ Установка и настройка

1. 📥 Клонируйте репозиторий:
   ```bash
   git clone https://github.com/deymonster/blood_pressure_tracker.git
   cd blood-pressure-tracker
   ```

2. 🏗️ Соберите и запустите Docker контейнеры:
   ```bash
   make build
   make run
   ```

3. После запуска контейнеров откройте новый терминал и выполните следующие команды для настройки базы данных:
   ```bash
   make migrate
   make createsuperuser
   ```
   Следуйте подсказкам для создания учетной записи администратора.

4. 🌐 Приложение теперь должно быть доступно по адресу `http://localhost:8000`

## 🚀 Использование

1. Перейдите по адресу `http://localhost:8000/admin/` в вашем веб-браузере
2. 🔑 Войдите в систему, используя учетные данные администратора
3. После авторизации вы сможете использовать все функции приложения:
   - 📝 Создание новой записи артериального давления
   - 👀 Просмотр последней записи артериального давления
   - 📊 Просмотр статистики артериального давления за определенный период

Примечание: Все функции доступны только после авторизации.

## 📂 Структура проекта

Основная папка проекта - `blood_pressure_tracker`, которая содержит:

- 📁 `blood_pressure_project/`: Основные настройки проекта Django
- 📁 `tracker/`: Приложение Django для отслеживания артериального давления
- 📁 `templates/`: HTML шаблоны
- ⚙️ `manage.py`: Утилита командной строки Django для административных задач
- 🐳 `Dockerfile`: Инструкции для сборки Docker образа
- 🐳 `docker-compose.yml`: Конфигурация Docker Compose
- 📜 `requirements.txt`: Зависимости Python
- 📜 `pyproject.toml`: Файл конфигурации Poetry
- 📜 `Makefile`: Файл с командами для сборки и управления проектом

## 🛠️ Разработка

Этот проект использует Poetry для управления зависимостями. Если вы хотите добавить или обновить зависимости, вы можете использовать следующие команды:

- ➕ Добавить новую зависимость: `poetry add имя_пакета`
- 🔄 Обновить зависимости: `poetry update`

После обновления зависимостей обязательно пересоберите ваши Docker контейнеры:


```
make stop
make build
make run
```


