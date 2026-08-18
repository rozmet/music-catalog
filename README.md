# 🎵 Music Catalog Application

Веб-приложение для каталогизации музыкальных альбомов, исполнителей и треков, разработанное по принципам Schema-Driven Design (SDD).

## 🛠 Технологический стек

* **Backend:** Python 3.11, Django 5, Django REST Framework (DRF), PostgreSQL, Pillow, Corsheaders, Python-dotenv.
* **Frontend:** Vue 3 (Composition API `<script setup>`), Vite, Pinia, Quasar Framework, Tailwind CSS, Axios.
* **Infrastructure:** Docker, Docker Compose, Git.

---

## 📐 Архитектура данных (Schema-Driven Design)

Центральный элемент архитектуры — гибкая связь между альбомами и песнями. Одна и та же песня может входить в разные альбомы под разными порядковыми номерами.

* **Artist** (Исполнитель): `id`, `name`.
* **Song** (Песня): `id`, `title`.
* **Album** (Альбом): `id`, `title`, `artist` (FK -> Artist), `release_year`, `cover` (ImageField), `songs` (ManyToMany -> Song through AlbumTrack).
* **AlbumTrack** (Промежуточная модель): `album` (FK), `song` (FK), `track_number` (PositiveIntegerField). Установлена уникальность пар `('album', 'track_number')`.

---

## 📁 Структура проекта

```text
music-catalog/
├── backend/                  # Django REST Framework API
│   ├── core/                 # Основной модуль настроек (settings/base.py, dev.py, prod.py)
│   ├── catalog/              # Django-приложение (models, views, serializers, urls)
│   ├── media/album-cover      # Загружаемые обложки альбомов
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                 # Vue 3 Single Page Application
│   ├── src/
│   │   ├── stores/           # Pinia stores (catalog.js)
│   │   ├── api.js            # Axios client
│   │   ├── MusicCatalog.css  # App Page css style
│   │   └── App.vue
│   ├── Dockerfile
│   └── package.json
├── .env.example              # Шаблон переменных окружения
├── docker-compose.yml        # Файл оркестрации контейнеров
└── README.md
```

---

## 🚀 Быстрый запуск (Docker Compose)


**1. Клонирование и настройка окружения**
   ```bash
   git clone [https://github.com/rozmet/music-catalog.git](https://github.com/rozmet/music-catalog.git)
   cd music-catalog
   ```

Создайте файл `.env` в корне проекта на основе шаблона:
   ```bash
   cp .env.example .env
   ```

Пример содержания `.env`:
   ```bash
       # Django settings
    DJANGO_SECRET_KEY=your-generated-django-secret-key
    DJANGO_DEBUG=False

    DJANGO_SETTINGS_MODULE = 'core.settings.prod'
    ALLOWED_HOSTS = ['*'] # Укажите ваш домен

    # Database settings
    DB_NAME=DB_NAME
    DB_USER=DB_USER
    DB_PASSWORD=DB_PASSWORD
    DB_HOST=db
    DB_PORT=5432
   ```

**2. Запуск контейнеров**
Запустите сборку и старт всех сервисов (PostgreSQL, Django, Vue.js):
   ```bash
   docker compose up --build
   ```

**3. Создание администратора**
В новом окне терминала создайте суперпользователя для доступа к админ-панели:
   ```bash
   docker compose exec backend python manage.py createsuperuser
   ```

## 🔗 Доступ к сервисам

|**Сервис**|**URL**|
|---|---|
|**Frontend (Vue 3 UI)**|[http://localhost:5173](http://localhost:5173/)|
|**Backend API**|[http://localhost:8000/api/albums/](http://localhost:8000/api/albums/)|
|**Django Admin**|[http://localhost:8000/admin/](http://localhost:8000/admin/)|
|**Media (Обложки)**|[http://localhost:8000/media/](http://localhost:8000/media/)|


## 💻 Локальный запуск без Docker (Альтернативный вариант)

### Backend

1. Перейдите в папку `backend`: `cd backend`
2. Создайте и активируйте venv: `python -m venv venv && source venv/bin/activate` (или `venv\Scripts\activate` на Windows)
3. Установите зависимости: `pip install -r requirements.txt`
4. Примените миграции: `python manage.py migrate`
5. Запустите сервер: `python manage.py runserver`
    

### Frontend

1. Перейдите в папку `frontend`: `cd frontend`
2. Установите зависимости: `npm install`
3. Запустите dev-сервер: `npm run dev`
