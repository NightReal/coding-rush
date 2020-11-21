import Vue from 'vue';
import Vuex from 'vuex';
// eslint-disable-next-line import/no-cycle
import APIHelper from '../api/apihelper';

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
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      state.user = {};
    },
    destroyAccess(state) {
      state.accessToken = null;
      localStorage.removeItem('accessToken');
    },
    updateAccess(state, access) {
      state.accessToken = access;
      localStorage.setItem('accessToken', access);
    },
    updateAll(state, { access, refresh }) {
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    updateUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    logout(context) {
      // TODO: Make server-side logout
      context.commit('destroyToken');
    },
    refresh(context) {
      context.commit('destroyAccess');
      return new Promise(((resolve, reject) => {
        APIHelper.post('/account/token/refresh/', {
          refresh: context.state.refreshToken,
        })
          .then((response) => {
            context.commit('updateAccess', response.data.access);
            return resolve();
          })
          .catch((err) => reject(err));
      }));
    },
    getUser(context) {
      return new Promise(((resolve, reject) => {
        APIHelper('/account/getme/')
          .then((response) => {
            context.commit('updateUser', response.data);
            return resolve();
          })
          .catch((err) => reject(err));
      }));
    },
    login(context, credentials) {
      return new Promise(((resolve, reject) => {
        APIHelper.post('/account/token/', {
          username: credentials.username,
          password: credentials.password,
        })
          .then((response) => {
            context.commit('updateAll', {
              access: response.data.access,
              refresh: response.data.refresh,
            });
            return resolve();
          })
          .catch((err) => reject(err));
      }));
    },
  },
  modules: {},
});
