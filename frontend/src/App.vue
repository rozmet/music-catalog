<template>
  <div class="catalog-container">
    <header class="catalog-header">
      <h1>Медиатека</h1>
      <p class="subtitle">Коллекция любимых музыкальных альбомов</p>
    </header>

    <div class="albums-grid">
      <article 
        v-for="album in catalogStore.albums" 
        :key="album.id" 
        class="album-card"
      >
        <!-- Обложка и базовая инфо -->
        <div class="cover-wrapper">
          <img :src="album.cover" :alt="album.title" class="album-cover" />
          <div class="cover-overlay">
            <span class="release-year">{{ album.release_year }}</span>
          </div>
        </div>

        <!-- Описание альбома -->
        <div class="album-info">
          <h2 class="album-title">{{ album.title }}</h2>
          <p class="album-artist">{{ album.artist_name }}</p>
        </div>

        <!-- Список треков -->
        <div class="tracks-section">
          <h3 class="section-title">Треклист</h3>
          <ul class="tracks-list">
            <li 
              v-for="track in album.tracks" 
              :key="track.id" 
              class="track-item"
            >
              <span class="track-number">{{ track.track_number }}</span>
              <span class="track-name">{{ track.song_title }}
              </span>
            
            </li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
@import "./MusicCatalog.css";
</style>


<script setup>
import { onMounted } from 'vue';
import { useCatalogStore } from './stores/catalog';

const catalogStore = useCatalogStore();

onMounted(() => {
  catalogStore.fetchAlbums();
});
</script>