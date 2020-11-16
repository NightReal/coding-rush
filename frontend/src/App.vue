<template>
  <v-app>
    <Header v-if="!isLogging()"/>
    <HeaderLogin v-else/>
    <v-main>
      <router-view/>
    </v-main>
    <Footer/>
  </v-app>
</template>

<script>

import Header from '@/components/Header.vue';
import HeaderLogin from '@/components/HeaderLogin.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'App',

  components: {
    Header,
    HeaderLogin,
    Footer,
  },

  methods: {
    isLogging() {
      return this.$router.currentRoute.path === '/';
    },
  },
};
</script>
