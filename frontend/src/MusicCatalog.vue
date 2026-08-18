<template>
  <div class="catalog-container">
    <header class="catalog-header">
      <h1>Моя Медиатека</h1>
      <p class="subtitle">Коллекция любимых музыкальных альбомов</p>
    </header>

    <div class="albums-grid">
      <article 
        v-for="album in albums" 
        :key="album.id" 
        class="album-card"
      >
        <!-- Обложка и базовая инфо -->
        <div class="cover-wrapper">
          <img :src="album.cover" :alt="album.title" class="album-cover" />
          <div class="cover-overlay">
            <span class="release-year">{{ album.year }}</span>
          </div>
        </div>

        <!-- Описание альбома -->
        <div class="album-info">
          <h2 class="album-title">{{ album.title }}</h2>
          <p class="album-artist">{{ album.artist }}</p>
        </div>

        <!-- Список треков -->
        <div class="tracks-section">
          <h3 class="section-title">Треклист</h3>
          <ul class="tracks-list">
            <li 
              v-for="song in album.songs" 
              :key="song.number" 
              class="track-item"
            >
              <span class="track-number">{{ formatNumber(song.number) }}</span>
              <span class="track-name">{{ song.title }}</span>
            </li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Демо-данные для каталога
const albums = ref([
  {
    id: 1,
    title: 'Random Access Memories',
    artist: 'Daft Punk',
    year: 2013,
    cover: 'https://unsplash.com',
    songs: [
      { number: 1, title: 'Give Life Back to Music' },
      { number: 2, title: 'The Game of Love' },
      { number: 3, title: 'Giorgio by Moroder' },
      { number: 4, title: 'Within' },
      { number: 5, title: 'Instant Crush' }
    ]
  },
  {
    id: 2,
    title: 'The Dark Side of the Moon',
    artist: 'Pink Floyd',
    year: 1973,
    cover: 'https://unsplash.com',
    songs: [
      { number: 1, title: 'Speak to Me' },
      { number: 2, title: 'Breathe' },
      { number: 3, title: 'On the Run' },
      { number: 4, title: 'Time' },
      { number: 5, title: 'The Great Gig in the Sky' }
    ]
  },
  {
    id: 3,
    title: 'After Hours',
    artist: 'The Weeknd',
    year: 2020,
    cover: 'https://unsplash.com',
    songs: [
      { number: 1, title: 'Alone Again' },
      { number: 2, title: 'Too Late' },
      { number: 3, title: 'Hardest To Love' },
      { number: 4, title: 'Scared To Live' },
      { number: 5, title: 'Blinding Lights' }
    ]
  }
])

// Красивое форматирование номеров (01, 02 вместо 1, 2)
const formatNumber = (num) => {
  return num < 10 ? `0${num}` : num
}
</script>

<style scoped>
/* Стили контейнера и темы */
.catalog-container {
  min-height: 100vh;
  background-color: #121212;
  color: #ffffff;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  padding: 2rem;
}

.catalog-header {
  margin-bottom: 3rem;
  text-align: center;
}

.catalog-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  background: linear-gradient(45deg, #1db954, #1ed760);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subtitle {
  color: #b3b3b3;
  font-size: 1rem;
}

/* Сетка альбомов */
.albums-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

/* Карточка альбома */
.album-card {
  background: #181818;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #282828;
}

.album-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(29, 185, 84, 0.15);
  border-color: #383838;
}

/* Обложка */
.cover-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 1 / 1;
  overflow: hidden;
}

.album-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.album-card:hover .album-cover {
  transform: scale(1.05);
}

.cover-overlay {
  position: absolute;
  top: 12px;
  right: 12px;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
  padding: 4px 10px;
  border-radius: 20px;
}

.release-year {
  font-size: 0.8rem;
  font-weight: 600;
  color: #1db954;
}

/* Информация об альбоме */
.album-info {
  padding: 1.25rem 1.25rem 0.5rem 1.25rem;
}

.album-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0 0 0.25rem 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.album-artist {
  color: #b3b3b3;
  font-size: 0.95rem;
  margin: 0;
}

/* Секция треков */
.tracks-section {
  padding: 0 1.25rem 1.25rem 1.25rem;
}

.section-title {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #6a6a6a;
  margin: 1rem 0 0.5rem 0;
  border-bottom: 1px solid #282828;
  padding-bottom: 0.5rem;
}

.tracks-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.track-item {
  display: flex;
  align-items: center;
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.03);
}

.track-item:last-child {
  border-bottom: none;
}

.track-number {
  font-size: 0.85rem;
  color: #6a6a6a;
  width: 24px;
  font-variant-numeric: tabular-nums;
}

.track-name {
  font-size: 0.9rem;
  color: #e1e1e1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.track-item:hover .track-name {
  color: #1db954;
}
</style>