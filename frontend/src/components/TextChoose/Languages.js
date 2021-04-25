import store from '@/store';

export const langColors = {
  python: '#ffeb3b',
  'c++': '#68d2ff',
  java: '#ff7575',
};

export function changeLanguage(lang) {
  store.commit('updateLastUsedLanguage', lang);
}
