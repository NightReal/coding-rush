<template>
  <v-app>
    <Header/>

    <v-main class="pa-0 ma-0">
      <router-view/>
    </v-main>

    <Footer/>
  </v-app>
</template>

<script>

import Header from '@/components/Headers/Header.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'App',

  components: {
    Header,
    Footer,
  },
};
</script>

<style>

body {
  overflow-x: hidden;
}

</style>
