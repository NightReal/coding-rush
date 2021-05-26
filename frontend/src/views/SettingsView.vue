<template>
  <div>
    <page-loader :loading="loading"></page-loader>
    <Settings></Settings>
  </div>
</template>

<script>

import Settings from '@/components/Settings/Settings.vue';
import PageLoader from '@/components/PageLoader.vue';

export default {
  name: 'EditorView',
  components: {
    Settings,
    PageLoader,
  },
  data: () => ({
    loading: false,
  }),
  mounted() {
    if (!this.$store.getters.user.username) {
      this.loading = true;
      this.$store.dispatch('getUser').then(() => { this.loading = false; });
    }
  },
};
</script>
