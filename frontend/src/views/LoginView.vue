<template>
  <v-container style="display: flex; justify-content: space-around">
    <LoginForm :parent-tab="tab" v-on:tab-changed="tabChanged($event)"/>
  </v-container>
</template>

<script>
import LoginForm from '@/components/LoginForm/LoginForm.vue';

export default {
  name: 'Login.vue',
  components: { LoginForm },
  data() {
    return {
      tab: 0,
    };
  },
  methods: {
    tabChanged(tab) {
      this.tab = tab;
      const path = tab === 0 ? '/signin' : '/signup';
      this.$router.push({ path }).catch((e) => e);
    },
  },
  beforeRouteUpdate(to, from, next) {
    next();
    this.tab = to.path === '/signup' ? 1 : 0;
  },
  mounted() {
    this.tab = this.$route.path === '/signup' ? 1 : 0;
  },
};
</script>
