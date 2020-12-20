<template>
  <v-container>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-toolbar-title>Coding Rush</v-toolbar-title>
    </v-app-bar>
    <NavigationBar :parent-drawer="drawer" :items="items" v-on:drawer-switched="drawer = $event"/>
  </v-container>
</template>

<script>

import NavigationBar from '@/components/Headers/NavigationBar.vue';

export default {
  name: 'HeaderUnauth',
  components: {
    NavigationBar,
  },
  data() {
    return {
      drawer: false,
      items: [
        {
          text: 'Close',
          icon: 'mdi-close',
          activating: false,
          function: () => { this.drawer = false; },
        },
        '',
        {
          text: 'Main page',
          icon: 'mdi-compass-outline',
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
    },
  },
};
</script>
