import axios from 'axios';
// eslint-disable-next-line import/no-cycle
import store from '../store';

const APIHelper = axios.create({
  headers: {
    contentType: 'application/json',
  },
  baseURL: '/api',
});

const requestInterceptor = (request) => {
  if (store.getters.isAuthenticated) {
    // eslint-disable-next-line no-param-reassign
    request.headers.Authorization = `Bearer ${store.state.accessToken}`;
  }
  return request;
};

const errorInterceptor = (error) => {
  const originalRequest = error.config;
  if (error.config && error.response && error.response.status === 403) {
    store.dispatch('refresh')
      .then(() => {
        console.log(originalRequest);
        originalRequest.headers.Authorization = `Bearer ${store.state.accessToken}`;
        return APIHelper(originalRequest);
      })
      .catch((err) => Promise.reject(err));
  }
};

APIHelper.interceptors.request.use(
  (request) => requestInterceptor(request),
  (error) => {
    Promise.reject(error);
  },
);

APIHelper.interceptors.response.use(
  (response) => response,
  (error) => errorInterceptor(error),
);

export default APIHelper;
