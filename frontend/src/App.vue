<template>
  <v-app>
    <Header/>
    <v-main>
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
    Header: {
      render: (c) => c(store.getters.isAuthenticated ? HeaderAuth : HeaderUnauth),
    },
    Footer,
  },
};
</script>
