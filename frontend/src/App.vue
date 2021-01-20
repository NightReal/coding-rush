<template>
  <v-app>
    <HeaderAuth v-if="isAuthenticated()"/>
    <HeaderUnauth v-else :main-page="isRoot()"/>
    <v-main class="pa-0 ma-0">
      <router-view/>
    </v-main>

    <FooterBig v-if="isRoot()"/>
    <FooterSmall v-else/>
  </v-app>
</template>

<script>

import HeaderAuth from '@/components/Headers/HeaderAuth.vue';
import HeaderUnauth from '@/components/Headers/HeaderUnauth.vue';
import FooterBig from '@/components/Footers/FooterBig.vue';
import FooterSmall from '@/components/Footers/FooterSmall.vue';
import store from '@/store/index';

export default {
  name: 'App',

  components: {
    HeaderAuth,
    HeaderUnauth,
    FooterSmall,
    FooterBig,
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
