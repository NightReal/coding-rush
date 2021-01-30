<template>
  <v-app>
    <HeaderAuth v-if="isAuthenticated()"/>
    <HeaderUnauth v-else :main-page="isRoot()"/>

    <v-main class="pa-0 ma-0">
      <router-view/>
    </v-main>

    <Footer/>
  </v-app>
</template>

<script>

import HeaderAuth from '@/components/Headers/HeaderAuth.vue';
import HeaderUnauth from '@/components/Headers/HeaderUnauth.vue';
import Footer from '@/components/Footer.vue';
import store from '@/store/index';

export default {
  name: 'App',

  components: {
    HeaderAuth,
    HeaderUnauth,
    Footer,
  },
  methods: {
    isAuthenticated() {
      return store.getters.isAuthenticated;
    },
    isRoot() {
      return this.$route.name === 'Root';
    },
  },
};
</script>
