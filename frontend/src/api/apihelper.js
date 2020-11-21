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
  if (error.config && error.response && error.response.status === 403) {
    return store.dispatch('refresh')
      .then(() => {
        const originalRequest = error.config;
        originalRequest.headers.Authorization = `Bearer ${store.state.accessToken}`;
        // return APIHelper(originalRequest);
        return new Promise(((resolve, reject) => {
          APIHelper.request(originalRequest).then((response) => {
            resolve(response);
          }).catch((err) => {
            reject(err);
          });
        }));
      })
      .catch((err) => {
        Promise.reject(err);
      });
  }
  return new Promise(((resolve, reject) => {
    reject(error);
  }));
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
