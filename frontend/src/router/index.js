import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MainView from '../views/MainView.vue';
import Login from '../views/Login.vue';
import EditorView from '../views/EditorView.vue';
import Register from '../views/Register.vue';
// eslint-disable-next-line import/no-cycle
import store from '../store/index';

Vue.use(VueRouter);

function isAuthed() {
  return store.getters.isAuthenticated;
}

const routes = [
  {
    path: '/',
    name: 'Root',
    component: {
      render: (c) => c(isAuthed() ? HomeView : MainView),
    },
  },
  {
    path: '/editor',
    name: 'Editor',
    component: EditorView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    props: true,
    meta: {
      requiresDisAuth: true,
    },
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (isAuthed() && to.matched.some((record) => record.meta.requiresDisAuth)) {
    next(from);
  } else if (!isAuthed() && to.matched.some((record) => record.meta.requiresAuth)) {
    next('/login');
  } else {
    next();
  }
});

export default router;
