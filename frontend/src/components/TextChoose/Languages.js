import store from '@/store';

export const langColors = {
  python: '#ffeb3b',
  'c++': '#68d2ff',
  java: '#ff9a32',
};

export function changeLanguage(lang) {
  store.commit('updateLastUsedLanguage', lang);
}
