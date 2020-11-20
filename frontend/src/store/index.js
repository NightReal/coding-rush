import Vue from 'vue';
import Vuex from 'vuex';
// eslint-disable-next-line import/no-cycle
import API from '../api/apihelper';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: localStorage.getItem('accessToken') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
    user: {},
  },
  getters: {
    isAuthenticated: (state) => state.accessToken != null,
  },
  mutations: {
    destroyToken(state) {
      state.accessToken = null;
      state.refreshToken = null;
      state.user = {};
    },
    updateAccess(state, access) {
      state.accessToken = access;
    },
    updateAll(state, { access, refresh }) {
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);
      state.accessToken = access;
      state.refreshToken = refresh;
    },
  },
  actions: {
    logout(context) {
      // TODO: Make server-side logout
      context.commit('destroyToken');
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    },
    login(context, credentials) {
      return new Promise(((resolve, reject) => {
        API.post('/account/token/', {
          username: credentials.username,
          password: credentials.password,
        })
          .then((response) => {
            context.commit('updateAll', {
              access: response.data.access,
              refresh: response.data.refresh,
            });
            resolve();
          })
          .catch((err) => {
            reject(err);
          });
      }));
    },
  },
  modules: {},
});
