<template>
  <div>
    <LoginForm :parent-tab="tab" v-on:tab-changed="tabChanged($event)"/>
  </div>
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
      const type = tab ? 'signup' : 'signin';
      this.$router.push({
        path: this.$route.path,
        query: { type },
      }).catch((e) => e);
    },
  },
  beforeRouteUpdate(to, from, next) {
    next();
  },
};
</script>

<style scoped>

</style>
