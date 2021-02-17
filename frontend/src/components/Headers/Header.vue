<template>
  <v-container class="pa-0 ma-0" v-bind:class="padding()">
    <v-app-bar app dense color="primary" dark
               v-bind:elevate-on-scroll="isMainPage() && !isAuthed()">
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-toolbar-title>Coding Rush</v-toolbar-title>
    </v-app-bar>
    <NavigationBar :parent-drawer="drawer" v-on:drawer-switched="drawer = $event"
                   :items="isAuthed() ? itemsAuthed : itemsUnauthed"/>
  </v-container>
</template>

<script>

import NavigationBar from '@/components/Headers/NavigationBar.vue';
import store from '@/store/index';

export default {
  name: 'HeaderUnauth',
  components: {
    NavigationBar,
  },
  data() {
    return {
      drawer: false,
      itemsAuthed: [
        {
          text: 'Close',
          icon: 'mdi-close',
          activating: false,
          function: () => { this.drawer = false; },
        },
        '',
        {
          text: 'Home',
          icon: 'mdi-home',
          path: '/',
          activating: true,
          function: (item) => this.goto(item),
        },
        {
          text: 'Typing',
          icon: 'mdi-keyboard',
          path: '/editor',
          activating: true,
          function: (item) => this.goto(item),
        },
        '',
        {
          text: 'Sign out',
          icon: 'mdi-account-cancel',
          activating: false,
          function: () => {
            this.drawer = false;
            this.$store.dispatch('logout')
              .then(() => this.goto('/'))
              // eslint-disable-next-line no-console
              .catch((err) => console.log(err));
          },
        },
      ],
      itemsUnauthed: [
        {
          text: 'Close',
          icon: 'mdi-close',
          activating: false,
          function: () => { this.drawer = false; },
        },
        '',
        {
          text: 'Main page',
          icon: 'mdi-star',
          path: '/',
          activating: true,
          function: (item) => this.goto(item),
        },
        '',
        {
          text: 'Sign in',
          icon: 'mdi-account-arrow-left',
          path: '/login?type=signin',
          activating: true,
          function: (item) => this.goto(item),
        },
        {
          text: 'Sign up',
          icon: 'mdi-account-plus',
          path: '/login?type=signup',
          activating: true,
          function: (item) => this.goto(item),
        },
      ],
    };
  },
  methods: {
    goto(item) {
      this.$router.push(item).catch((e) => e);
      this.drawer = false;
    },
    isMainPage() {
      return this.$route.name === 'Root';
    },
    isAuthed() {
      return store.getters.isAuthenticated;
    },
    padding() {
      if (this.isAuthed()) {
        return 'pa-3';
      }
      if (!this.isMainPage()) {
        return 'pb-12';
      }
      return false;
    },
  },
};
</script>

<style scoped>

</style>
