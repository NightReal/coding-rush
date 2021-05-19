import axios from 'axios';
import Cookies from 'js-cookie';
// eslint-disable-next-line import/no-cycle
import store from '../store';

const APIHelper = axios.create({
  headers: {
    contentType: 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken'),
  },
  baseURL: '/api',
});

export const APIHelperFile = axios.create({
  headers: {
    contentType: 'multipart/form-data',
    'X-CSRFToken': Cookies.get('csrftoken'),
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
  if (error.response.status !== 401 || !store.getters.isAuthenticated) {
    return Promise.reject(error);
  }

  return store.dispatch('refresh')
    .then(() => {
      const originalRequest = error.config;
      originalRequest.headers.Authorization = `Bearer ${store.state.accessToken}`;

      return new Promise(((resolve, reject) => {
        APIHelper.request(originalRequest)
          .then((response) => {
            resolve(response);
          })
          .catch((err) => {
            store.dispatch('logout');
            reject(err);
          });
      }));
    })
    .catch(() => Promise.reject(error));
};

APIHelper.interceptors.request.use(
  (request) => requestInterceptor(request),
  (error) => Promise.reject(error),
);

APIHelper.interceptors.response.use(
  (response) => response,
  (error) => errorInterceptor(error),
);

export default APIHelper;
