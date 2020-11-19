import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#2b2b2b',
        secondary: '#c9c9c9',
        accent: '#ffcb8c',
        error: '#b71c1c',
      },
    },
  },
});
