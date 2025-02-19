# Django Rest Framework Social Network

## О проекте
Этот проект представляет собой псевдосоциальную сеть, разработанную с использованием Django и Django Rest Framework (DRF). Реализована система аутентификации с использованием Token Authentication и JWT Authentication через библиотеку Djoser.

## Стек технологий
- Python 3.11
- Django 4.x
- Django Rest Framework (DRF)
- Djoser (аутентификация через Token и JWT)
- SQLite (по умолчанию)

## Установка и запуск проекта

### 1. Клонирование репозитория
```bash
git clone https://github.com/Emir4ikkk/RestFrameWork.git
cd RestFrameWork
```

### 2. Создание и активация виртуального окружения
```bash
python -m venv venv  # создание виртуального окружения
source venv/bin/activate  # активация в macOS/Linux
venv\Scripts\activate  # активация в Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Применение миграций и запуск сервера
```bash
python manage.py migrate
python manage.py runserver
```
Сервер запустится на [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API

### **1. Аутентификация**
Используется Djoser для обработки регистрации, входа и управления пользователями.

- **Регистрация**: `POST /auth/users/`
- **Вход по JWT**: `POST /auth/jwt/create/`
- **Обновление токена**: `POST /auth/jwt/refresh/`
- **Выход**: `POST /auth/token/logout/`

---

### **2. Работа с категориями (CRUD)**
Эндпоинты для управления категориями блога.

- **Получение списка**: `GET /api/categories/`
- **Создание**: `POST /api/categories/`
- **Детальный просмотр**: `GET /api/categories/{id}/`
- **Обновление**: `PUT /api/categories/{id}/`
- **Удаление**: `DELETE /api/categories/{id}/`

---

### **3. Работа с публикациями (CRUD)**
Эндпоинты для управления публикациями.

- **Получение списка публикаций**: `GET /api/publications/`
- **Создание публикации** _(только авторизованные пользователи)_: `POST /api/publications/`
- **Детальный просмотр публикации**: `GET /api/publications/{id}/`
- **Редактирование публикации** _(только владелец)_: `PUT /api/publications/{id}/`
- **Удаление публикации** _(только владелец)_: `DELETE /api/publications/{id}/`

---

### **4. Взаимодействия между пользователями**
Добавление функционала подписок и лайков.

- **Подписаться на пользователя**: `POST /api/follow/{user_id}/`
- **Отписаться от пользователя**: `DELETE /api/follow/{user_id}/`
- **Лайкнуть публикацию**: `POST /api/publications/{id}/like/`
- **Убрать лайк**: `DELETE /api/publications/{id}/like/`

---
