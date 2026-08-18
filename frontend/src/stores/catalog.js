import { defineStore } from 'pinia';
import api from '../api';

export const useCatalogStore = defineStore('catalog', {
  state: () => ({
    albums: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchAlbums() {
      this.loading = true;
      try {
        const response = await api.get('albums/');
        this.albums = response.data;
      } catch (err) {
        this.error = 'Не удалось загрузить каталог альбомов';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },
  },
});