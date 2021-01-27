import axios from 'axios';
import Cookies from 'js-cookie';
// eslint-disable-next-line import/no-cycle
import store from '../store';
// eslint-disable-next-line import/no-cycle
import router from '../router';

const APIHelper = axios.create({
  headers: {
    contentType: 'application/json',
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
  if (error.config && error.response && error.response.status === 401) {
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
      .catch((err) => Promise.reject(err));
  }
  if (error.config && error.response && error.response.status === 403) {
    // here we got hacked or refresh expired or we got invalid login.
    store.dispatch('logout');
    router.push('/login');
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
