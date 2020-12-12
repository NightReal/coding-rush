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
  name: 'HeaderAuth',
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
            this.$store.dispatch('logout')
              .then(() => this.goto('/login'))
              .catch((err) => console.log(err));
          },
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
