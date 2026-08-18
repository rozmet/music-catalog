# Music Catalog App

Веб-приложение для каталогизации музыкальных альбомов. 

## Технологический стек
* **Backend:** Python, Django, DRF, PostgreSQL
* **Frontend:** Vue 3 (Composition API), Vite, Pinia, Quasar, Tailwind CSS
* **Инфраструктура:** Docker, Docker Compose

## Архитектура БД
Реализована связь "Многие-ко-многим" (Many-to-Many) между `Album` и `Song` через промежуточную модель `AlbumTrack` для хранения уникального порядкового номера песни в рамках конкретного альбома.

## Быстрый запуск (Через Docker)

1. Клонируйте репозиторий:
   ```bash
   git clone [https://github.com/rozmet/music-catalog.git](https://github.com/rozmet/music-catalog.git)
   cd music-catalog
