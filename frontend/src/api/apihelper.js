import axios from 'axios';
// eslint-disable-next-line import/no-cycle
import store from '../store';

const API = axios.create({
  headers: {
    contentType: 'application/json',
  },
  baseURL: '/api',
});

API.interceptors.request.use(
  (config) => {
    if (store.getters.isAuthenticated) {
      // eslint-disable-next-line no-param-reassign
      config.headers.Authorization = `Bearer ${store.state.accessToken}`;
    }
    return config;
  },
  (error) => {
    Promise.reject(error);
  },
);

export default API;
