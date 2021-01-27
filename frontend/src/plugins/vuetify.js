import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#2b2b2b',
        secondary: '#ffffff',
        accent: '#ff992e',
        error: '#b71c1c',
      },
    },
  },
});
